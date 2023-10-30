#!/bin/sh

renpy_sdk=renpy-${RENPY_VERSION}-sdk

echo "Downloading the SDK ($renpy_sdk)..."
wget -q https://www.renpy.org/dl/${RENPY_VERSION}/${renpy_sdk}.tar.bz2

echo "Setting up the SDK ($renpy_sdk)..."
tar -xjf ./${renpy_sdk}.tar.bz2
rm ./${renpy_sdk}.tar.bz2
mv ./${renpy_sdk} ./renpy

echo "Building the project..."
COMMAND="./renpy/renpy.sh ./renpy/launcher distribute ./game"
if $COMMAND; then
    built_dir=$(ls | grep '\-dists')
    echo Build version: ${built_dir%'-dists'}
else
    return 1
fi
