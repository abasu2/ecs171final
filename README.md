# ECS 171 Project

This repository has two components: the report and the code, under folders report and code.

# Report

The report is the 8-10 page final report formatted according to IEEE guidelines. The content of the report is split into `.tex` files under `report/src`.

## Requirements

Refer the requirements from [latex-workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop).

### For Windows

You can use either [MiKTeX](https://miktex.org/) or [TeX Live](https://www.tug.org/texlive/). Install as instructed.

### For macOS

Install [MacTeX](https://www.tug.org/mactex/) as instructed from the website.

### For Linux

Install the required package for `pdflatex` and `bibtex` according to your chosen distro.

For Ubuntu:

```bash
sudo apt-get -qq update && sudo apt-get install -y --no-install-recommends \
    dvipng texlive-latex-recommended \
    texlive-fonts-recommended \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-bibtex-extra biber xzdec
```

For Manjaro:

```bash
pacman -Syu texlive-core texlive-fontsextra texlive-latexextra texlive-science texlive-bibtexextra biber
```

## Usage

To build the project report and open it, change your working directory to `report` and use the provided makefile.

### For Linux
```bash
cd report
make
```

# Code

The code includes all the models and data visualization.

## Requirements

The requirements for running the code are given in `requirements.txt`. To install the requirements, use the pip package manager and run `pip install -r requirements.txt`.
