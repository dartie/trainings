#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Dario Necco"

import locale
import os
import sys
import argparse
from argparse import ArgumentParser, RawTextHelpFormatter
import logging
import inspect
import markdown
import bs4
import re

# import template.py which holds the html base content
from template import template

# import Namespace
try:
    from types import SimpleNamespace as Namespace  # available from Python 3.3
except ImportError:
    class Namespace:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

if sys.version[0] == '2':
    from imp import reload

    reload(sys)
    sys.setdefaultencoding("utf-8")

# import Colorama
try:
    from colorama import init, Fore, Back, Style

    init(strip=True)  # strip makes colorama working in PyCharm
except ImportError:
    print('Colorama not imported')

locale.setlocale(locale.LC_ALL, 'C')  # set locale

# set version and author
__version__ = 1.0

# I obtain the app directory
if getattr(sys, 'frozen', False):
    # frozen
    dirapp = os.path.dirname(sys.executable)
    dirapp_bundle = sys._MEIPASS
    executable_name = os.path.basename(sys.executable)
else:
    # unfrozen
    dirapp = os.path.dirname(os.path.realpath(__file__))
    dirapp_bundle = dirapp
    executable_name = os.path.basename(__file__)

##############################################################################################
# DEBUG
this_scriptFile = inspect.getfile(inspect.currentframe())
this_scriptFile_filename = os.path.basename(this_scriptFile)
this_scriptFile_filename_noext, ext = os.path.splitext(this_scriptFile_filename)

# logging.basicConfig(filename=this_scriptFile_filename_noext + '.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')  # uncomment for Logging

print('Working dir: \\"' + dirapp + '\\"')
welcome_text = '{char1} {appname} v.{version} {char2}'.format(char1='-' * 5,
                                                              appname=os.path.splitext(os.path.basename(__file__))[0],
                                                              version=__version__, char2='-' * 5)
print(welcome_text)
logging.info(welcome_text)


def print_color(text, color):
    print('{color}{text}{reset_color}'.format(color=color, text=text, reset_color=Style.RESET_ALL))


def print_error(text):
    print('{color}{text}{reset_color}'.format(color=Fore.RED, text=text, reset_color=Style.RESET_ALL))


def print_warning(text):
    print('{color}{text}{reset_color}'.format(color=Fore.YELLOW, text=text, reset_color=Style.RESET_ALL))


def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]


def remove_suffix(text, suffix):
    return text[:-len(suffix)] if text.endswith(suffix) and len(suffix) != 0 else text


def _prettify(self, indent_width=4):
    r = re.compile(r'^(\s*)', re.MULTILINE)
    return r.sub(r'\1' * indent_width, bs4.BeautifulSoup(self, features="lxml").prettify())

#bs4.BeautifulSoup.prettify = prettify


def remove_additional_tags(html_text):
    """
    Removes tags added automatically by bs4 parser (html, head and body) as this is a snippet
    :param html_text:
    :return:
    """
    clean = remove_prefix(html_text, '<html><body>')
    clean = remove_suffix(clean, '</body></html>')

    return clean


def adjust_slide_html(slide_content_html):
    # handle code blocks incorrectly shown as inline code blocks
    # code_regex = re.compile(r'^ {4}<code>((.|\n)*?)<\/code>', re.MULTILINE)
    # slide_content_html = code_regex.sub("<pre><code>\g<1></code></pre>", slide_content_html)

    soup = bs4.BeautifulSoup(slide_content_html, 'lxml')
    code_tags = soup.findAll('code')

    for code in code_tags:
        # remove code tag in case of a snippet (only block, keeping it for inline) without language,
        # so that the syntax highlighting is not applied
        # add class 'inline' for handling the inline text.
        if 'class' not in code.attrs and str(code).endswith('\n</code>'):
            code.name = ''
        elif 'class' not in code.attrs:
            code.attrs['class'] = 'inline'

    # remove empty tags caused by "code" tags removal for rendering properly the plain text without syntax highlighting
    clean = str(soup).replace('<pre><>', '<pre>').replace('</></pre>', '</pre>')

    # remove tags added automatically by bs4 parser (html, head and body) as this is a snippet
    clean = remove_additional_tags(clean)

    # manage attributes for code
    regex_line_info = re.compile(r'>\{(.*)\}$')
    regex_line_info_sub = re.compile(r'\{(.*)\}$')
    clean_html_split = clean.split('\n')
    for i, cl in enumerate(clean_html_split):
        string_to_add_list = regex_line_info.findall(cl)

        if not string_to_add_list or not [x for x in string_to_add_list if "data-line-numbers" in x]:
            continue

        string_to_add = ' '.join(string_to_add_list) + ' '

        # Adding a string to recognize where the extra CRLF needs to be removed.
        cl_clean = regex_line_info_sub.sub('<!--CR-TO-REMOVE-->', clean_html_split[i], 1)

        # add option as code attribute
        clean_html_split[i] = cl_clean.replace('<pre><code ', '<pre><code ' + string_to_add)
        clean_html_split[i] = cl_clean.replace('><!--CR-TO-REMOVE-->', ' ' + string_to_add + '><!--CR-TO-REMOVE-->')

    clean_html_string = '\n'.join(clean_html_split)

    # moving the line attribute/s from snippet to code attributes left an empty line in the code snippet content
    # I replaced with "<!--CR-TO-REMOVE-->"
    # Now I'm removing "<!--CR-TO-REMOVE-->\n" for aligning the code at line 1
    regex_remove_cr_firstline = re.compile(r'(<!--CR-TO-REMOVE-->[\s])', re.MULTILINE)
    clean_html_string = regex_remove_cr_firstline.sub('', clean_html_string)

    return clean_html_string


def check_args():
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter, description="""
Reveal-deck converts a markdown file to reveal.js slides. It require a custom syntax only for handling:

* Vertical slides (https://revealjs.com/vertical-slides)
    
    ---# means Horizontal slide
    
    ---## means child Vertical slide

* Syntax highlighting focus / animation (https://revealjs.com/code/)
    ```go 
    {data-line-numbers="1,2|5-6"}
    
    ...
    ```
    
    where: 
    , comma adds more lines to highlight
    | char means it highlights on next shift (arrow down)
    - dash specifies a range of lines to highlight 
    
    """)

    # Options
    parser.add_argument("-debug", dest="debug", action='store_true', help=argparse.SUPPRESS)
    # help='Increase output verbosity. Output files don\\'t overwrite original ones'

    parser.add_argument("-b", "--background", dest="background", default="")

    parser.add_argument("-t", "--theme", dest="theme",
                        default='black.css',
                        choices=[x.rstrip('.css') for x in os.listdir(os.path.join(dirapp_bundle, 'dist', 'theme')) if x.lower().endswith('.css')]
                        )

    parser.add_argument("-op", "--output", dest="output_path",
                        help="qac output path. it has given in input to this application")

    parser.add_argument("files", nargs='+',
                        help="Markdown files to convert to presentations")

    args = parser.parse_args()  # it returns input as variables (args.dest)
    # end check args

    return args


def main(args=None):
    if args is None:
        args = check_args()

    # set background value
    if not args.background == '':
        background = ' data-background-image="{}"'.format(args.background)
    else:
        background = ""

    for file in args.files:
        with open(file, 'r', encoding='utf-8', errors='ignore') as read_md:
            md_content = read_md.readlines()

        ___count = 0
        end_header_index = None
        index = -1
        for l in md_content:
            index += 1
            l_strip = l.strip()

            if l_strip == '---':
                ___count += 1

            if ___count == 2:
                end_header_index = index
                break

        presentation_md_content = ''.join(md_content[end_header_index + 1:])
        slides = presentation_md_content.split('---#')

        slides_dict = {}
        slides_html_dict = {}

        slide_index = -1
        for s in slides:
            if s.replace('\n', '') == '':
                continue

            if not s.startswith('#'):
                slide_index += 1
                slides_dict[slide_index] = []
                slides_html_dict[slide_index] = []

            slide_content_markdown = remove_prefix(remove_prefix(s, '#'), '\n')
            slides_dict[slide_index].append(slide_content_markdown)

            slide_content_html = markdown.markdown(slide_content_markdown, indentation=4, output_format='html', extensions=['pymdownx.superfences', 'pymdownx.emoji', 'markdown.extensions.tables', 'markdown.extensions.admonition', 'toc', 'pymdownx.mark'])  # , 'codehilite' enables pygments for syntax highlighting

            # adjust html slide content
            slide_content_html = adjust_slide_html(slide_content_html)

            slides_html_dict[slide_index].append(slide_content_html)

        presentation_html_snippet = ''

        section_template = """<section{}>
{}
</section>        
"""

        for horizontal, vertical_content_list in slides_html_dict.items():
            section_snippet_list = [section_template.format(background, x) for x in vertical_content_list]

            if len(vertical_content_list) > 1:
                section_snippet = section_template.format(background, ''.join(section_snippet_list))
            else:
                section_snippet = ''.join(section_snippet_list)

            presentation_html_snippet += section_snippet

        # print(presentation_html_snippet)

        # write presentation to file
        output_file = os.path.splitext(file)[0] + '.html'
        with open(output_file, 'w', encoding='utf-8', errors='ignore') as write_presentation:
            slide_output = template.replace('{content}', presentation_html_snippet)
            slide_output = slide_output.replace('{theme}', args.theme)
            slide_output = slide_output.replace('{title}', os.path.splitext(file)[0])
            write_presentation.write(slide_output)
        print('"{}" output created!'.format(output_file))


if __name__ == '__main__':
    try:
        main(args=None)
    except KeyboardInterrupt:
        print('\\n\\nBye!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

# TODO: H1 should be fixed on top of the browser
# TODO: href should be opened in a new tab (or an option shuold be available)
