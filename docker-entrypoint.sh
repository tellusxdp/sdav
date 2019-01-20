#!/bin/sh
tini -g -- start-notebook.sh
sleep 10
#jupyter kernelgateway --KernelGatewayApp.api='kernel_gateway.notebook_http' --KernelGatewayApp.seed_uri='./SampleAPI.ipynb'

