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
docker exec -it tellus-jupyter bash
curl -i http://localhost:8889/img/osm/13/7248/3226
curl -i http://localhost:8889/ndsi_img/13/7248/3226
```

## reference
- https://github.com/jupyter/kernel_gateway/blob/master/docs/source/config-options.md

