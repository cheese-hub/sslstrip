# SSLStrip Hacker

This container includes a Jupyter notebook server and two Jupyter notebooks with step-by-step instructions for performing an ARP poisoning attack and a SSL strip attack. 

To build the container:

``
docker build -t cheesehub/sslstrip-hacker .
``

To run:

``
docker run --cap-add=NET_ADMIN -d -p 8888 cheesehub/sslstrip-hacker
``
