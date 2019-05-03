# SSL Strip Attack

## Description of the scenario

The SSL strip attack is a typical "man-in-the-middle" attack used to circumvent the security enforced by SSL certificates on HTTPS-enabled websites. It's a technique that downgrades your connection from secure HTTPS to insecure HTTP and exposes you to eavesdropping and data manipulation.

## Target Audience

### Instructors
If you are an instructor teaching cybersecurity concepts and, specifically network security, you can use this example to provide hands-on experience with SSLStrip attacks, demonstrating the ease with which network traffic can be compromised. The first step before conducting a SSLStrip attack is the ARPSpoof attack. Once a hacker has successfully poisoned ARP tables, even the SSL-enabled communication can be compromised. These two demonstrations together can illustrate the real-world impacts.

### Students
If you are a student in a cybersecurity or computer networks class, or, a budding web developer, it is instructive to understand how network traffic can be compromised by a well-situated hacker. If you are currently learning about SSL stripping in your class, you can get further practical experience with how these attacks operate, and, learn how to identify such attacks.

## Design and Architecture
This demonstration is designed using three Docker containers, one each for the hacker, victim, and, server attached to the same virtual network. The containers all come with the necessary network tools to ping, examine ARP tables, trace packet routing between machines and redirect HTTPs traffic. The hacker machine comes with the ARPSpoof command line tool for running an ARP poisoning attack and SSLStrip command line tool for initiating a SSL strip attack. The victim container provides a VNC interface to Ubuntu and the requisite commands can be run on the LXTerminal emulator. Both the hacker and server provide a Jupyter notebook interface; the necessary commands can be run in the terminal console provided by Jupyter. The hacker notebook contains instructions on conducting the ARP poisoning attack and SSLStrip attack; including the commands to be run on each of the three containers.


## Installation and Usage

### Installation

Build each of the containers separately:

```bash
cd hacker-notebook
docker build -t cheesehub/sslstrip-hacker .

cd victim-vnc
docker build -t cheesehub/sslstrip-victim .

cd server
docker build -t cheesehub/sslstrip-server .
```
The hacker provides a Jupyter notebook interface; the victim is a VNC-enabled Ubuntu 18.04 container and the server includes a simple web application and a Wetty terminal. We will expose different ports when running these containers:

```bash
docker run --cap-add=NET_ADMIN -d -p 8888 cheesehub/sslstrip-hacker

docker run -d -p 80 cheesehub/sslstrip-victim

docker run -d -p 8888 cheesehub/sslstrip-server
```

### Usage

Select SSLStrip.ipynb from the ``hacker`` Jupyter notebook interface for a step-by-step overview of executing the SSL Strip attack. The notebook included commands that need to be run on the victim and server. A terminal for running the commands from the notebook can be launched from the Jupyter notebook interface. In the ``victim`` VNC window, click the start menu at the bottom left corner and navigate the menu options to launch a terminal window. You will be prompted to login to the Wetty session in the ``server`` container. Use ``term`` for both the username and password.

SSL strip requires the three containers to be on the same local network. When running these containers using ``docker run``, they are all attached to the same Docker bridge network on the same host. However, if using Kubernetes ensure that the pods are all deployed to the same cluster node. Also, this demonstration has been found to not work when using certain overlay networks. Currently, this has been tested successfully on the Weave overlay network.  


