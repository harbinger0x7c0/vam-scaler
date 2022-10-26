# VAM Scaler
People make some really cool stuff for Virt-A-Mate, but I'm not sure why Imp
Midna needs a 4k texture just for her genital area. Regular old HD seems
perfectly reasonable to me and also means I can fit a lot more genital textures
on my hard drive. Do you also want to fit more genital textures on your hard
drive? Ask your doctor if VAM Scaler is right for you.

## What it does
This is a very early version, so the functionality may well improve, but for now
it's pretty basic. It just unpacks any var files you give it, looks for any jpg
or png files inside, and if they are 4k it scales them down to 1k. Then it packs
everything back up into a new var with the old var's name.

In case you didn't notice, that means the original var will be lost. Back it up
if you don't want that to happen.

## What it needs
- To run on linux
  - It assumes linux-style path separators. You might could make it work on Mac
  OS, but I won't help you do it.
- ImageMagick available on $PATH
- Python3
  - Seriously, it's been out for like 10 years already.

## How to use it
You can tell it to process one or more var files, like so:

`vamscaler.py file1.var file2.var etc.var`

## How to get help or make a suggestion
File an issue, and be civil and patient. I take a perverse pleasure in being
mean to people I think have been rude to me.
