#!/bin/bash

SCRIPT_DIR="$(
    cd "$(dirname "$0")"
    pwd
)"

IPA_PATH=$1
FIR_TOKEN=$2
FIR_SHORT_LINK=$3
FIR_LOG_PATH=$4

fir publish ${IPA_PATH} -T ${FIR_TOKEN} -s ${FIR_SHORT_LINK} -Q --verbose --need_release_id > ${FIR_LOG_PATH}

