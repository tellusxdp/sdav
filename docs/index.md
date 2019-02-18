# 雪質解析API

>OS: Ubuntu 18.04  
>python: 3.6  


## API概要

衛星画像を利用することで、スキー場の雪質を解析・監視するためのAPIを作成

### 背景
* 衛星画像のAPIが身近になってきた
* いい雪でスキー・スノボーがしたい

### スコープ

* tellusがAPIで提供する衛星データを利用することで以下を検証
    * 雪が積もっているかどうかの判定
    * 雪質を色で可視化
* 解析結果をもとに雪質判定APIを作成

---
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

---

## デプロイ方法

[README.md](https://github.com/tellusxdp/sdav) を参照

---

## API情報

| Name | 内容 | エンドポイント | 例| 出力形式|
|:--|:--|:--|:--|:--|
| OSM Image| tellus APIのOSM画像をそのまま出力 | https://sdav.app.tellusxdp.com/cli/img/osm/{z}/{x}/{y} | https://sdav.app.tellusxdp.com/cli/img/osm/13/7252/3234 <br>localの場合:<br>   http://localhost:8889/img/osm/13/7252/3234  | html |
| NDSI Image| NDSIを計算した結果を出力 | https://sdav.app.tellusxdp.com/cli/ndsi_img/{z}/{x}/{y} | https://sdav.app.tellusxdp.com/cli/ndsi_img/13/7252/3234   <br>localの場合:<br>   http://localhost:8889/ndsi_img/13/7252/3234 | html |
| SAR analysis Image| 2枚のSAR画像を比較して解析した結果を出力 | https://sdav.app.tellusxdp.com/cli/sar_analysis_img | https://sdav.app.tellusxdp.com/cli/sar_analysis_img   <br>localの場合:<br>   http://localhost:8889/sar_analysis_img | html |


---

---

# 分析内容

## 1.光学画像の基礎分析（[notebook](https://github.com/tellusxdp/sdav/blob/master/notebooks/analysis/%E5%85%89%E5%AD%A6%E7%94%BB%E5%83%8F%E3%81%AE%E5%9F%BA%E7%A4%8E%E5%88%86%E6%9E%90.ipynb)）

### 概要
衛星画像を取得できるtellusAPIの挙動を確認するとともに、データの読み込み・notebook上での画像の確認・変換処理・可視化を行う。またその中で、富士山の雪を直感的に識別できるか調査。

### 利用データ
* 光学画像（tellusAPI）
	* band1（青）
	* band2（緑）
	* band3（赤）
	* band4（近赤外線）

###  利用技術
* RGB画像への変換
	* 複数band帯からtrue画像作成
* YIQ画像への変換
* HSV画像への変換

---

## 2.光学画像を用いたNDSI分析（[notebook](https://github.com/tellusxdp/sdav/blob/master/notebooks/analysis/%E5%85%89%E5%AD%A6%E7%94%BB%E5%83%8F%E3%82%92%E4%BD%BF%E3%81%84NDSI%E3%82%92%E5%88%86%E6%9E%90.ipynb)）

### 概要
光学画像の複数bandを組み合わせることで雪かどうかを判定するためのNDSI（Normalized Difference Snow Index）を作成する。また、明度によるフィルタリングと合わせ、雪質判定機を作成する。

### 利用データ
* 光学画像（tellusAPI）
	* band1（青）
	* band2（緑）
	* band3（赤）
	* band4（近赤外線） 
	
### 利用技術
* NDSI変換
* フィルタリング（閾値設定）

---

## 3.SAR画像の基礎分析（[notebook](https://github.com/tellusxdp/sdav/blob/master/notebooks/analysis/SAR%E7%94%BB%E5%83%8F%E3%81%AE%E5%9F%BA%E7%A4%8E%E5%88%86%E6%9E%90.ipynb)）

### 概要
SAR画像をtellusAPIから取得し、データの確認を行う。また、9月と12月に取得された2種類の富士山のSAR画像を利用することで、そのデータの違いから雪の判定を行う。

### 利用データ
* SARデータ（tellusAPI）

### 利用技術
* フィルタリング（平滑化）


---
# サービスへのリンク

## tellusとは？
[https://www.tellusxdp.com/](https://www.tellusxdp.com/)
