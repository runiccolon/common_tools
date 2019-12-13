# -*- coding: utf-8 -*-
from base64 import b64decode
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


# AES CBC模式
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


# 加密函数
def encryt(text):
    key = 'zhaobingqianqian'.encode('utf-8')    # 此处key必须是16,24,32位中任选其一
    mode = AES.MODE_CBC
    iv = b'baishitongshumei'    # 偏移量iv
    text = add_to_16(text)
    cryptos = AES.new(key, mode, iv)
    cipher_text = cryptos.encrypt(text)
    return b2a_hex(cipher_text)


# 解密函数
def decrypt(text):
    key = 'zhaobingqianqian'.encode('utf-8')
    mode = AES.MODE_CBC
    iv = b'baishitongshumei'
    cryptos = AES.new(key, mode, iv)
    plain_text = cryptos.decrypt(a2b_hex(text))
    return bytes.decode(plain_text).rstrip('\0')


# AES ECB模式(无需偏移量)

# def add_to_16(text):
#     if len(text.encode('utf-8')) % 16:
#         add = 16 - (len(text.encode('utf-8')) % 16)
#     else:
#         add = 0
#     text = text + ('\0' * add)
#     return text.encode('utf-8')


# 加密函数
def ecb_encryt(text):
    key = 'zhaobingqianqian'.encode('utf-8')
    mode = AES.MODE_ECB
    text = add_to_16(text)
    cryptos = AES.new(key, mode)
    cipher_text = cryptos.encrypt(text)
    return b2a_hex(cipher_text)


# 解密函数
def ecb_decrypt(text):
    key = 'zhaobingqianqian'.encode('utf-8')
    mode = AES.MODE_ECB
    cryptos = AES.new(key, mode)
    plain_text = cryptos.decrypt(a2b_hex(text))
    return bytes.decode(plain_text).rstrip('\0')


if __name__ == '__main__':
    e = encryt('万里悲秋常作客,百年多病独登台')   # 加密
    d = decrypt(e)
    print(e, "\n", d)

    e1 = ecb_encryt('万里悲秋常作客,百年多病独登台')
    d1 = ecb_decrypt(e1)
    print(e1, "\n", d1)




