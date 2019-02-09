# tellus-sdav

## install
- docker-compose
- docker

## create local env
```
docker-compose up -d
```

## try
response json
```
docker exec -it kernel_gateway bash
curl -i http://localhost:8889/img/osm/13/7248/3226
curl -i http://localhost:8889/ndsi_img/13/7252/3234
```

## api
```
http://sdav.app.tellusxdp.com/img/osm/13/7252/3234
http://sdav.app.tellusxdp.com/ndsi_img/13/7252/3234
```

## reference
- https://github.com/jupyter/kernel_gateway/blob/master/docs/source/config-options.md

