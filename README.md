# Satellite Data Analysis and Visualization web server (SDAV)

![mtfuji_ndsi](https://user-images.githubusercontent.com/8220075/52929715-e6aa4c80-3388-11e9-887b-127ba1dca1dd.png)

想定環境
> OS: Ubuntu 18.04 (ホスト)
> Python 3.6 (コンテナ内)


## 概要
SDAVはTellusのデータをJupyter Notebookで分析し、解析結果をAPI化するサンプルプロジェクトです。
参考実装として雪質の解析とそのAPI化を行っています。

**Tellus Platformでの動作を想定しているため、それ以外の環境ではTellusAPIの利用に失敗します**

[開発者向けドキュメントはこちら](https://tellusxdp.github.io/sdav/)


## 依存先 (ホスト)
- docker
- docker-compose


## 起動
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

詳細は各Notebookを参照してください
* [分析](https://github.com/tellusxdp/sdav/tree/master/notebooks/analysis)
* [API](https://github.com/tellusxdp/sdav/blob/master/notebooks/api/get_image_api.ipynb)


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
  * [@motionweekender](https://www.instagram.com/motionweekender/)
  * [@revenue-hack](https://github.com/revenue-hack)

