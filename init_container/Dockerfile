FROM python:3.10-slim

RUN apt update && apt install curl -y
RUN curl https://dl.min.io/client/mc/release/linux-amd64/mc --create-dirs -o $HOME/minio-binaries/mc
RUN chmod +x $HOME/minio-binaries/mc

COPY . .
RUN chmod +x ./docker-entrypoint.sh
ENTRYPOINT ["/bin/bash", "./docker-entrypoint.sh"]