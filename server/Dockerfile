# Based on the jupyter base notebook
FROM jupyter/base-notebook:61d8aaedaeaf

# File Author / Maintainer
MAINTAINER Rajesh Kalyanam "rkalyanapurdue@gmail.com"

USER root

# Update the repository sources list
# Install Apache2
RUN apt-get update && \
    apt-get install -y \
	apache2=2.4.29-1ubuntu4.6 \
	apache2-utils=2.4.29-1ubuntu4.6 \
	libapache2-mod-wsgi-py3=4.5.17-1 \
	ssl-cert=1.0.39 \
	net-tools=1.60+git20161116.90da8a0-1ubuntu1 \
	supervisor=3.3.1-1.1

# Create the default directory
RUN mkdir -p /srv/www/app

# Clone the app and install packages
ADD app /srv/www/app
RUN pip install Flask==1.0.3

#copy conf files for our new app over to Apache's conf
ADD conf /etc/apache2/sites-available

#enable various Apache modules
RUN a2enmod wsgi && \
    a2enmod ssl && \
    a2enmod rewrite

#disable default sites and use our app instead
RUN a2dissite 000-default && \
    a2dissite default-ssl && \
    a2ensite server && \
    a2ensite server-ssl

#copy supervisord config file
#need to start both Apache and Jupyter notebook server
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#copy the primary notebook
COPY --chown=1000:100 Server.ipynb $HOME/

# Expose the Apache and Jupyter ports
EXPOSE 80
EXPOSE 8888

# Set default container command
ENTRYPOINT ["/usr/bin/supervisord"]

