#!/bin/bash
set -x buildDeps='dpkg-dev flex';
apt-get update;
apt-get install -y --no-install-recommends $buildDeps;
rm -r /var/lib/apt/lists/*;
curl -fSL "http://ftpmirror.gnu.org/gcc/gcc-$GCC_VERSION/gcc-$GCC_VERSION.tar.bz2" -o gcc.tar.bz2;
curl -fSL "http://ftpmirror.gnu.org/gcc/gcc-$GCC_VERSION/gcc-$GCC_VERSION.tar.bz2.sig" -o gcc.tar.bz2.sig gpg --batch --verify gcc.tar.bz2.sig gcc.tar.bz2;
mkdir -p /usr/src/gcc;
tar -xf gcc.tar.bz2 -C /usr/src/gcc --strip-components=1;
rm gcc.tar.bz2*;
cd /usr/src/gcc;
./contrib/download_prerequisites;
{ rm *.tar.* || true; };
for f in config.guess config.sub;
do wget -O "$f" "https://git.savannah.gnu.org/cgit/config.git/plain/$f?id=7d3d27baf8107b630586c962c057e22149653deb";
find -mindepth 2 -name "$f" -exec cp -v "$f" '{}' ';';
done;
dir="$(mktemp -d)";
cd "$dir";
extraConfigureArgs='';
dpkgArch="$(dpkg --print-architecture)";
case "$dpkgArch" in armel) extraConfigureArgs="$extraConfigureArgs --with-arch=armv4t --with-float=soft";;
   armhf) extraConfigureArgs="$extraConfigureArgs --with-arch=armv7-a --with-float=hard --with-fpu=vfpv3-d16 --with-mode=thumb" ;;
   i386) osVersionID="$(set -e; . /etc/os-release; echo "$VERSION_ID")";
case "$osVersionID" in 8) extraConfigureArgs="$extraConfigureArgs --with-arch-32=i586" ;; *)
 extraConfigureArgs="$extraConfigureArgs --with-arch-32=i686" ;; esac; ;; esac; gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)"; /usr/src/gcc/configure --build="$gnuArch" --disable-multilib --enable-languages=c,c++,fortran,go $extraConfigureArgs; make -j "$(nproc)"; make install-strip; cd ..; rm -rf "$dir"; apt-get purge -y --auto-remove $buildDeps
