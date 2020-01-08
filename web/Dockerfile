FROM ubuntu:latest

RUN apt-get -y update
RUN apt install python3.5 python3-pip
RUN pip3 install --upgrade pip

ADD app /app
ADD a.sh /app/a.sh
RUN chmod 755 /app/a.sh

RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install --yes USE_AVX_INSTRUCTIONS

# COPY . /root/face_recognition
# RUN cd /root/face_recognition && \
#     pip3 install -r requirements.txt && \
#     python3 setup.py install

RUN pip3 install Flask SQLAlchemy flask-sqlalchemy PyMySQL Flask-Migrate opencv-python


WORKDIR /app
CMD ./a.sh