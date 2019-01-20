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
jupyter kernelgateway --KernelGatewayApp.api='kernel_gateway.notebook_http' --KernelGatewayApp.seed_uri='SampleAPI.ipynb' &
curl http://localhost:8889/ons/hoge
```

