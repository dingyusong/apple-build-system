#!/bin/bash

curl --location --request POST "$1" \
--form "OSSAccessKeyId="\"$2\" \
--form "key="\"$3\" \
--form "policy="\"$4\" \
--form "signature="\"$5\" \
--form "callback="\"$6\" \
--form "file=@"\"$7\"