# -*- coding: utf-8 -*-

import rsa


def create_keys():  # 创建公钥和私钥并保存
    (pub_key, priv_key) = rsa.newkeys(1024)
    pub = pub_key.save_pkcs1()
    with open('public.pem', 'wb+') as f:
        f.write(pub)

    pri = priv_key.save_pkcs1()
    with open('private.pem', 'wb+')as f:
        f.write(pri)


def encrypt():  # 用公钥加密
    with open('public.pem', 'rb') as publickfile:
        p = publickfile.read()
    pub_key = rsa.PublicKey.load_pkcs1(p)
    with open('D:\spiderman2\crawlframe\spiders\imei-MD5.txt', 'rb') as f:  # 需要加密的文件流
        original_text = f.read()
    crypt_text = rsa.encrypt(original_text, pub_key)
    print(crypt_text)
    print(str(crypt_text))
    print(len(crypt_text))
    return crypt_text   # 加密后的密文


def decrypt(crypt_text):    # 用私钥解密
    with open('private.pem', 'rb') as privatefile:
        p = privatefile.read()
    priv_key = rsa.PrivateKey.load_pkcs1(p)
    final_text = rsa.decrypt(crypt_text, priv_key).decode()
    print(final_text)


if __name__ == '__main__':
    # create_keys()
    crypt_text = encrypt()
    # decrypt(crypt_text)

