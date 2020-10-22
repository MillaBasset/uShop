from hashlib import pbkdf2_hmac, md5
import binascii
from Crypto.Cipher import AES
import os
import sys

def generate_key(title_id, pwd):
    # remove 00 padding from title id
    title_idGen = title_id[2:]

    # get secret string, append title id, and convert to binary string
    secret = binascii.unhexlify('fd040105060b111c2d49' + title_idGen)
    # get md5 hash of secret
    hashed_secret = md5(secret).digest()
    
    # key is a pbkdf2 hash with sha1 base using hashed_secret as salt and 20 iterations
    non_encrypted_key = binascii.hexlify(pbkdf2_hmac('sha1', pwd.encode(), hashed_secret, 20, 16))

    title_id += '0000000000000000'
    title_id = binascii.unhexlify(title_id)
    ckey = binascii.unhexlify(get_ckey())
    title_key = binascii.unhexlify(non_encrypted_key)
    encryptor = AES.new(key=ckey, mode=AES.MODE_CBC, IV=title_id)
    encrypted_title_key = encryptor.encrypt(title_key)

    # return as hexstring
    return binascii.hexlify(encrypted_title_key)

def get_ckey() -> str:
    if not os.path.exists('ckey.txt'):
        print('Common key was not found. Please create a file called ckey.txt and write the cmmon key in the first line.')
        sys.exit(0)

    with open('ckey.txt', 'r') as f:
        return f.readline().replace('\r', '').replace('\n', '')

def verify_ckey():
    if md5(get_ckey().upper().encode()).hexdigest() == '35ac5994972279331d97094fa2fb97fc':
        return True

def main(tid, password='mypass'):
    return generate_key(tid, password);