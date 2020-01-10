import numpy as np


def svd_compress(imArr, K=50):
    """Compress image array using SVD decomposition.
    Arg:
        imArr: numpy array with shape (height, width, 3).
    Return:
        Compressed imArr: numpy array.
    """
    imArr_compressed = np.zeros(imArr.shape)
    # For each channel
    for ch in range(3):
        # --------------------
        # TODO: 
        #     Compress the image array using SVD decomposition
        # hint:
        #     1. numpy.linalg.svd
        #     2. numpy.diag
        #     3. numpy.dot
        #
        # Your code here
        # imArr_compressed = ??
        # 
        # --------------------
        
        u, s, vh = np.linalg.svd(imArr[:, :, ch], full_matrices = False)
        # print(u.shape, s.shape, vh.shape)
        imArr_compressed[:, :, ch] = np.dot(np.dot(u[:, :K], s[K - 1]), vh[:K, :])

        # Make imArr_compressed range from 0 to 255
        imArr_compressed[:, :, ch] -= imArr_compressed[:, :, ch].min()
        imArr_compressed[:, :, ch] /= imArr_compressed[:, :, ch].max()
        imArr_compressed[:, :, ch] *= 255
        # Return uint8 because save_image needs input of type uint8
    return imArr_compressed.astype(np.uint8)
