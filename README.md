# BMP Transformer

This is a small project made without fee on request from an industrial knitting factory in Sweden, which feeds its (old) machines with images containing patterns to knit. Compatibility errors due to the images' bit depth, transparency layer or file format were frequently encountered, which is why they asked me for a small application that converts to the correct file format, and allows resizing and stretching.

Feel free to take inspiration from, modify or improve this small project to your liking without notice to me as long as it is in accordance with the licenses of [Pillow](https://github.com/python-pillow) and [PySimpleGUI](https://github.com/PySimpleGUI).

### Usage

1) Start **main.py**
2) Choose file with the button 'Choose file...'
3) Check 'Use original dimensions' to do so, otherwise specify new dimensions using the available inputs. Rescaling can be done by inputting a float value in the scale input.
4) Press 'Transform'
5) The transformed picture is outputted in alongside the original with the ending *_tr*

This application takes all common file formats (jpeg, png, tif, jp2 and bmp among others) and outputs a 3 layer bitmap image with bit depth 24.

### Screenshot

![Screenshot of main window](screenshot.png?raw=true "Screenshot of main window")

### Credits:


The Python Imaging Library (PIL) is

    Copyright © 1997-2011 by Secret Labs AB
    Copyright © 1995-2011 by Fredrik Lundh

Pillow is the friendly PIL fork. It is

    Copyright © 2010-2020 by Alex Clark and contributors

The full Python-Pillow license can be found [here](https://github.com/python-pillow/Pillow/blob/master/LICENSE).