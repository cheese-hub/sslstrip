# SSLStrip Server

This container implements a server that a victim communicates with before being subjected to an ARP poisoning attack and a SSL strip attack. 
The container includes a Jupyter notebook server. 

To build the container:

``
docker build -t cheesehub/sslstrip-server .
``

To run:

``
docker run -d -p 8888 cheesehub/sslstrip-server
``
