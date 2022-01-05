FROM ubuntu:20.04

ARG DEBIAN_FRONTEND="noninteractive"

WORKDIR /root

# Install Prerequisites
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        software-properties-common \
        python3 \
        python3-pip \
        gpg-agent \
        curl \
        wget \
        unzip \
        xvfb

# Install Wine
RUN dpkg --add-architecture i386 \
    && wget -nv -O- https://dl.winehq.org/wine-builds/winehq.key | apt-key add - \
    && add-apt-repository "deb https://dl.winehq.org/wine-builds/ubuntu/ focal main" \
    && apt-get update \
    && apt-get install -y --install-recommends winehq-stable \
    && wine wineboot --init 

# Install IDA Requirements (Python)
RUN wget -nv https://www.python.org/ftp/python/2.7.18/python-2.7.18.amd64.msi \
    && wine msiexec /qn /i python-2.7.18.amd64.msi /L*V! python_install.log \
    && rm python-2.7.18.amd64.msi python_install.log

# Install IDA
ARG IDA_ZIP="IDA_7.0.zip"
ARG IDA_REG="ida.reg"
ARG IDA_SCRIPT="ida.sh"

COPY $IDA_ZIP /root/.wine/drive_c/
COPY $IDA_REG /root/.wine/drive_c/
COPY $IDA_SCRIPT /usr/bin/

RUN cd /root/.wine/drive_c/ \
    && unzip $IDA_ZIP && rm $IDA_ZIP \
    && wine regedit /C $IDA_REG \
    && while pgrep wineserver > /dev/null; do echo "Waiting for wineserver"; sleep 1; done \
    && rm $IDA_REG

# HTTP Server
ARG IDA_SERVER="./server"
COPY $IDA_SERVER ./server

RUN cd ./server \
    && pip3 install -r requirements.txt

EXPOSE 5000
CMD [ "python3", "./server/server.py"]
# ENTRYPOINT [ "sleep", "infinity" ]