FROM jupyter/datascience-notebook
RUN pip install jupyter_kernel_gateway

# tellusAPIからtif画像を取ってきたい場合はコメントを外す。ただし重すぎるため30分くらいかかる可能性あり
# RUN wget -q http://sample-data.app.tellusxdp.com/1/10/data -O /tmp/IMG-HH-ALOS2233612910-180920-UBSR2.1GUD.tif
# RUN wget -q http://sample-data.app.tellusxdp.com/1/14/data -O /tmp/IMG-HH-ALOS2246032910-181213-UBSR2.1GUD.tif

ENTRYPOINT jupyter kernelgateway --KernelGatewayApp.port=8889 --KernelGatewayApp.api='kernel_gateway.notebook_http' --KernelGatewayApp.ip='0.0.0.0' --KernelGatewayApp.seed_uri='api/get_image_api.ipynb'
