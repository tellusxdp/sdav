ls
jupyter kernelgateway --KernelGatewayApp.api='kernel_gateway.notebook_http' --KernelGatewayApp.seed_uri='./work/SimpleAPI.ipynb'
jupyter kernelgateway --KernelGatewayApp.api='kernel_gateway.notebook_http' --KernelGatewayApp.seed_uri='SimpleAPI.ipynb'
pip install jupyter_kernel_gateway
jupyter kernelgateway --KernelGatewayApp.api='kernel_gateway.notebook_http' --KernelGatewayApp.seed_uri='SimpleAPI.ipynb'
ls
jupyter kernelgateway --KernelGatewayApp.api='kernel_gateway.notebook_http' --KernelGatewayApp.seed_uri='SampleAPI.ipynb'
jupyter kernelgateway --KernelGatewayApp.api='kernel_gateway.notebook_http' --KernelGatewayApp.seed_uri='SampleAPI.ipynb' &
curl http://localhost:8889/hgoe
curl http://localhost:8889/ons/hgoe
ps aux
curl http://localhost:8889/ons/hgoe
exit
