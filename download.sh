#!/usr/bin/env bash

VERSION=`jq -r ".version" package.json`


wget https://github.com/zadam/trilium/releases/download/v${VERSION}/trilium-linux-x64-${VERSION}.tar.xz
tar -xf trilium-linux-x64-${VERSION}.tar.xz && mv trilium-linux-x64 /workdir/trilium-trans/
cd /workdir/trilium-trans-release
mkdir mac windows linux && chmod -R 777 mac windows linux
wget https://github.com/zadam/trilium/releases/download/v${VERSION}/trilium-linux-x64-${VERSION}.tar.xz  -O /linux/trilium-linux-x64-${VERSION}.tar.xz
wget https://github.com/zadam/trilium/releases/download/v${VERSION}/trilium-mac-x64-${VERSION}.zip  -O /mac/trilium-mac-x64-${VERSION}.zip
wget https://github.com/zadam/trilium/releases/download/v${VERSION}/trilium-windows-x64-${VERSION}.zip -O /windows/trilium-windows-x64-${VERSION}.zip
ls
