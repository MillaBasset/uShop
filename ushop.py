import subprocess
import sys
import keygen, tikgen

if not keygen.verify_ckey(keygen.get_ckey()):
    print("The common key is invalid.")
    print("To use this tool, you must have the common key in ckey.json.")
elif len(sys.argv) == 1 or len(sys.argv[1]) != 16:
    print("Invalid TID length, or TID is missing.")
    print(f"Usage: ushop.py <titleid> [version]")
    sys.exit(1)
else:
    tikgen.main(sys.argv[1])
    if len(sys.argv) == 2:
        subprocess.call([sys.executable, "./wiiu_cdndownload.py", sys.argv[1]])
    elif len(sys.argv) >= 3:
        subprocess.call([sys.executable, "./wiiu_cdndownload.py", sys.argv[1], sys.argv[2]])