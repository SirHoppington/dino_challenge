# Download base image
FROM python:3.9 AS base

LABEL maintainer="nickhopgood@gmail.com"
LABEL description="Dockerfile for Dino challenge"

ENV PYTHONUNBUFFERED True

#Create a working directory for container to run.
WORKDIR /usr/src/app

COPY dino_app/ dino_app/


# Install requirements
RUN pip3 install --no-cache-dir -r dino_app/requirements.txt

# Run test build stage only, tests are not carried over to production image.
FROM base as test

COPY --from=base /usr/src/app /usr/src/app
WORKDIR /usr/src/app
# Copy tests to container

# Run unit tests only.
#RUN ["pytest", "-vv"]

# Create full image
FROM test as production

ADD run.sh /
RUN chmod +x /run.sh

CMD ["/run.sh"]