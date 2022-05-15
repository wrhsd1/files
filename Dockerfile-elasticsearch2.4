FROM openjdk:8-jre

# grab gosu for easy step-down from root
ENV GOSU_VERSION 1.14
RUN set -x && \
    curl -Lo /usr/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-arm64" && \
    curl -Lo /tmp/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-arm64.asc" && \
    export GNUPGHOME="$(mktemp -d)" && \
    gpg --batch --keyserver hkps://keys.openpgp.org --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 && \
    gpg --batch --verify /tmp/gosu.asc /usr/bin/gosu && \
    rm -r "$GNUPGHOME" /tmp/gosu.asc && \
    chmod +x /usr/bin/gosu && \
    # Allow user to become root
    #chmod u+s /usr/bin/gosu && \
    gosu nobody true


# https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-repositories.html
# https://www.elastic.co/guide/en/elasticsearch/reference/5.0/deb.html
RUN apt-key adv --keyserver hkps://keys.openpgp.org --recv-keys 46095ACC8548582C1A2699A9D27D666CD88E42B4

ENV ELASTICSEARCH_MAJOR 2.4
ENV ELASTICSEARCH_VERSION 2.4.0

RUN cd /tmp \
  && wget -q https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-${ELASTICSEARCH_VERSION}.deb

RUN cd /tmp \
  && dpkg -i elasticsearch-${ELASTICSEARCH_VERSION}.deb

RUN set -x \
	&& apt-get update \
  && rm -rf /var/lib/apt/lists/*

ENV PATH /usr/share/elasticsearch/bin:$PATH

WORKDIR /usr/share/elasticsearch

RUN set -ex \
	&& for path in \
		./data \
		./logs \
		./config \
		./config/scripts \
	; do \
		mkdir -p "$path"; \
		chown -R elasticsearch:elasticsearch "$path"; \
	done

COPY config ./config

VOLUME /usr/share/elasticsearch/data

COPY docker-entrypoint.sh /

EXPOSE 9200 9300
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["elasticsearch"]
