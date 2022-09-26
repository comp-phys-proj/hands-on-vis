#!/bin/bash

HERE="${BASH_SOURCE[0]}"
eval HEREDIR="$(dirname "$HERE")"
DIR="$(cd "$HEREDIR"; pwd -P)"
export PYTHONPATH="$PYTHONPATH:$DIR/dscribe"
