#!/bin/sh
#参考:https://developer.qiniu.com/kodo/1302/qshell
#https://github.com/qiniu/qshell


WORK_DIR="$HOME/.apple-build-system/4-update_info"
cd $WORK_DIR

usage(){
    echo "Usage: `basename $0` -x <xcodeproj path> [option value]"
    echo "Options:"
    echo "      -a  ak"
    echo "      -s  sk"
    echo "      -p  space"
    echo "      -i  path_update_info"
    echo "      -u  update_url"
    echo "      -n  refershName"
    echo "      -h  help"
    exit 1
}

while getopts ":a:s:p:i:u:n:h" opt; do 
  case $opt in
    a)  ak=$OPTARG;;
    s)  sk=$OPTARG ;;
    p)  space=$OPTARG ;;
    i)  path_update_info=$OPTARG ;;
    u)  update_url=$OPTARG;;
    n)  refershName=$OPTARG;;
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

echo $update_url > $WORK_DIR/refersh_list.txt

$WORK_DIR/qshell account $ak $sk

$WORK_DIR/qshell fput $space $refershName $path_update_info true application/json

$WORK_DIR/qshell cdnrefresh $WORK_DIR/refersh_list.txt

echo "qshell refersh done!"
