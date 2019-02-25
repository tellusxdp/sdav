# Satellite Data Analysis and Visualization web server (SDAV)

<p align="center">
  <a href="https://tellusxdp.github.io/sdav">
    <img src="https://user-images.githubusercontent.com/8220075/52929715-e6aa4c80-3388-11e9-887b-127ba1dca1dd.png">
  </a>
</p>


想定環境

> ホストにDocker/DockerComposeが導入されていること


## 概要
[Tellus](https://www.tellusxdp.com) を利用したサンプルプロジェクトです。

Jupyter Notebookをベースに、Tellusから取得できる衛星画像を利用した様々な分析・可視化をし、結果をAPIするWebサーバです。

参考実装として、雪質の分析・可視化を行うAPIが実装されています。

**Tellus Platformでの動作を想定しているため、それ以外の環境ではTellusAPIの利用に失敗する場合があります**

[開発者向けドキュメントはこちら](https://tellusxdp.github.io/sdav/)


## 依存先 (ホスト)
- Docker
- DockerCompose


## 依存先（コンテナ内）
- Python 3.6+

## 実行
```
cd .deploy
sh local.sh
```


## API例
```
# OpenStreamMapの取得
http://localhost:8080/img/osm/13/7252/3234

# NDSIの結果の取得
http://localhost:8080/ndsi_img/13/7252/3234

# SARから得られた結果の取得
http://localhost:8080/sar_analysis_img
```

詳細は開発者ドキュメントや各Notebookを参照してください
* [開発者向けドキュメント](https://tellusxdp.github.io/sdav)
* [分析Notebook](https://github.com/tellusxdp/sdav/tree/master/notebooks/analysis)
* [API Notebook](https://github.com/tellusxdp/sdav/blob/master/notebooks/api/get_image_api.ipynb)


## Jupyter Notebookの利用
```
http://localhost:8888
```

(初期パスワード: `password`)


## 参考
* [https://docs.docker.com/](https://docs.docker.com/)
* [https://hub.docker.com/r/jupyter/datascience-notebook/](https://hub.docker.com/r/jupyter/datascience-notebook/)
* [https://github.com/jupyter/kernel_gateway/blob/master/docs/source/config-options.md
](https://github.com/jupyter/kernel_gateway/blob/master/docs/source/config-options.md)


## Collaborators
* 株式会社プラハ
  * [@shin-kanouchi](https://github.com/shin-kanouchi)
  * [@revenue-hack](https://github.com/revenue-hack)


-----


<p align="center">
  <a href="https://www.tellusxdp.com">
    <img src="https://user-images.githubusercontent.com/3175456/53102763-b53fa580-356f-11e9-94d5-a934d220c6fa.png">
  </a>
</p>

