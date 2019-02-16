FROM jupyter/datascience-notebook
COPY .docker/generate_sha1_password.py /

ENTRYPOINT JUPYTER_PASSWORD_HASH=$(echo ${JUPYTER_PASSWORD} | python /generate_sha1_password.py| cat) \
    && /bin/bash start-notebook.sh --NotebookApp.password=${JUPYTER_PASSWORD_HASH}
