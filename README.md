# uShop
Downloads Wii U games in an installable format from the CDN.

## What this program will do
This program will download the .app/.h3/.cert/.tmd files from the CDN.  
It will then generate a .tik file in the same directory.  
You can install the contents generated by this program with [WUP Installer GX2](https://sourceforge.net/projects/wup-installer-gx2/).

## Disclaimer
This program is largely unfinished. Report any bugs in issues, please.

## Usage
You must have the Wii U common key in the file named ckey.json.

    $ ./ushop.py <titleid> [version]

## Credits
[ihaveamac](https://github.com/ihaveamac) for his [wiiu-things](https://github.com/ihaveamac/wiiu-things) repository.  
[dojafoja](https://github.com/dojafoja) for his [Kii-U-Generator](https://github.com/dojafoja/Kii-U-Generator).  
[TimmSkiller](https://github.com/TimmSkiller) for figuring out that the Wii U uses the same ticket structure as the 3DS, and making a utility to generate tickets for me.
