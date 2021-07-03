
from numpy import asarray
from PIL import Image
import numpy as np


def fancy_pca(image_path):
    im = Image.open(r'C:\Users\dell\Desktop\girl.jpg') #load image.jpg
    i_a = asarray(im) #convert image to array

    i_a = i_a / 255.0

    img_rs = i_a.reshape(-1, 3)

    img_centered = img_rs - np.mean(img_rs, axis=0)

    img_cov = np.cov(img_centered, rowvar=False)

    eig_vals, eig_vecs = np.linalg.eigh(img_cov)

    sort_perm = eig_vals[::-1].argsort()
    eig_vals[::-1].sort()
    eig_vecs = eig_vecs[:, sort_perm]
    print(eig_vecs)

    m1 = np.column_stack((eig_vecs))
    print(m1)

    m2 = np.zeros((3, 1))
    alpha = np.random.normal(0, 0.1)

    m2[:, 0] = alpha * eig_vals[:]
    add_vect = np.matrix(m1) * np.matrix(m2)

    for idx in range(3):   # RGB
        i_a[..., idx] += add_vect[idx]

    orig_img = np.clip(i_a, 0.0, 255.0)
    orig_img = orig_img.astype(np.uint8)

    final_img = Image.fromarray(orig_img)

    return final_img


img = fancy_pca(r'C:\Users\dell\Desktop\girl.jpg')
print(type(img))



