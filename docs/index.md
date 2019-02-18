# 雪質解析API

>OS: Ubuntu 18.04  
>python: 3.6  


## API概要

衛星画像を利用することで、スキー場の雪質を解析・監視するためのAPIを作成

### 背景
* 衛星画像のAPIが身近になってきた
* いい雪でスキー・スノボーがしたい

### スコープ

1. tellusがAPIで提供する衛星データを利用することで以下を検証
    * 雪が積もっているかどうかの判定
    * 雪質を色で可視化
2. 解析結果をもとに雪質判定APIを作成


## API構成

| NAME | 役割 | 技術要素など |
|:--|:--|:--|
| sdav-proxy| プロキシサーバー | nginx |
| sdav-gateway| APIサーバ | kernel gateway |
| sdav-jupyter| 分析環境・APIのコード | jupyter notebook |


### 依存ライブラリ

* Docker 
    * jupyter/datascience-notebook
        * skimage
        * numpy
    * jupyter kernel gateway
    * nginx

詳細は[.docker](https://github.com/tellusxdp/sdav/tree/master/.docker)を参照。

## デプロイ方法

[README.md](https://github.com/tellusxdp/sdav) 参照


## API情報

| Name | 内容 | エンドポイント | API例| 出力形式|
|:--|:--|:--|:--|:--|
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


## サービスへのリンク


### tellusとは？
[https://www.tellusxdp.com/](https://www.tellusxdp.com/)
