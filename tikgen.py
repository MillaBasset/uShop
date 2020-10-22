import keygen
import binascii

def main(tid, path):
    print(f"Generating title.tik for Title ID {tid}...")

    with open(f"{path}/title.tik", 'wb+') as outputTik:
        with open('basetik.tik', 'rb') as tik:
            outputTik.write(tik.read())
            outputTik.seek(0x1BF)
            outputTik.write(binascii.unhexlify(keygen.main(tid)))
            outputTik.seek(0x1DC)
            outputTik.write(binascii.unhexlify(tid))
