# SSLStrip Victim

The Arpspoof Victim is a VNC-enabled Ubuntu 18.04 container. It includes both a terminal and web browser that will be used to access the simple web application hosted by the server. This container is based on fcwu/docker-ubuntu-vnc-desktop container and adds networking tools to it.

To build the container:

``
docker build -t cheesehub/sslstrip-victim .
``

The VNC interface can be accessed on port 80. To run the container,

``
docker run -d -p 80 cheesehub/sslstrip-victim .
``


