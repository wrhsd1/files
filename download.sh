#!/usr/bin/env bash

VERSION=`jq -r ".version" package.json`


wget https://github.com/zadam/trilium/releases/download/v${VERSION}/trilium-linux-x64-${VERSION}.tar.xz
tar -xf trilium-linux-x64-${VERSION}.tar.xz && mv trilium-linux-x64 /workdir/trilium-trans/
cd /workdir/trilium-trans-release
ls
