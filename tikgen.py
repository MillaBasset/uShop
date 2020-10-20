import keygen
import io
import os
import binascii

def main(tid):
    ckey = keygen.get_ckey()
    
    tik = open('basetik.tik', 'rb')

    baseTik = io.BytesIO(tik.read())

    tik.close()

    keys = keygen.main(tid, ckey)

    currentTik = baseTik
    currentTik.seek(0x1BF)
    currentTik.write(binascii.unhexlify(keys[0]))
    currentTik.seek(0x1DC)
    currentTik.write(binascii.unhexlify(tid))

    os.mkdir(tid)
    a = open(f"{tid}/title.tik", 'wb+')

    currentTik.seek(0)
    a.write(currentTik.read())
    a.close()