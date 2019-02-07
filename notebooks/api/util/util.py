#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from skimage import io
import io as bytes_io
import base64

def make_base64_image(img_np):
    img_bytes = bytes_io.BytesIO() #空のインスタンスを作る
    io.imsave(img_bytes, img_np)
    img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
    return img_base64




if __name__ == '__main__':
    pass
