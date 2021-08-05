#!/bin/sh

PROXY=proxychains4

URL=https://github.com/sonatype/nexus-public.git
SRC=~/rpmbuild/SOURCES
SKIPTEST=true
BUILDVERSION=1
RELEASE=release-3.33.0-01

rpmdev-setuptree
cd ${SRC}
${PROXY} git clone ${URL}
cd ${SRC}/nexus-public
${PROXY} git fetch --tags
git checkout -b ${RELEASE} origin/${RELEASE} --
sudo ${PROXY} ./mvnw clean install -DskipTests=${SKIPTEST} -Dbuild.revision=${BUILDVERSION}
