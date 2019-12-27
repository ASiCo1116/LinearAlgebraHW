import sys
import numpy as np
import math

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_wave(x, path = './wave.png'):
    plt.gcf().clear()
    plt.plot(x)
    plt.xlabel('n')
    plt.ylabel('xn')
    plt.savefig(path)

def plot_ak(a, path = './freq.png'):
    plt.gcf().clear()

    # Only plot the mag of a
    a = np.abs(a)
    plt.plot(a)
    plt.xlabel('k')
    plt.ylabel('ak')
    plt.savefig(path)

def CosineTrans(x, B):
    # TODO
    # implement cosine transform

    return np.linalg.inv(B) @ x

def InvCosineTrans(a, B):
    # TODO
    # implement inverse cosine transform

    return B @ np.array(a, dtype = np.int32)

def gen_basis(N):
    # TODO
    basis = []
    for k in range(N):
      basis_inner = []
      for n in range(N):
        if k == 0:
          basis_inner.append(1/N**.5)
        else:
          basis_inner.append((2/N)**.5 * math.cos((n + .5) * k * math.pi / N))
      basis.append(basis_inner)
    return np.array(basis, dtype = np.float64).T

if __name__ == '__main__':

    signal_path = sys.argv[1]

    x = np.loadtxt(signal_path, dtype = np.float64).reshape(-1, 1)
    
    B = gen_basis(1000)

    a = CosineTrans(x, B)

    where = [1 if x > 10 else 0 for x in a]

    loc = []
    for i, j in enumerate(where):
      if j == 1:
        loc.append(i) #f1 = 30 , f3 = 268
    # print(loc)

    mask1 = [1 if x == loc[0] else 0 for x in range(1000)]
    mask2 = [1 if x == loc[2] else 0 for x in range(1000)]
    
    mask1 = np.array(mask1).reshape(-1, 1)
    mask2 = np.array(mask2).reshape(-1, 1)

    # plot_ak(a * mask1, '1.png')

    a1 = a * mask1
    a3 = a * mask2

    f1 = InvCosineTrans(a1, B)
    f3 = InvCosineTrans(a3, B)

    np.savetxt('b05611046_f1.txt', f1)
    np.savetxt('b05611046_f3.txt', f3)

    # plot_wave(np.loadtxt('./ex/s1.txt'), 's1.png')

    # plot_wave(f1, 'testf1.png')
    # plot_wave(f3, 'testf3.png')

    plot_ak(a, 'b05611046_freq.png')

