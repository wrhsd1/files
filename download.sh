#!/usr/bin/env bash

VERSION=`jq -r ".version" package.json`


wget https://github.com/zadam/trilium/releases/download/v${VERSION}/trilium-linux-x64-${VERSION}.tar.xz
tar -xf trilium-linux-x64-${VERSION}.tar.xz && mv trilium-linux-x64 /workdir/trilium-trans/
cd /workdir/trilium-trans-release
wget https://github.com/zadam/trilium/releases/download/v${VERSION}/trilium-linux-x64-${VERSION}.tar.xz  -O trilium-linux-x64.tar.xz
wget https://github.com/zadam/trilium/releases/download/v${VERSION}/trilium-linux-x64-server-${VERSION}.tar.xz  -O trilium-linux-x64-server.tar.xz
wget https://github.com/zadam/trilium/releases/download/v${VERSION}/trilium-mac-x64-${VERSION}.zip  -O trilium-mac-x64.zip
wget https://github.com/zadam/trilium/releases/download/v${VERSION}/trilium-windows-x64-${VERSION}.zip  -O trilium-windows-x64.zip
ls
