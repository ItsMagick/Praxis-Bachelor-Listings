FROM buildpack-deps:jammy

RUN set -ex; \
    apt-get update; \
    apt-get install -y --no-install-recommends; \
    wget https://launchpad.net/gcc-arm-embedded/4.8/4.8-2014-q2-update/+download/gcc-arm-none-eabi-4_8-2014q2-20140609-src.tar.bz2; \
    tar -xvjf  ./gcc-arm-none-eabi-4_8-2014q2-20140609-src.tar.bz2; \
    \
    #apt-get install gcc-4.8

#RUN set -ex; \
#	\
#	savedAptMark="$(apt-mark showmanual)"; \
#	apt-get update && apt-get install file; \
#    mkdir install_g++-4.8; \
#    cd install_g++-4.8; \
#    wget http://mirrors.edge.kernel.org/ubuntu/pool/universe/g/gcc-4.8-armhf-cross/g++-4.8-arm-linux-gnueabihf_4.8.5-4ubuntu1cross2_amd64.deb; \
#    wget http://mirrors.edge.kernel.org/ubuntu/pool/universe/g/gcc-4.8-armhf-cross/libsfstdc++-4.8-dev-armhf-cross_4.8.5-4ubuntu1cross2_all.deb; \
#    wget http://mirrors.edge.kernel.org/ubuntu/pool/universe/g/gcc-4.8-armhf-cross/gcc-4.8-arm-linux-gnueabihf-base_4.8.5-4ubuntu1cross2_amd64.deb; \
#    wget http://mirrors.edge.kernel.org/ubuntu/pool/universe/g/gcc-4.8-armhf-cross/gcc-4.8-arm-linux-gnueabihf_4.8.5-4ubuntu1cross2_amd64.deb; \
#    wget http://mirrors.edge.kernel.org/ubuntu/pool/universe/g/gcc-4.8-armhf-cross/libgcc-4.8-dev-armhf-cross_4.8.5-4ubuntu1cross2_all.deb; \
#    wget http://mirrors.edge.kernel.org/ubuntu/pool/universe/g/gcc-4.8-armhf-cross/cpp-4.8-arm-linux-gnueabihf_4.8.5-4ubuntu1cross2_amd64.deb; \
#    wget http://mirrors.edge.kernel.org/ubuntu/pool/universe/g/gcc-4.8-armhf-cross/libasan0-armhf-cross_4.8.5-4ubuntu1cross2_all.deb; \
#    apt-get install ./gcc-4.8-arm-linux-gnueabihf_4.8.5-4ubuntu1cross2_amd64.deb ./gcc-4.8-arm-linux-gnueabihf-base_4.8.5-4ubuntu1cross2_amd64.deb ./libsfstdc++-4.8-dev-armhf-cross_4.8.5-4ubuntu1cross2_all.deb ./cpp-4.8-arm-linux-gnueabihf_4.8.5-4ubuntu1cross2_amd64.deb ./libgcc-4.8-dev-armhf-cross_4.8.5-4ubuntu1cross2_all.deb ./libasan0-armhf-cross_4.8.5-4ubuntu1cross2_all.deb ./g++-4.8-arm-linux-gnueabihf_4.8.5-4ubuntu1cross2_amd64.deb