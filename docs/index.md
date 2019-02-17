# 雪質解析API

>OS: Ubuntu 18.04  
>python: 3.6  
>node: 10.15  


## API概要

tellusAPIの光学画像とSAR画像を利用することで、
雪質を調査して雪質画像を返すAPIです。
これでスキーに行く日を決めることができるかも。

## API構成

| NAME | 役割 | 技術要素など |
|:--|:--|:--|
| sdav-proxy| プロキシサーバー | nginx |
| sdav-gateway| APIサーバ | kernel gateway |
| sdav-jupyter| 分析環境・APIのコード | jupyter notebook |


## 依存ライブラリ
* jupyter_kernel_gateway
* jupyter/datascience-notebook
    * skimage
    * numpy

Dockerで構築されているため、詳細は
[jupyter.Dockerfile](https://github.com/tellusxdp/sdav/blob/master/.docker/jupyter.Dockerfile)と[kernel_gateway.Dockerfile](https://github.com/tellusxdp/sdav/blob/master/.docker/kernel_gateway.Dockerfile)を参照。

## デプロイ方法

### ローカルの場合

### サーバの場合

## API情報
| Name | 内容 | API | 例| 出力形式|
|:--|:--|:--|:--|:--|:--|
| OSM Image| tellus APIのOSM画像をそのまま出力 | https://sdav.app.tellusxdp.com/cli/img/osm/{z}/{x}/{y} | https://sdav.app.tellusxdp.com/cli/img/osm/13/7252/3234 <br>localの場合:<br>   http://localhost:8889/img/osm/13/7252/3234  | html |
| NDSI Image| NDSIを計算した結果を出力 | https://sdav.app.tellusxdp.com/cli/ndsi_img/{z}/{x}/{y} | https://sdav.app.tellusxdp.com/cli/ndsi_img/13/7252/3234   <br>localの場合:<br>   http://localhost:8889/ndsi_img/13/7252/3234 | html |
| SAR analysis Image| 2枚のSAR画像を比較して解析した結果を出力 | https://sdav.app.tellusxdp.com/cli/sar_analysis_img | https://sdav.app.tellusxdp.com/cli/sar_analysis_img   <br>localの場合:<br>   http://localhost:8889/sar_analysis_img | html |


## 分析について

### 光学画像の基礎分析

* [notebookはこちら](https://github.com/tellusxdp/sdav/blob/master/notebooks/analysis/%E5%85%89%E5%AD%A6%E7%94%BB%E5%83%8F%E3%81%AE%E5%9F%BA%E7%A4%8E%E5%88%86%E6%9E%90.ipynb)

### 光学画像を用いたNDSI分析

* [notebookはこちら](https://github.com/tellusxdp/sdav/blob/master/notebooks/analysis/%E5%85%89%E5%AD%A6%E7%94%BB%E5%83%8F%E3%82%92%E4%BD%BF%E3%81%84NDSI%E3%82%92%E5%88%86%E6%9E%90.ipynb)

### SAR画像の基礎分析

* [notebookはこちら](https://github.com/tellusxdp/sdav/blob/master/notebooks/analysis/SAR%E7%94%BB%E5%83%8F%E3%81%AE%E5%9F%BA%E7%A4%8E%E5%88%86%E6%9E%90.ipynb)


## サムネ
なんか置く




## サービスへのリンク


### tellusとは？
[https://www.tellusxdp.com/](https://www.tellusxdp.com/)
