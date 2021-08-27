#!/bin/bash

SCRIPT_DIR="$(
    cd "$(dirname "$0")"
    pwd
)"


# buildno=`date +%Y%m%d%H%M%S`

path_xcodeproj=$1
scheme_name=$2
buildno=$3

path_xcodeproj_dir=$(dirname $path_xcodeproj)

path_build_dir="${path_xcodeproj_dir}/build/$scheme_name/${buildno}"
path_build_log_file="${path_build_dir}/build.log"

mkdir -p $path_build_dir
touch $path_build_log_file
