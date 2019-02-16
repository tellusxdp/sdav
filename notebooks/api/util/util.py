#!/usr/bin/env python
# -*- coding: utf-8 -*-

from skimage import io
import io as bytes_io
import base64

def make_base64_image(img_np):
    """numpyの画像データをbase64に変換"""    

    #空のインスタンスを作り一時保存
    img_bytes = bytes_io.BytesIO()
    io.imsave(img_bytes, img_np)

    #型変換
    img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')

    return img_base64


if __name__ == '__main__':
    pass
