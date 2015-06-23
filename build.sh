#!/bin/bash

set -e

DIR=$(cd $(dirname $0); pwd)
BUILD_DIR=$DIR/build
VIRTUALENV=$BUILD_DIR/virtualenv

test -d $BUILD_DIR && rm -rf $BUILD_DIR
mkdir -p $BUILD_DIR
virtualenv $VIRTUALENV
$VIRTUALENV/bin/pip install -r requirements.txt

echo $DIR/sources/thinkstats > \
    $VIRTUALENV/lib/python2.7/site-packages/think-stats.pth
