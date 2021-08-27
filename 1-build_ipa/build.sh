#!/bin/bash

SCRIPT_DIR="$(
    cd "$(dirname "$0")"
    pwd
)"

SourceDir="$HOME/.apple-build-system/1-build_ipa"
cd $SourceDir

platform="ios"
buildno=`date +%Y%m%d%H%M%S`

usage(){
    echo "Usage: `basename $0` -x <xcodeproj path> [option value]"
    echo "Options:"
    echo "      -x  xcodeproj path."
    echo "      -p  platform. optional, ios(default) or mac."
    echo "      -w  workspace path, optional,"
    echo "      -b  buildNo, optional,if not paas we will generate"
    echo "      -s  scheme_name, optional, default dump from xcodeproj path"
    echo "      -v  version, optional,"
    exit 1
}

while getopts ":x:m:p:w:b:s:hv:" opt; do 
  case $opt in
    x)  path_xcodeproj=$OPTARG;;
    p)  platform=$OPTARG ;;
    w)  path_workspace=$OPTARG ;;
    b)  buildno=$OPTARG;;
    s)  scheme_name=$OPTARG;;
    v)  build_version=$OPTARG;;
    h)  usage;;
    :)
        echo "Option -$OPTARG requires an argument."
        exit 1
        ;;
    a)  usage;;
    ?)  echo "Invalid option: -$OPTARG index:$OPTIND"
	    usage
      ;;
  esac
done

if [ ! -n "$1" ];then
    usage
fi

if [ ! -n "$scheme_name" ];then
    file_xcodeproj=$(basename $path_xcodeproj)
    name_xcodeproj=${file_xcodeproj%.*}
    scheme_name=${name_xcodeproj}
fi

source $SourceDir/output_build.sh $path_xcodeproj $scheme_name $buildno

fastlane $platform dev \
    path_workspace:$path_workspace \
    path_xcodeproj:$path_xcodeproj \
    scheme_name:${scheme_name} \
    build_number:${buildno} \
    build_version:${build_version} \
    output_directory:$path_build_dir \
    | tee -a ${path_build_log_file}