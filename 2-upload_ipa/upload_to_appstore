#!/bin/bash

apiKey=""
if [ -z "$1" ]; then
    echo -e "\033[31m Please enter apiKey \033[0m"
    read key
    while ([ -z "$key" ]); do
        echo -e "\033[31m Please enter apiKey \033[0m"
        read key
    done
    apiKey=$key
else
    apiKey=$1
fi

apiIssuer=""
if [ -z "$2" ]; then
    echo -e "\033[31m Please enter apiIssuer \033[0m"
    read issuer
    while ([ -z "$issuer" ]); do
        echo -e "\033[31m Please enter apiIssuer \033[0m"
        read issuer
    done
    apiIssuer=$issuer
else
apiIssuer=$2
fi

path_to_ipa=$3

echo -e "\033[46;30m apiKey is: $apiKey -- apiIssuer is: $apiIssuer \033[0m"

#上傳
function uploadFunc() {
    upload="xcrun altool --upload-app -f $path_to_ipa -t iOS --apiKey $apiKey --apiIssuer $apiIssuer --verbose"
    echo "running upload cmd" $upload
    uploadApp="$($upload)"
    echo uploadApp
    if [ -z "$uploadApp" ]; then
        echo -e "\033[31m upload failed \033[0m"
    else
        echo -e "\033[46;30m upload success \033[0m"
    fi
}

# 验证
validate="xcrun altool --validate-app -f $path_to_ipa -t iOS --apiKey $apiKey --apiIssuer $apiIssuer --verbose"
echo "running validate cmd" $validate

runValidate="$($validate)"
echo $runValidate

if [ -z "$runValidate" ]; then
    echo -e "033[31m validate failed \033[0m"
else
    uploadFunc
fi
