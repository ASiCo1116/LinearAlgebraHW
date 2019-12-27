import numpy as np
from util import mod_inv


def get_key(cipher, plain):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?!'
    #TODO
    '''
    Calculate public key with cipher text and plain text.

    Arguments:
        cipher: str, cipher text
        plain: str, plain text

    Return:
        key: str, public key
    '''

    cipher_list = [letters.index(i) for i in cipher]
    cipher_np = np.reshape(cipher_list, (-1, 3)).T

    plain_list = [letters.index(i) for i in plain]
    plain_np = np.reshape(plain_list, (-1, 3)).T

    pub_key = np.mod(cipher_np @ mod_inv(plain_np), 31)
    key_list = []
    for k in pub_key.flatten():
      key_list.append(str(k))
    key = ' '.join(key_list)
    return key

