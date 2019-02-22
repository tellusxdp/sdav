# 衛星データ分析可視化サーバ（参考実装: 雪質解析）

想定環境
> ホストにDocker/DockerComposeが導入されていること

> Python 3.6 (コンテナ内)


## 目次
* 概要
* アプリ構成
* デプロイ方法
* API情報
  * サンプルAPI
    * URI
    * Parameter
    * API利用例
  * 雪質解析API
    * URI
    * Parameter
    * API利用例
* 雪質解析詳細
  * TellusAPIの紹介
  * 光学画像の基礎分析
  * 光学画像を用いたNDSI分析
  * SAR画像の基礎分析
* リンク


## 概要
[Tellus](https://www.tellusxdp.com) を利用したサンプルプロジェクトです。

Jupyter Notebookをベースに、Tellusから取得できる衛星画像を利用した様々な分析・可視化をし、結果をAPIするWebサーバです。

参考実装として、[雪質の分析・可視化を行うAPI](#雪質解析API)が実装されています。[解析の詳細はこちら](#雪質解析詳細)。

**Tellus Platformでの動作を想定しているため、それ以外の環境ではTellusAPIの利用に失敗する場合があります。また、[データポリシー](https://www.tellusxdp.com/ja/dev/data) にご注意ください。**


## アプリ構成

| NAME | 役割 | 技術要素など |
|:--|:--|:--|
| sdav-proxy | プロキシサーバー | nginx |
| sdav-gateway | APIサーバ | kernel gateway |
| sdav-jupyter | 分析環境・APIのコード | jupyter notebook |

### Docker Image
* [jupyter/datascience-notebook](https://hub.docker.com/r/jupyter/datascience-notebook)
  * [Jupyter Kernel Gateway](https://github.com/jupyter/kernel_gateway)
* [nginx](https://hub.docker.com/_/nginx)

詳細は[.docker](https://github.com/tellusxdp/sdav/tree/master/.docker)を参照してください。


## デプロイ準備例 (Ubuntu 18.04)
DockerとDockerComposeをインストール

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


## 実行
``` bash
git clone https://github.com/tellusxdp/sdav.git
cd satellite-puzzle/.deploy
sudo sh local.sh
```


## 実装済みAPI一覧
### サンプルAPI
#### 背景
* サンプル

#### API
##### URI

| name | description | URI |output format|
|:--|:--|:--|:--|
| original image| Tellus APIの画像をそのまま出力 | local:<br> http://localhost:8889/img/{kind}/{z}/{x}/{y} <br>production:<br> https://0.0.0.0/api/img/{kind}/{z}/{x}/{y} | html |

##### Parameter

|params|description|sample|
|:--|:--|:--|
|kind|画像の種類|osm, band1, band2, band3, band4|
|z|ズーム値 (大きいほどズーム)|13|
|x|地図のx軸の値|7252|
|y|地図のy軸の値|3234|

#### API利用例
`http://localhost:8889/img/osm/13/7252/3234`
![default](https://user-images.githubusercontent.com/8220075/52954330-3ca0e380-33cd-11e9-955b-b5ac4ab25f85.png)


### 雪質解析API
#### 背景
* 衛星画像をAPI経由で利用できる
* いい雪でスキー・スノボーがしたい

#### スコープ
* TellusがAPIで提供する衛星データを利用することで以下を検証
    * 雪が積もっているかどうかの判定
    * 雪質をグラデーションで可視化
* 解析結果をもとに雪質判定をAPI化

#### API
##### URI

| name | description | URI |output format|
|:--|:--|:--|:--|
| NDSI image| NDSIを計算した結果を出力 | local: <br> http://localhost:8889/ndsi_img/{z}/{x}/{y} <br>production:<br> https://0.0.0.0/api/ndsi_img/{z}/{x}/{y} | html |
| SAR analysis image| 2枚のSAR画像を比較して解析した結果を出力 | local:<br> http://localhost:8889/sar_analysis_img <br>production:<br> https://0.0.0.0/api/sar_analysis_img | html |

##### Parameter

|params|description|sample|
|:--|:--|:--|
|kind|画像の種類|osm, band1, band2, band3, band4|
|z|ズーム値 (大きいほどズーム)|13|
|x|地図のx軸の値|7252|
|y|地図のy軸の値|3234|


#### API利用例
`http://localhost:8889/ndsi_img/13/7252/3234`
![default](https://user-images.githubusercontent.com/8220075/52929715-e6aa4c80-3388-11e9-887b-127ba1dca1dd.png)

`http://localhost:8889/sar_analysis_img`
![default](https://user-images.githubusercontent.com/8220075/52954420-825dac00-33cd-11e9-83c7-a90f105f809c.png)


## リンク
* [Tellus](https://www.tellusxdp.com/)
* [Jupyter NotebookでTellusを使ってみた〜雪質解析してみた〜](https://sorabatake.jp/3531/)


---


## 雪質解析詳細
### 0. 利用データとTellus API
### 概要
今回のデータ解析で扱う [Tellus API](https://www.tellusxdp.com/ja/dev/api) ではいくつかの衛星データが利用可能です。今回は[AVNIR-2](https://www.eorc.jaxa.jp/ALOS/about/javnir2.htm)が受信する光学画像と[PALSAR-2](https://www.eorc.jaxa.jp/ALOS-2/about/jpalsar2.htm)が受信するSAR画像を利用します。

**一部正式リリース前のサンプルAPIが含まれます。**

### 光学画像とは
太陽の出す可視・赤外線を元に、地上で反射した光を観測するセンサで捉えたデータを画像化したものです。各波長での反射の強さは水・土壌・植物などによって異なるため、複数波長を組み合わせることで物質の認識が可能になります。

Tellus APIでは、AVNIR-2の4バンドが利用可能です。

|band|波長|色|
|:--|:--|:--|
|band1|0.42~0.50μm|青|
|band2|0.52~0.60μm|緑|
|band3|0.61~0.69μm|赤|
|band4|0.76~0.89μm|近赤外線（不可視光線）|

### SAR画像とは
SAR (Synthetic Aperture Radar; 合成開口レーダー) はマイクロ波を地表面に斜めに照射し、地表面からの後方散乱波を受信したものです。SARのマイクロ波は雲を通過し観測に太陽光を必要としないため、天候に左右されず、夜間でも観測が可能という特徴があります。

|band|周波数|
|:--|:--|
|L band | 1.2GHz帯（波長 23cm） |

### 光学画像とSAR画像の比較

||光学画像(AVNIR-2)|SAR画像(PALSAR-2)|備考|
|:--|:--|:--|:--|
|分解能|10m|3~100m|SARの高分解能モードでは3mまで分解可能|
|太陽光|必要|不要|光学画像は雲の影響を受けるが、SAR画像は受けにくい|
|入射角|0~44度|8~70度|SARは斜めに飛ばした電波の跳ね返りを観測するため、入射角が必要|
|観測幅|70km|50km~490km|SARの広域観測モードは広範囲を一度に観測可能|

## 1. 光学画像の基礎分析1（雪判定）（[Notebook](https://github.com/tellusxdp/sdav/blob/master/notebooks/analysis/%E5%85%89%E5%AD%A6%E7%94%BB%E5%83%8F%E3%81%AE%E5%9F%BA%E7%A4%8E%E5%88%86%E6%9E%901%EF%BC%88%E9%9B%AA%E5%88%A4%E5%AE%9A%EF%BC%89.ipynb)）

### 概要
衛星画像を取得できるTellus APIの挙動を確認するとともに、データの読み込み・Notebook上での画像の確認・変換処理・可視化といった基本的操作を行います。またその中で、富士山の雪を直感的に識別できるか調査します。

### 利用データ
* AVNIR-2光学画像（Tellus API）
	* band1（青）
	* band2（緑）
	* band3（赤）
	* band4（近赤外線）

### 技術要素
* RGB画像への変換
	* 複数band帯からtrue画像作成
* YIQ画像への変換
* HSV画像への変換

### 分析サマリ
1.複数bandを組み合わせてtrue画像作成

![true](https://user-images.githubusercontent.com/8220075/52991537-6bac6900-3450-11e9-9828-fb9d3fb1efbf.png)

2.明度の画像抽出

![hsv_no_v](https://user-images.githubusercontent.com/8220075/52991551-79fa8500-3450-11e9-8410-3ab6226561d0.png)

3.閾値でフィルタリングし雪かどうかを判定

![filter](https://user-images.githubusercontent.com/8220075/52991558-8383ed00-3450-11e9-8032-211c208257e5.png)

### 考察
直感的な色や明るさでフィルタリングの作成を行いました。
雪と土や森は色が明らかに違うため識別が容易かと思われましたが、陰になっている部分が想像以上に暗く、判別が難しいことが明らかになりました。また、道などのコンクリート部分も白く抽出されてしまうことが分かりました。

今回は富士山を対象に行いましたが、スキー場であれば基本的に同一方向を向いており光の当たり具合も似ていると思われるため、スキー場毎に閾値を設定すればスキー場毎の雪判定はできそうです。


## 2. 光学画像の基礎分析2（雪質分析）（[Notebook](https://github.com/tellusxdp/sdav/blob/master/notebooks/analysis/%E5%85%89%E5%AD%A6%E7%94%BB%E5%83%8F%E3%81%AE%E5%9F%BA%E7%A4%8E%E5%88%86%E6%9E%902%EF%BC%88%E9%9B%AA%E8%B3%AA%E5%88%86%E6%9E%90%EF%BC%89.ipynb)）

### 概要
光学画像の複数bandを組み合わせることで雪かどうかを判定するためのNDSI（Normalized Difference Snow Index）を作成します。ただし、AVNIR-2では得られないデータが必要となるため、一部代替手段を模索します。また、明度による雪判定と合わせ、雪質判定機を作成します。

### 利用データ
* 光学画像（Tellus API）
	* band1（青）
	* band2（緑）
	* band3（赤）
	* band4（近赤外線）

### 利用技術
* NDSI変換
* マスキング

### 分析サマリ
1. NDSIを作成

![ndsi](https://user-images.githubusercontent.com/8220075/52991582-9d253480-3450-11e9-8978-165e44bbdb03.png)

2. 前のNotebookの雪判定をマスクとして作成

![filter](https://user-images.githubusercontent.com/8220075/52991558-8383ed00-3450-11e9-8032-211c208257e5.png)

3. NDSIの結果を雪判定マスクでtrue画像を重ねる

![default](https://user-images.githubusercontent.com/8220075/52929715-e6aa4c80-3388-11e9-887b-127ba1dca1dd.png)

### 考察
光学画像の不可視光線を利用することで、NDSIを作成しました。本来は中間赤外線が必要だが、AVNIR-2では提供されていないため、近赤外線で代用しました。
赤外線を利用することで、色では捉えられない情報（植生の深さや水の有無など）を認識可能となり、今回はこれを使い雪質の判定を試みました。

結果として、近赤外線を利用したため植生に敏感に反応するものとなった（1の赤い部分）。雪かどうかでも多少色が分かれているものの、雪部分と岩部分の境界が微妙となっており、明度による分類よりも精度が落ちてしまいました。

そこで、明度で雪かどうかの判定をするマスク作成したのち、雪として判定した部分に対してNDSIを計算して色付けしたものを最終的なアウトプットとしました。色の濃淡は出ましたが、雪質（ふわふわ、べちょべちょ、カチカチなど）に関しては実際の雪と一致しているか検証する必要が残っています。


## 3. SAR画像の基礎分析（雪判定）（[Notebook](https://github.com/tellusxdp/sdav/blob/master/notebooks/analysis/SAR%E7%94%BB%E5%83%8F%E3%81%AE%E5%9F%BA%E7%A4%8E%E5%88%86%E6%9E%90%EF%BC%88%E9%9B%AA%E5%88%A4%E5%AE%9A%EF%BC%89.ipynb)）

### 概要
SAR画像をTellus APIから取得し、データの確認を行います。また、9月と12月に取得された2種類の富士山のSAR画像を利用することで、そのデータの違いから雪の判定を試みます。

### 利用データ
* SARデータ（Tellus サンプルAPI）

### 利用技術
* 差分
* 平滑化

### 分析サマリ
1. 異なる日時のSAR画像を読み込み（左が9月、右が12月）

![sar](https://user-images.githubusercontent.com/8220075/52991765-73204200-3451-11e9-9cd1-4fe0ee3f0044.png)

2. 2つのSAR画像の差分を抽出

![sar_diff](https://user-images.githubusercontent.com/8220075/52991767-74ea0580-3451-11e9-81f8-a6154d257fde.png)

3. ノイズを取り除き可視化

![default](https://user-images.githubusercontent.com/8220075/52954420-825dac00-33cd-11e9-83c7-a90f105f809c.png)

### 考察
SAR画像は複数偏波（HH, VV, HV, VH）がある場合もあるが、今回は単一の偏波（HH）の提供だったため、偏波の差分の検証は行わず、2つの日時のデータの差分を利用することで、雪の判定を試みました。

夏と冬の同一位置の差分を抽出した結果、ノイズが目立ち判断が難しかったため、ガウシアンフィルタを利用し平滑化することで、差分を見やすく加工しました。

結果として、富士山の中腹部の変化が激しいことが判明しましたが、この変化が雪によるものなのか、草木が枯れたことによるものなのかまでの判断は難しいと言えます。


## 4. 光学画像とSAR画像の両方についての考察
今回の検証において、光学画像とSAR画像にはそれぞれメリット・デメリットがありました。光学画像はのメリットとして、可視光線を含むため直感的な解析を行うことができました。その上で近赤外線なども利用することで、目で見える可視光線以上のアウトプットが可能でした。

一方デメリットとして、雲が雪として判定されてしまう問題がありました。以下は光学画像による富士山の右上部分アウトプットですが、雲も明度が高いため雪として判定され、青くなっていることがわかります。

![ndsi_cloud](https://user-images.githubusercontent.com/8220075/52995375-c9937d80-345d-11e9-80fc-bded70c8d148.png)

一方でSAR画像は太陽光を利用しないため、雲や天候の影響を受けにくく安定したアウトプットを出力可能という利点があります。


## Future Work
光学画像の時系列データが入手できれば分析の幅は広がります。複数の日時のデータを用いて、雪が降った前後の光学画像を比較した分析、雲がある時/ない時の判定を行うことが考えられます。

また、SAR画像では複数偏波（HH, VV, HV, VH）を利用した検証・同一日時の光学画像を確認しながらの検証・光学画像とSAR画像を組み合わせた検証を行うことが考えられます。


## 参考文献
* 開発
    * [https://docs.docker.com/](https://docs.docker.com/)
    * [https://hub.docker.com/r/jupyter/datascience-notebook/](https://hub.docker.com/r/jupyter/datascience-notebook/)
    * [https://jupyter-kernel-gateway.readthedocs.io/en/latest/](https://jupyter-kernel-gateway.readthedocs.io/en/latest/)
    * [https://github.com/jupyter/kernel_gateway/blob/master/docs/source/config-options.md
](https://github.com/jupyter/kernel_gateway/blob/master/docs/source/config-options.md)
* 分析
    * [ALOS-2の概要 - 地球観測研究センター](https://www.eorc.jaxa.jp/ALOS-2/about/joverview.htm)
    * [ALOS-2/PALSAR-2 プロダクトフォーマット説明書](https://www.eorc.jaxa.jp/ALOS-2/doc/fdata/PALSAR-2_xx_Format_CEOS_J_r.pdf)
    * [ALOS-2/PALSAR-2 による災害観測について](https://annex.jsap.or.jp/photonics/kogaku/public/43-02-kaisetsu1.pdf)
    * [Snow Index - NDSI](http://profhorn.meteor.wisc.edu/wxwise/satmet/lesson3/ndsi.html)
    * [Snow cover area and snow water equivalent in upstream area in Aka River](http://soil.en.a.u-tokyo.ac.jp/jsidre/search/PDFs/16cd/manuscript_pdf/%5B5-34(P)%5D.pdf)
