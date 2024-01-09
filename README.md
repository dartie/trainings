# Trainings
Tool to convert markdown documents to [revealjs](https://revealjs.com/) slides.

- [Trainings](#trainings)
  - [Syntax](#syntax)
    - [Slides navigation](#slides-navigation)
    - [Admonitions](#admonitions)
    - [Support for code line numbers](#support-for-code-line-numbers)
  - [Setup](#setup)
  - [Usage](#usage)


## Syntax

Syntax to use in the markdown document to covert it properly to revealjs slides.

### Slides navigation
* `---#` : new horizontal slide
* `---##` : new vertical slide

### Admonitions

* Supported syntax : [Mkdocs Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

```
!!! note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
```

```
!!! danger

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
```

### Support for code line numbers
Setting the first line of the code snippet as
```
{data-line-numbers="all|2|all"}
```

allows to:

* show line numbers
* highlight specific numbers

**Usage:**

* `1,5` : highlights lines 1 and 5
* `1-5` : highlights lines from 1 to 5 (range)
* `all` : highlights all lines
* `|` char creates a transition

````
```c++
{data-line-numbers="all|2|all"}
int main() {
  return 0;
}
```
````


## Setup 

```bash
# Create dedicated virtual environment 
# (it avoids to encounter issues with markdown conversion)
virtualenv venv-trainings

# Enable virtual environment
source venv-trainings/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Usage

```bash
# syntax
python create-preso.py "<file.md>" - t "<theme-name>"

# syntax
python create-preso.py Go-Nalug.md -t nalug
```