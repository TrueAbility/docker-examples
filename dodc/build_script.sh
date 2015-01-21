#!/bin/sh

REPO="trueability"

build_image() {
    if [ ! -f dockerfiles/Dockerfile.$1 ];
    then
       echo "ERROR: couldn't find dockerfiles/Dockerfile.$1"
       exit 2
    fi

    echo "Building $1..."
    rm -f ./Dockerfile
    ln -s dockerfiles/Dockerfile.$1 ./Dockerfile
    docker build -t $REPO/$1 .  || exit 1
}

docker pull debian:stable

build_image dodc:task1
build_image dodc:task2
build_image dodc:task2_answer
build_image dodc:task3_web
build_image dodc:task3_db
build_image dodc:task4-snd
build_image dodc:task4-rcv

rm -f Dockerfile
