FROM ubuntu:artful

ENV DEBIAN_FRONTEND=noninteractive \
    TERM=linux \
    LANG=en_US.UTF-8

RUN set -ex \
    && apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends software-properties-common \
    && add-apt-repository -y ppa:alex-p/tesseract-ocr \
    && apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
      git \
      build-essential \
      tesseract-ocr \
      tesseract-ocr-chi-tra \
      tesseract-ocr-chi-tra-vert \
      tesseract-ocr-chi-sim \
      tesseract-ocr-chi-sim-vert \
      libtesseract-dev \
      libleptonica-dev \
      python3-pip \
      python3-dev \
      python3-pil \
      locales \
    && sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \
    && locale-gen \
    && update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \
    && python3 -m pip install -U pip setuptools wheel \
    && CPPFLAGS=-DUSE_STD_NAMESPACE pip3 install \
      git+https://github.com/sirfz/tesserocr@9564fac1ef23bec304ce1ed74f976fae17c0c8c5 \
    && apt-get --purge autoremove -yqq \
      build-essential \
      python3-dev \
    && apt-get clean \
    && rm -rf \
      /var/lib/apt/lists/* \
      /tmp/* \
      /var/tmp/* \
      /usr/share/man \
      /usr/share/doc \
      /usr/share/doc-base

ADD run.py /

ENTRYPOINT ["/run.py"]
