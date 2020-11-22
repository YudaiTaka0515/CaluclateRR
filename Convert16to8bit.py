import numpy as np


def Convert16to8bit(images_u16):
    maxV, minV = np.amax(images_u16), np.amin(images_u16)
    # maxV, minV = (60000, 50000)
    # print(maxV, minV)
    alpha = 255.0 / (maxV - minV)
    images_u8 = np.add(images_u16, -minV)
    images_u8 = images_u8 * alpha
    images_u8 = images_u8.astype(np.uint8)
    return images_u8
