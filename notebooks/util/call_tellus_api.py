#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from skimage import io
import os
import numpy as np
URL_DOMAIN="https://gisapi.opf-dev.jp/"

def get_image_using_tellus_api(x, y, z, img_type="osm"):

    if img_type.startswith("band"):
        img_type = "av2ori/" + img_type

    url = "{}/{}/{}/{}/{}.png".format(URL_DOMAIN, img_type, z, x, y)
    try:
        img = io.imread(url)
        return img.astype('int32')
    except:
        print("ERROR: Image not found")
        sys.exit(1)


def get_local_sar_image():
    path_to_fuji_trim_sep = "data/mtfuji_sep.png"
    path_to_fuji_trim_dec = "data/mtfuji_dec.png"

    if os.path.exists(path_to_fuji_trim_sep) and os.path.exists(path_to_fuji_trim_dec):
        # ローカルにトリミング済みデータがある場合はそれを読み込んで利用
        img_fuji_sep = io.imread(path_to_fuji_trim_sep).astype(int)
        img_fuji_dec = io.imread(path_to_fuji_trim_dec).astype(int)

    elif os.path.exists("../" + path_to_fuji_trim_sep) and os.path.exists("../" + path_to_fuji_trim_dec):
        img_fuji_sep = io.imread("../" + path_to_fuji_trim_sep).astype(int)
        img_fuji_dec = io.imread("../" + path_to_fuji_trim_dec).astype(int)

    else:
        #ない場合はtif形式のSAR画像（1.5GB*2）を読み込み、トリミング

        # SAR画像（tif形式）の読み込み  #重すぎてエラーになることあり
        img_fuji_sep_org = io.imread("/tmp/IMG-HH-ALOS2233612910-180920-UBSR2.1GUD.tif")
        img_fuji_dec_org = io.imread("/tmp/IMG-HH-ALOS2246032910-181213-UBSR2.1GUD.tif")
    
        # 前処理
        # 画像が大きすぎるため、富士山の周辺のみ切り取り
        img_fuji_sep = img_fuji_sep_org[5500:8500,4500:7500,] 
        img_fuji_dec = img_fuji_dec_org[5500:8500,4500:7500,]
    
        # 0 ~ 255にスケール
        img_fuji_sep = np.clip( (img_fuji_sep) / 80 , 0, 255).astype(int)
        img_fuji_dec = np.clip( (img_fuji_dec) / 80 , 0, 255).astype(int)    

    return img_fuji_sep, img_fuji_dec


if __name__ == '__main__':
    pass

