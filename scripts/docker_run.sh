# !/bin/bash 
docker stop finam-quote-loader
docker rm finam-quote-loader
docker run -d -l finam-quote-loader-service -p 7001:5000 --name finam-quote-loader finam-quote-loader:v3.5