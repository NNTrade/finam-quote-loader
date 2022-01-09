#!bin/bash
docker build -t finam-quote-loader/base-img --ssh default --no-cache -f ./.devcontainer/base/Dockerfile .