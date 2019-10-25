FROM tryton/tryton:5.2 as builder
USER root
RUN mkdir /module
COPY ./demo /module
WORKDIR /module
RUN python3 setup.py sdist

FROM tryton/tryton:5.2
LABEL maintainer="a <a>" \
      org.label-schema-url="a" \
      org.label-schema.vendor="d"
ENV VERSION 5.2.0

USER root
COPY --from=builder /module/dist /dist
RUN pip3 install /dist/* \
    && rm -rf /root/.cache
USER trytond
