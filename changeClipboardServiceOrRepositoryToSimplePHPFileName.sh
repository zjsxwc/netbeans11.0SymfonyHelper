#!/bin/bash

_APP_HOME="$(cd $(dirname $0);pwd)"
_CMD="/usr/bin/python ${_APP_HOME}/changeClipboardServiceOrRepositoryToSimplePHPFileName.py"
exec ${_CMD}