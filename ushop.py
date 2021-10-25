#!/usr/bin/env python3
import wiiu_cdndownload
import sys
import keygen

if not keygen.verify_ckey():
    print("The common key is invalid.")
    print("To use this tool, you must have the common key in ckey.txt,")
    print("with the key being in the first line.")
elif len(sys.argv) == 1 or len(sys.argv[1]) != 16:
    print("Invalid or missing Title ID.")
    print(f"Usage: {sys.argv[0]} (Title ID) [version]")
    sys.exit(1)
else:
    if len(sys.argv) == 2:
        wiiu_cdndownload.runDownload(sys.argv[1])
    elif len(sys.argv) == 3:
        wiiu_cdndownload.runDownload(sys.argv[1], sys.argv[2])
    else:
        print('Too many arguments.')
