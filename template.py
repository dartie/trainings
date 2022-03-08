template = """<!doctype html>
<html lang="en">

	<head>
		<meta charset="utf-8">

		<title>{title}</title>

		<meta name="description" content="A framework for easily creating beautiful presentations using HTML">
		<meta name="author" content="Dario Necco">

		<meta name="apple-mobile-web-app-capable" content="yes">
		<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

		<meta name="viewport" content="width=device-width, initial-scale=1.0">

		<link rel="stylesheet" href="dist/reset.css">
		<link rel="stylesheet" href="dist/reveal.css">
		<link rel="stylesheet" href="dist/admonitions.css">		
		<link rel="stylesheet" href="dist/theme/{theme}.css" id="theme">

		<!-- Theme used for syntax highlighting of code -->
        <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.2/styles/default.min.css">-->
		<link rel="stylesheet" href="plugin/highlight/monokai.css" id="highlight-theme">
		
		<!-- Third Party Plugin for copy code snippet -->
		<link rel="stylesheet" href="plugin/copycode/copycode.css">

        <style>
            .copy-code-button {
                color: #272822;
                background-color: #FFF;
                border-color: #272822;
                border: 2px solid;
                border-radius: 3px 3px 0px 0px;
            
                /* right-align */
                display: block;
                margin-left: auto;
                /* margin-right: -18px; */
                /* margin-bottom: -60px; */
                margin-right: 0px;
                margin-bottom: -45px;
                padding: 3px 8px;
                font-size: 0.4em;
            }
            
            .copy-code-button:hover {
                cursor: pointer;
                background-color: #F2F2F2;
            }
            
            .copy-code-button:focus {
                /* Avoid an ugly focus outline on click in Chrome,
                   but darken the button for accessibility.
                   See https://stackoverflow.com/a/25298082/1481479 */
                background-color: #E6E6E6;
                outline: 0;
            }
            
            .copy-code-button:active {
                background-color: #D9D9D9;
            }
            
            .highlight pre {
                /* Avoid pushing up the copy buttons. */
                margin: 0;
            }
        </style>

	</head>

	<body>

		<div class="reveal">

			<!-- Any section element inside of this container is displayed as a slide -->
			<div class="slides">

                {content}

			</div>

		</div>

		<script src="dist/reveal.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.6/clipboard.min.js"></script>
        <script src="plugin/copycode/copycode.js"></script>
		<script src="plugin/zoom/zoom.js"></script>
		<script src="plugin/notes/notes.js"></script>
		<script src="plugin/search/search.js"></script>
		<script src="plugin/markdown/markdown.js"></script>
		<script src="plugin/highlight/highlight.js"></script>
		
		<!-- Third-Party Plugin for menu -->
        <script src="plugin/menu/menu.js"></script>

		<script>

			// Also available as an ES module, see:
			// https://revealjs.com/initialization/
			Reveal.initialize({
				controls: true,
				progress: true,
				center: true,
				hash: true,
				slideNumber: true,

                copycode: {
                    copy: "Copy",
                    copied: "Copied!",
                    timeout: 1000,
                    copybg: "orange",
                    copiedbg: "green",
                    copycolor: "black",
                    copiedcolor: "white"
                },

				// Learn about plugins: https://revealjs.com/plugins/
				plugins: [ RevealZoom, RevealNotes, RevealSearch, RevealMarkdown, RevealHighlight, RevealMenu, CopyCode ]
			});

		</script>
		
		<script>
		function addCopyButtons(clipboard) {
            document.querySelectorAll('pre > code').forEach(function (codeBlock) {
                var button = document.createElement('button');
                button.className = 'copy-code-button';
                button.type = 'button';
                button.innerText = 'Copy';
        
                button.addEventListener('click', function () {
                    clipboard.writeText(codeBlock.innerText).then(function () {
                        /* Chrome doesn't seem to blur automatically,
                           leaving the button in a focused state. */
                        button.blur();
        
                        button.innerText = 'Copied!';
        
                        setTimeout(function () {
                            button.innerText = 'Copy';
                        }, 2000);
                    }, function (error) {
                        button.innerText = 'Error';
                    });
                });
        
                var pre = codeBlock.parentNode;
                if (pre.parentNode.classList.contains('highlight')) {
                    var highlight = pre.parentNode;
                    highlight.parentNode.insertBefore(button, highlight);
                } else {
                    pre.parentNode.insertBefore(button, pre);
                }
            });
        }
        /*
        if (navigator && navigator.clipboard) {
            addCopyButtons(navigator.clipboard);
        } else {
            var script = document.createElement('script');
            script.src = 'https://cdnjs.cloudflare.com/ajax/libs/clipboard-polyfill/2.7.0/clipboard-polyfill.promise.js';
            script.integrity = 'sha256-waClS2re9NUbXRsryKoof+F9qc1gjjIhc2eT7ZbIv94=';
            script.crossOrigin = 'anonymous';
            script.onload = function() {
                addCopyButtons(clipboard);
            };
        
            document.body.appendChild(script);
        }
        */
		</script>

	</body>
</html>
"""