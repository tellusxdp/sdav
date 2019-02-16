#!/usr/bin/env python
# -*- coding: utf-8 -*-

img_types=["osm",
           "true",
           "natural",
           "band1",
           "band2",
           "band3",
           "band4"]

def input_validation_check(x, y, z, img_type="osm"):
    """バリデーションチェック"""
    
    if not img_type or not x or not y or not z:
        print("ERROR: Input format error. please input `/img/[img_type]/[z]/[x]/[y]`")
        print("ex. http://localhost:8822/img/osm/13/7252/3234")
        return False
    
    elif img_type not in img_types:
        print("ERROR: img_type format error. please input next format`/img/[img_type]/[z]/[x]/[y]`")
        print("img_types only allows [{}]".format(", ".join(img_types)))
        return False
    
    elif not (x+y+z).isdecimal():
        print("ERROR: x/y/z format error")
        print("x/y/z only allows  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
        return False

    else:
        return True


if __name__ == '__main__':
    pass
