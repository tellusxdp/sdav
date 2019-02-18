# tellus-sdav

![mtfuji_ndsi](https://user-images.githubusercontent.com/8220075/52929715-e6aa4c80-3388-11e9-887b-127ba1dca1dd.png)

> OS: Ubuntu 18.04
> python 3.6

## Overview
tellus-sdav is a api to analyze snow quality using satellite image.

[https://tellusxdp.github.io/sdav/](https://tellusxdp.github.io/sdav/)

## install
- docker-compose
- docker

## deploy

### local

```
cd .deploy
sh local.sh
```

### production
```
cd .deploy
sh production.sh
```


## try
```
docker exec -it sdav-gateway bash
curl -i http://localhost:8889/img/osm/13/7248/3226
curl -i http://localhost:8889/ndsi_img/13/7252/3234
curl -i http://localhost:8889/sar_analysis_img
```


## api

Please access the following URL.

### local
```
 http://localhost:8889/img/osm/13/7252/3234
http://localhost:8889/ndsi_img/13/7252/3234
http://localhost:8889/sar_analysis_img
```

### production

```
https://sdav.app.tellusxdp.com/cli/img/osm/13/7252/3234
https://sdav.app.tellusxdp.com/cli/ndsi_img/13/7252/3234
https://sdav.app.tellusxdp.com/cli/sar_analysis_img
```


## jupyter notebook

### local
```
http://localhost:8888
```

### production
```
https://sdav.app.tellusxdp.com
```

## reference
* [https://docs.docker.com/](https://docs.docker.com/)
* [https://hub.docker.com/r/jupyter/datascience-notebook/](https://hub.docker.com/r/jupyter/datascience-notebook/) 
* [https://github.com/jupyter/kernel_gateway/blob/master/docs/source/config-options.md
](https://github.com/jupyter/kernel_gateway/blob/master/docs/source/config-options.md)