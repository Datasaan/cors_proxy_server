# cors_proxy_server
This server is used as a proxy between front-end and tensorflow serving container.

CORS is not enabled in tf serving, thus it can't be called directly from the browser. 
This simple proxy server written in Flask has CORS enabled. 
