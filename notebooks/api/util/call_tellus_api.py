#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from skimage import io

URL_DOMAIN="https://img.opf-dev.jp"
img_types=["osm",
           "true",
           "natural",
           "av2ori/band1",
           "av2ori/band2",
           "av2ori/band3",
           "av2ori/band4"]


def get_image_using_tellus_api(x, y, z, img_type="osm"):
    url = "{}/{}/{}/{}/{}.png".format(URL_DOMAIN, img_type, z, x, y)
    try:
        img = io.imread(url)
        return img
    except:
        print("ERROR: Image not found")
        return None


def get_images_using_tellus_api(x, y, z, img_types=img_types):
    urls = ["{}/{}/{}/{}/{}.png".format(URL_DOMAIN, img_type, z, x, y) for img_type in img_types]
    try:
        imgs = np.array([io.imread(url) for url in urls])
        return imgs
    except:
        print("ERROR: Image not found")
        return None


if __name__ == '__main__':
    pass
