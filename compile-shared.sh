#!/bin/bash

echo "running gcc docker: gcc-4.8 -fPIC -Wall -Wextra sockfuzz.c -shared -ldl -o sockfuzz.so"

docker run \
  --rm -v ${PWD}:/pwd \
  --workdir /pwd \
  -it arm32v7/ubuntu:18.04 \
  bash -c 'apt-get update -y; \
    apt-get install gcc-4.8 -y; \
    gcc-4.8 -fPIC -Wall -Wextra sockfuzz.c -shared -ldl -o sockfuzz.so'

cp ./socketfuzz.so ../../root/app