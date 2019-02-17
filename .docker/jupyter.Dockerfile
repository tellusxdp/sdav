FROM jupyter/datascience-notebook
COPY .docker/generate_sha1_password.py /

# RUN wget -q http://sample-data.app.tellusxdp.com/1/10/data -O /tmp/IMG-HH-ALOS2233612910-180920-UBSR2.1GUD.tif
# RUN wget -q http://sample-data.app.tellusxdp.com/1/14/data -O /tmp/IMG-HH-ALOS2246032910-181213-UBSR2.1GUD.tif

ENTRYPOINT JUPYTER_PASSWORD_HASH=$(echo ${JUPYTER_PASSWORD} | python /generate_sha1_password.py| cat) && \
    /bin/bash start-notebook.sh --NotebookApp.ip='0.0.0.0' --NotebookApp.password=${JUPYTER_PASSWORD_HASH}
