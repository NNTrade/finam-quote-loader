# !/bin/bash 
docker run -d -l finam-quote-loader-service -p 7001:5000 --name finam-quote-loader finam-quote-loader:v3.0