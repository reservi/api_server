FROM armdocker.rnd.ericsson.se/dockerhub-ericsson-remote/python:3.9.5-alpine3.14 AS base_env

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Part where all environment variables should be stored
FROM base_env as prep_env
ENV SOMETESTENV SOMETESTVAL


FROM prep_env AS production
COPY . .
RUN python3 setup.py install

ENTRYPOINT [ "reservi" ]