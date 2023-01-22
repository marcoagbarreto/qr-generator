# QR-Generator

This is a program to generate and read QR codes.

## Example
Generator
1. Run [qr-generator]().
2. Input some text or JSON file.
3. Hit Generate.
3. Profit.
4. Save the image.

Reader
1. Run [qr-generator]().
2. Input a QR code image.
3. Hit Decode.
4. SUPER Profit.

![example](example.gif)

## Code Usage

clone the repository (no installation required, source files are sufficient):
        
[//]: # (    https://github.com/marcoagbarreto/pixelsPatterns.git)

dependencies:

    from flask import Flask, render_template, request
    import qrcode
    import cv2
    import json
    import base64
    import io

[//]: # (or [download and extract the zip]&#40;https://github.com/marcoagbarreto/pixelsPatterns/archive/main.zip&#41; into your project folder.)

## Known limitations:
* Only text and JSON files can be converted to a QR code.
