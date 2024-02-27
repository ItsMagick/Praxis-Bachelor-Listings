#!/bin/bash
set -ex
echo "running gcc docker: gcc-4.8 -Wall -Wextra example-tcp-server.c -o example-tcp-server.o"

docker run \
  --rm -v ${PWD}:/pwd \
  --workdir /pwd \
  -it arm32v7/ubuntu:18.04 \
  bash -c 'apt-get update -y; \
    apt-get install gcc-4.8 -y; \
    gcc-4.8 -Wall -Wextra example-tcp-server.c -o example-tcp-server.o'
