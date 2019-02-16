#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from skimage import io
import sys
URL_DOMAIN="https://img.opf-dev.jp"

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
        return None


if __name__ == '__main__':
    pass
