time docker run -v ${PWD}:/opt/es-test/save --rm -m 500M --cpu-period=5000 --cpu-quota=5000 es-test -es 115.29.34.243:9200 -name elastic -password superzsh123 -index bigtable -lines 5000 -pull
