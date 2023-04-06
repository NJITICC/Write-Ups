# QR


## Steganography

## Description

My stupid kid drew on this QR code with his crayons. Figure it out. He was a mistake.


## What's Provided:

One photo: qr.png


# Steps:

Solving this took some learning. I honestly had no idea how QR Codes worked. So I took to Google, searching QR code repair.

One of the first sites I found gave me a suitable amount of information to go off of ->[DataGenetics](http://datagenetics.com/blog/november12013/index.html).

There I learned why the art was so destructive: It covered all of the necessary info at least partially. That means that the positioning, format information, timing marks, version info, spacing, and alignment were all pretty well broken.

So how do you fix it? My first step was... tedious. I went to [Photopea](https://photopea.com) and began manually fixing each square. It felt like when a plastic surgeon removes the skin from your leg to repair a face. 

Did it look good? No. Not at all. 
Was it passable? Also no. I am not a good surgeon or a good graphic designer.

So rather than waste three more hours of my life, I found a new tool: [QRazyBox](https://merricx.github.io/qrazybox/). This tool allowed me to really explore a QR - see the bit info and repair without the extremely boring job of cutting, copying, and pasting tiny squares all over this QR.

Eventually I got far enough to uncover the flag. 
RS{CUE_ARE_D3C0D3D}