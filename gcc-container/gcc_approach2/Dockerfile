FROM arm32v7/buildpack-deps:buster

# https://gcc.gnu.org/mirrors.html

ENV GCC_VERSION 4.8.1

# "download_prerequisites" pulls down a bunch of tarballs and extracts them,
# but then leaves the tarballs themselves lying around
RUN apt-get update \
	&& apt-get install -y curl flex wget \
	&& rm -r /var/lib/apt/lists/* \
	&& wget https://ftp.fu-berlin.de/unix/languages/gcc/releases/gcc-4.8.1/gcc-4.8.1.tar.bz2 \
	&& mkdir -p /usr/src/gcc2 \
	&& tar -xvjf gcc-4.8.1.tar.bz2 -C /usr/src/gcc2 --strip-components=1 \
	&& rm gcc-4.8.1.tar.bz2* \
	&& cd /usr/src/gcc2 \
	&& ./contrib/download_prerequisites \
		&& dir="$(mktemp -d)" \
	&& cd "$dir" \
	&& /usr/src/gcc2/configure \
		--disable-multilib \
		--enable-languages=c,c++ \
	&& make -j"$(nproc)" \
	&& make install-strip \
	&& cd .. \
	&& rm -rf "$dir" \
	&& apt-get purge -y --auto-remove curl gcc g++ wget