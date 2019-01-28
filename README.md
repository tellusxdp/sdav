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
jupyter kernelgateway --KernelGatewayApp.port=8889 --KernelGatewayApp.api='kernel_gateway.notebook_http' --KernelGatewayApp.ip='0.0.0.0' --KernelGatewayApp.seed_uri='get_image_api.ipynb'
curl -i http://localhost:8889/ndsi_img/13/7248/3226
```

## reference
- https://github.com/jupyter/kernel_gateway/blob/master/docs/source/config-options.md

