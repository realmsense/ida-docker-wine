FROM ubuntu:20.04

ARG DEBIAN_FRONTEND="noninteractive"

WORKDIR /root

# Install prerequisites
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        software-properties-common \
        gpg-agent \
        curl \
        wget \
        unzip \
        xvfb

# Install wine
RUN dpkg --add-architecture i386 \
    && wget -nv -O- https://dl.winehq.org/wine-builds/winehq.key | apt-key add - \
    && add-apt-repository "deb https://dl.winehq.org/wine-builds/ubuntu/ focal main" \
    && apt-get update \
    && apt-get install -y --install-recommends winehq-stable \
    && wine wineboot --init 

# Install python
RUN wget -nv https://www.python.org/ftp/python/2.7.18/python-2.7.18.amd64.msi \
    && wine msiexec /qn /i python-2.7.18.amd64.msi /L*V! python_install.log \
    && rm python-2.7.18.amd64.msi python_install.log

# TODO: Environmental variables should persist from the installer above, we shouldn't need to manually set these.
# sed -n -e "s/^Name: Path, Value: \(.*\), Action.*$/\1/p" python_install.log
ENV WINEPATH="C:\Python27\;C:\Python27\Scripts;C:\windows\system32;C:\windows;C:\windows\system32\wbem;C:\windows\system32\WindowsPowershell\v1.0"
ENV PYTHONHOME="C:\Python27"
ENV PYTHONPATH="C:\Python27\Lib"

# Install IDA
ARG IDA_ZIP="IDA_7.0.zip"
ARG IDA_REG="ida.reg"

COPY $IDA_ZIP /root/.wine/drive_c/
COPY $IDA_REG /root/.wine/drive_c/

RUN cd /root/.wine/drive_c/ \
    && unzip $IDA_ZIP && rm $IDA_ZIP \
    && wine regedit /C $IDA_REG && \
    while pgrep wineserver > /dev/null; do echo "Waiting for wineserver"; sleep 1; done

ENV WINEPATH="$WINEPATH;C:\IDA"

ENTRYPOINT [ "sleep", "infinity" ]