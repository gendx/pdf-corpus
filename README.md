# PDF corpus

This project allows to quickly create hand-crafted PDF files.
The main Python script `pdf-corpus.py` is an ad-hoc template engine to easily prototype new PDFs.

## Installation

To compile the corpus, just `make` it (you need a Python interpreter).
All `.txt` files contained in the `corpus/` folder are then converted into PDFs.

## Description

Each PDF in the corpus is described by a `.txt` file that indicates the template to use and the content to insert in the template.
The following templates are defined, but you can easily create your own by tweaking the Python code.

* `contentstream`: A simple document containing one page in A4 format.
You define the graphic commands to put in the page's content stream (see my [cheat sheet](https://github.com/gendx/pdf-cheat-sheets/blob/master/pdf-graphics.clean.pdf)).
For convenience, a font resource is declared as `/F1`.
* `objects`: A lower level template to directly declare objects.
Simple streams can be defined, for which the template computes the `/Length` field.


# Available corpus

The corpus already contains some files.
These examples are classified into the following categories.

* `corpus/contentstream/`: Playing with graphics instructions.
* `corpus/name/`: Escape sequences in names.
* `corpus/number/`: How numbers are parsed.

If you want to learn more about how these examples work, you can have a look at my blog posts: [introduction to PDF syntax](https://gendignoux.com/blog/2016/10/04/pdf-basics.html).
I also make one-page [cheat sheet(s)](https://github.com/gendx/pdf-cheat-sheets) about PDF.
For further details you can also dive into the [PDF specification](https://www.adobe.com/devnet/pdf/pdf_reference.html).

## Disclaimer

Once compiled, these example files may not be fully compliant with the [specification](https://www.adobe.com/devnet/pdf/pdf_reference.html).
In particular, they may be interpreted differently by different PDF readers.

## License

MIT

