#!/usr/bin/env bash

VERSION=`jq -r ".version" package.json`
SERIES=${VERSION:0:4}-latest
cat package.json | grep -v electron > server-package.json
echo "${VERSION}"
