FROM    kalilinux/kali-last-release:latest


# https://nim-lang.org/install_unix.html
ENV     NIM_VERSION=1.6.2
ENV     NIM_HASH=9e0c616fe504402e29e43d44708a49416dcbfa295cee1883ce6e5bfb25c364f1
# https://github.com/jart/cosmopolitan/releases
ENV     COSMO_VERSION=1.0
ENV     COSMO_HASH=d6a11ec4cf85d79d172aacb84e2894c8d09e115ab1acec36e322708559a711cb

RUN     apt-get update && \
        apt-get -y upgrade && \
        apt-get -y install \
                gcc \
		gcc-mingw-w64 \
		git \
                golang-1.17 \
                metasploit-framework \
                python3-pip \
                unzip \
		upx \
                wget \
                xz-utils \
        && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*

RUN	cd /usr/src/ && \
	git clone --depth=1 https://github.com/xct/morbol && \
	GO111MODULE=off /usr/lib/go-1.17/bin/go get golang.org/x/sys/windows && \
	pip3 install donut-shellcode

RUN     cd /opt/ && \
        wget "https://nim-lang.org/download/nim-${NIM_VERSION}-linux_x64.tar.xz" && \
        [ X"${NIM_HASH}" = X$(sha256sum nim* | awk '{print $1;}') ] && \
        xz -cd ./nim* | tar -f- -x && \
        rm -rf *xz

RUN     mkdir /usr/src/cosmopolitan/ && \
        cd /usr/src/cosmopolitan/ && \
        wget "https://github.com/jart/cosmopolitan/releases/download/${COSMO_VERSION}/cosmopolitan-amalgamation-${COSMO_VERSION}.zip" && \
        [ X"${COSMO_HASH}" = X$(sha256sum cosmo* | awk '{print $1;}') ] && \
        unzip *zip && \
        rm -f *zip


ADD     ./requirements.txt /tmp/requirements.txt
RUN     pip3 install --no-cache-dir -r /tmp/requirements.txt && rm -f /tmp/requirements.txt
ADD     ./pop/ /opt/pop

RUN	rm -f /etc/profile.d/kali.sh

RUN     useradd -m -r -s/bin/false pop
USER    pop
WORKDIR /opt/
CMD     PATH="/opt/nim-${NIM_VERSION}/bin:/usr/lib/go-1.17/bin:${PATH}" waitress-serve --call --port "${PORT}" pop:create_bot
