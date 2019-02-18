# 雪質解析API

>OS: Ubuntu 18.04  
>python: 3.6  


## 目次
* 概要
* アプリ構成
* デプロイ方法
* API情報
    * URI
    * parameter
    * sample
* 分析
    * 光学画像の基礎分析
    * 光学画像を用いたNDSI分析
    * SAR画像の基礎分析
* サービスへのリンク
    
## 概要

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
## アプリ構成

| NAME | 役割 | 技術要素など |
|:--|:--|:--|
| sdav-proxy| プロキシサーバー | nginx |
| sdav-gateway| APIサーバ | kernel gateway |
| sdav-jupyter| 分析環境・APIのコード | jupyter notebook |


### 依存ライブラリ

* Docker 
    * jupyter/datascience-notebook
    * jupyter kernel gateway
    * nginx

詳細は[.docker](https://github.com/tellusxdp/sdav/tree/master/.docker)を参照。

---

## デプロイ方法

>Docker version 18.09  
>docker-compose version 1.23  

### docker install

まずはdockerをインストール  
以下のシェルを実行

``` bash
#!/bin/bash
sudo apt update
sudo apt install git
sudo apt-get install -y \
        apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable"
sudo apt update
sudo apt-get install -y docker-ce
sudo gpasswd -a $(whoami) docker
sudo chgrp docker /var/run/docker.sock
sudo service docker restart
docker info

sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose -v
```

### local

以下を実行

``` bash
git clone https://github.com/tellusxdp/sdav.git
cd satellite-puzzle/.deploy
sudo sh local.sh
```

### production

wildcard.app.tellusxdp.com.crt, wildcard.app.tellusxdp.com.keyを`/var`配下におく  
※ wildcard.app.tellusxdp.com.crtは中間証明書と合成しておくこと  

その後$HOME配下に以下のシェルスクリプトを置きsudoで実行する

``` bash
#!/bin/bash
if [ -d /var/sdav ] ; then
        rm -rf /var/sdav
fi
cd /var && git clone https://github.com/tellusxdp/sdav.git
cp wildcard.app.tellusxdp.com.crt sdav/.docker
cp wildcard.app.tellusxdp.com.key sdav/.docker
cd /var/sdav/.deploy && sh production.sh
```

---

# API情報

## URI
 
| name | description | URI |output format|
|:--|:--|:--|:--|
| original image| tellus APIの画像をそのまま出力 | production:<br> https://0.0.0.0/cli/img/{kind}/{z}/{x}/{y} <br>local:<br> http://localhost:8889/img/{kind}/{z}/{x}/{y}  | html |
| NDSI image| NDSIを計算した結果を出力 | production:<br> https://0.0.0.0/cli/ndsi_img/{z}/{x}/{y} <br>local: <br> http://localhost:8889/ndsi_img/{z}/{x}/{y} | html |
| SAR analysis image| 2枚のSAR画像を比較して解析した結果を出力 | production:<br> https://0.0.0.0/cli/sar_analysis_img <br>local:<br> http://localhost:8889/sar_analysis_img | html |


## parameter

|params|description|sample|
|:--|:--|:--|
|kind|画像の種類|osm, band1, band2, band3, band4|
|z|ズーム値 (大きいほどズーム)|13|
|x|地図のx軸の値|7252|
|y|地図のy軸の値|3234|


## sample

### local


``` http://localhost:8889/img/osm/13/7252/3234
http://localhost:8889/ndsi_img/13/7252/3234
http://localhost:8889/sar_analysis_img 
```

### production

``` https://sdav.app.tellusxdp.com/cli/img/osm/13/7252/3234
https://sdav.app.tellusxdp.com/cli/ndsi_img/13/7252/3234
https://sdav.app.tellusxdp.com/cli/sar_analysis_img 
```

### sample output
Please access the following URL


`http://localhost:8889/img/osm/13/7252/3234`

![default](https://user-images.githubusercontent.com/8220075/52954330-3ca0e380-33cd-11e9-955b-b5ac4ab25f85.png)



`http://localhost:8889/ndsi_img/13/7252/3234`

![default](https://user-images.githubusercontent.com/8220075/52929715-e6aa4c80-3388-11e9-887b-127ba1dca1dd.png)

`http://localhost:8889/sar_analysis_img`

![default](https://user-images.githubusercontent.com/8220075/52954420-825dac00-33cd-11e9-83c7-a90f105f809c.png)


---

# 分析

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
## サービスへのリンク

### tellusとは？
[https://www.tellusxdp.com/](https://www.tellusxdp.com/)
