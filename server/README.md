# Arpspoof Server

This container implements a server that a victim communicates with before being subjected to an ARP poisoning attack. 
The container includes a simple web server and Wetty web-based terminal interface. 

To build the container,

``
docker build -t cheesehub/arpspoof-server .
``

To run and access the Wetty terminal,

``
docker run -d -p 3000 cheesehub/arpspoof-server
``
