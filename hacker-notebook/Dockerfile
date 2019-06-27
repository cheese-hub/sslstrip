# Based on the jupyter base notebook
FROM jupyter/base-notebook:61d8aaedaeaf
MAINTAINER Rajesh Kalyanam <rkalyanapurdue@gmail.com>

USER root

# Install the necessary networking tools
RUN apt-get update && \
    apt-get install -yq --no-install-recommends \
    gcc=4:7.4.0-1ubuntu2.3 \
    libc-dev \
    dsniff=2.4b1+debian-28.1~build1 \
    inetutils-ping=2:1.9.4-3 \
    inetutils-traceroute=2:1.9.4-3 \
    net-tools=1.60+git20161116.90da8a0-1ubuntu1 \
    iptables=1.6.1-2ubuntu2 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

#Allow Jupyter user (jovyan) to modify IP tables, run arpspoof
#as root without a password
ADD hackersudo /etc/sudoers.d/
RUN chmod 0400 /etc/sudoers.d/hackersudo

# Create a Python 2.x environment using conda including at least the ipython kernel
# and the kernda utility. Add any additional packages you want available for use
# in a Python 2 notebook to the first line here (e.g., pandas, matplotlib, etc.)
RUN conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 ipython=5.8.0 ipykernel=4.10.0 kernda=0.3.0 && \
    conda clean -tipsy

# Create a global kernelspec in the image and modify it so that it properly activates
# the python2 conda environment.
RUN $CONDA_DIR/envs/python2/bin/python -m ipykernel install && \
    $CONDA_DIR/envs/python2/bin/kernda -o -y /usr/local/share/jupyter/kernels/python2/kernel.json && \
    echo "source activate python2" > ~/.bashrc

# Add the new python2 binaries to the standard path
ENV PATH $CONDA_DIR/envs/python2/bin:$PATH

COPY sslstrip /tmp

WORKDIR /tmp

# Install SSLStrip and its dependencies
RUN pip install pyopenssl==19.0.0 service_identity==18.1.0 Twisted==18.9.0 && \
    python setup.py install && \
    rm -rf /tmp/sslstrip && \
    fix-permissions $CONDA_DIR

#copy the primary notebook
COPY --chown=1000:100 Hacker.ipynb $HOME/
COPY --chown=1000:100 SSLStrip.ipynb $HOME/

WORKDIR $HOME

CMD ["start-notebook.sh","--NotebookApp.token="]

