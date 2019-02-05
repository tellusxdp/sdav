FROM jupyter/datascience-notebook
RUN pip install jupyter_kernel_gateway

COPY ./generate_sha1_password.py /
COPY ./docker-entrypoint.sh /

ENTRYPOINT JUPYTER_PASSWORD_HASH=$(echo ${JUPYTER_PASSWORD} | python /generate_sha1_password.py| cat) \
    && /bin/bash start-notebook.sh --NotebookApp.password=${JUPYTER_PASSWORD_HASH}

#ENTRYPOINT ["/docker-entrypoint.sh"]
