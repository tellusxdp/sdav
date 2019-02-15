FROM jupyter/datascience-notebook
RUN pip install jupyter_kernel_gateway

ENTRYPOINT jupyter kernelgateway --KernelGatewayApp.port=8889 --KernelGatewayApp.api='kernel_gateway.notebook_http' --KernelGatewayApp.ip='0.0.0.0' --KernelGatewayApp.seed_uri='get_image_api.ipynb'
