FROM arm32v7/buildpack-deps
CMD ["bash"]

RUN apt-get update && \
     apt-get install -y --no-install-recommends ca-certificates curl wget file bzr git mercurial openssh-client subversion procps && \
      rm -rf /var/lib/apt/lists/*
RUN if ! command -v gpg > /dev/null; then apt-get install -y --no-install-recommends gnupg2 dirmngr; rm -rf /var/lib/apt/lists/*; fi
RUN apt-get update; apt-get install -y --no-install-recommends autoconf automake bzip2 dpkg-dev file g++ gcc imagemagick libbz2-dev libc6-dev libcurl4-openssl-dev libdb-dev libevent-dev libffi-dev libgdbm-dev libgeoip-dev libglib2.0-dev libjpeg-dev libkrb5-dev liblzma-dev libmagickcore-dev libmagickwand-dev libncurses-dev libpng-dev libpq-dev libreadline-dev libsqlite3-dev libssl-dev libtool libwebp-dev libxml2-dev libxslt-dev libyaml-dev make patch xz-utils zlib1g-dev $(if apt-cache show 'default-libmysqlclient-dev' 2>/dev/null | grep -q '^Version:'; then echo 'default-libmysqlclient-dev'; else echo 'libmysqlclient-dev'; fi); rm -rf /var/lib/apt/lists/*
RUN if ! command -v gpg > /dev/null; then apt-get update; apt-get install -y --no-install-recommends gnupg2 dirmngr; rm -rf /var/lib/apt/lists/*; fi

ENV GCC_VERSION=4.8.1

RUN buildDeps='dpkg-dev flex'; \
    apt-get update; \
    apt-get install -y --no-install-recommends $buildDeps; \
    rm -r /var/lib/apt/lists/*; \
    wget https://ftp.fu-berlin.de/unix/languages/gcc/releases/gcc-4.8.1/gcc-4.8.1.tar.bz2; \
    mkdir -p /usr/src/gcc2; \
    tar -xvjf gcc-4.8.1.tar.bz2 -C /usr/src/gcc2 --strip-components=1; \
    rm gcc-4.8.1.tar.bz2; \
    cd /usr/src/gcc2; \
    ./contrib/download_prerequisites; \
    { rm *.tar.* || true; }; \
    for f in config.guess config.sub; \
    do wget -O "$f" "https://git.savannah.gnu.org/cgit/config.git/plain/$f?id=7d3d27baf8107b630586c962c057e22149653deb"; \
    find -mindepth 2 -name "$f" -exec cp -v "$f" '{}' ';'; \
    done; \
    dir="$(mktemp -d)"; \
    cd "$dir"; \
    extraConfigureArgs=''; \
    dpkgArch="$(dpkg --print-architecture)"; \
    case "$dpkgArch" in armel) extraConfigureArgs="$extraConfigureArgs --with-arch=armv4t --with-float=soft";; \
       armhf) extraConfigureArgs="$extraConfigureArgs --with-arch=armv7-a --with-float=hard --with-fpu=vfpv3-d16 --with-mode=thumb" ;; \
       i386) osVersionID="$(set -e; . /etc/os-release; echo "$VERSION_ID")"; \
    case "$osVersionID" in 8) extraConfigureArgs="$extraConfigureArgs --with-arch-32=i586" ;;  \
        *) extraConfigureArgs="$extraConfigureArgs --with-arch-32=i686" ;; esac; ;; esac; \
    gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)"; \
    /usr/src/gcc2/configure --build="$gnuArch" --disable-multilib --enable-languages=c,c++,fortran,go $extraConfigureArgs; \
    make -j "$(nproc)"; \
    make install-strip; \
    cd .. ; \
    rm -rf "$dir"; \
    apt-get purge -y --auto-remove $buildDeps




