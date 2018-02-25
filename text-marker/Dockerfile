FROM ubuntu:artful

ENV DEBIAN_FRONTEND=noninteractive \
    TERM=linux \
    LANG=en_US.UTF-8

RUN set -ex \
    && apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
      python3-opencv \
      locales \
    && sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \
    && locale-gen \
    && update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \
    && apt-get clean \
    && apt-get --purge autoremove -yqq \
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
