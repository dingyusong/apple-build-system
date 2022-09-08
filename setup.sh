#!/usr/bin/env bash

SourceDir=$HOME/.apple-build-system
if [ -d "$SourceDir" ];then
    echo "already set up"        
    cd $SourceDir
    git pull origin master
else
    git clone https://github.com/dingyusong/apple-build-system.git  $SourceDir
    cd $SourceDir
fi

program_exists() {
    local ret='0'
    command -v $1 >/dev/null 2>&1 || { local ret='1'; }
    if [ "$ret" -ne 0 ]; then
        return 1
    fi
    return 0
}

if program_exists "bundle"; then
    echo "bundle exist"
else
    echo "bundle not exist , install it"
    gem install bundler
fi

if program_exists "fastlane" || program_exists "fir" ; then
    echo "fastlane and fir exist"
else
    echo "astlane or fir not exist , install it"
    bundle install
fi


if python3 -c "import requests"; then
    echo "requests exist"
else
    echo "requests not exist , install it"
    pip3 install requests
fi


function update_shell_env() {
	cmdd=$1
	if [ `grep -c "$cmdd" ~/.zshrc` -eq '0' ]; then
		echo "add to .zshrc: ${cmdd} "
		echo $cmdd  >> ~/.zshrc
        `$cmdd`
	else
		echo ".zshrc already contain: ${cmdd} "
	fi  
}

# update_shell_env 'export PYTHONPATH=$PYTHONPATH:~/.apple-build-system/1-build_ipa'
# update_shell_env 'export PYTHONPATH=$PYTHONPATH:~/.apple-build-system/2-upload_ipa'
# update_shell_env 'export PYTHONPATH=$PYTHONPATH:~/.apple-build-system/3-upload_symbol/upload_umeng_dsym'
# update_shell_env 'export PYTHONPATH=$PYTHONPATH:~/.apple-build-system/4-generate_update_info'
# update_shell_env 'export PYTHONPATH=$PYTHONPATH:~/.apple-build-system/5-update_info'

# update_shell_env 'export PATH=$PATH:~/.apple-build-system/1-build_ipa'
# update_shell_env 'export PATH=$PATH:~/.apple-build-system/2-upload_ipa'
# update_shell_env 'export PATH=$PATH:~/.apple-build-system/3-upload_symbol/upload_umeng_dsym'
# update_shell_env 'export PATH=$PATH:~/.apple-build-system/4-generate_update_info'
# update_shell_env 'export PATH=$PATH:~/.apple-build-system/5-update_info'

# source ~/.zshrc

update_shell_env 'source ~/.apple-build-system/abs-env-source'




