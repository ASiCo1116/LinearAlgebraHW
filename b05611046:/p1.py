import numpy as np
from util import mod_inv

def decode(cipher, key):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?!'
    #TODO
    '''
    Decode cipher with public key.

    Arguments:
        cipher: str, cipher text
        key: str, public key

    Return:
        plain: str, plain text
    '''
    cipher_list = [letters.index(i) for i in cipher]
    cipher_np = np.reshape(cipher_list, (-1, 3)).T
    
    pub_key = [int(k) for k in key.split()]
    pub_key_np = np.reshape(pub_key, (-1, 3))
    pri_key = mod_inv(pub_key_np)
    
    plain_np = np.mod(pri_key @ cipher_np, 31)
    plain_list = []
    for p in plain_np.T.flatten():
      plain_list.append(letters[p])
    plain = ''.join(plain_list)
    return plain
