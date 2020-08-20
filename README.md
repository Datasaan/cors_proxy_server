#CorsProxyServer

The Tensorflow serving docker container doesn't have CORS enabled. So, browsers won't be able to call the container directly.
This server can be used as a proxy between front-end and tensorflow serving container.


This simple proxy server written in Flask has CORS enabled. 

