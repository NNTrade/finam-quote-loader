# !/bin/bash 
docker stop finam-quote-loader-srv
docker rm finam-quote-loader-srv
docker run -d -l finam-quote-loader-service -p 7001:5000 --name finam-quote-loader-srv --label stereotype=srv --restart=always finam-quote-loader:v3.7