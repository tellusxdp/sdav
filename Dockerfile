FROM jupyter/datascience-notebook
RUN pip install jupyter_kernel_gateway
COPY ./docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

