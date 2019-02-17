# tellus-sdav

## install
- docker-compose
- docker

## create local env
```
cd .deploy
sh local.sh
```

## try
response json
```
docker exec -it kernel_gateway bash
curl -i http://localhost:8889/img/osm/13/7248/3226
curl -i http://localhost:8889/ndsi_img/13/7252/3234
curl -i http://localhost:8889/sar_analysis_img
```

## api
```
http://sdav.app.tellusxdp.com/cli/img/osm/13/7252/3234
http://sdav.app.tellusxdp.com/cli/ndsi_img/13/7252/3234
http://sdav.app.tellusxdp.com/cli/sar_analysis_img
```

## jupyter notebook
```
http://sdav.app.tellusxdp.com
```

## reference
- https://github.com/jupyter/kernel_gateway/blob/master/docs/source/config-options.md
