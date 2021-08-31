iOS/macOS 打包，上传ipa，上传符号表，更新提示，工具包，灵活扩展，一体化Python解决方案。



# 安装

github

```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/dingyusong/apple-build-system/master/setup.sh)" 
or
sh -c "$(wget -O- https://raw.githubusercontent.com/dingyusong/apple-build-system/master/setup.sh)" 
```



```
source ~/.zshrc
```



# 使用

**Life is  short, use python！**



## 打个包

```python
from build_ipa import IPABuilder
builder = IPABuilder(path_xp = path_xp)
```

是对打包工具 [fastlane](https://fastlane.tools/)的封装，默认自动签名。

## 上传到fir

```python
from upload_ipa_to_fir import UploadIPAToFir
path_ipa        = builder.build_ipa_path()
fir_token       = "xxx"
fir_shortlink   = "xxx"
ipa_uploader    = UploadIPAToFir(
    path_ipa        = path_ipa, 
    fir_token       = fir_token, 
    fir_shortlink   = fir_shortlink)
```

是对测试分发平台 [fir-cli](https://github.com/FIRHQ/fir-cli)的封装。

## 上传符号表

上传到友盟

```python
from upload_symb_to_umeng import UploadDSYMToUmeng
umeng_appkey        = "xxx"
umeng_apikey        = xxx
umeng_apisecurity   = "xxx"
path_to_symbol      = builder.build_symbol_path()
umeng_appVersion    = builder.version
umeng_fileName      = builder.build_symbol_name()
symbol_uploader     = UploadDSYMToUmeng(
    appKey      = umeng_appkey,
    apiKey      = umeng_apikey,
    apiSecurity = umeng_apisecurity,
    pathToSym   = path_to_symbol,
    appVersion  = umeng_appVersion, 
    fileName    = umeng_fileName)
```

是对[友盟上传符号表工具](https://developer.umeng.com/docs/193624/detail/194577#p-1fo-zuq-vyv)的封装。

## 生成更新信息

使用默认更新模板

```python
from generate_update_info import GenerateUpdateInfo
buildNo         = builder.build_no
updateMsg       = "测试包已更新"
updateInfo_path = os.path.join(builder.build_dir(), "updateInfo")
url_to_download = fir_shortlink
update_info_builder = GenerateUpdateInfo(
    buildNo         = buildNo,
    updateMsg       = updateMsg,
    updateInfo_path = updateInfo_path,
    url_to_download = url_to_download)
```

自己写得根据模板生成一个json对象。

## 上传更新信息

上传更新信息到七牛云

```python
from upload_info_to_qiniu import UploadInfoToQiNiu
ak              = 'xxx'
sk              = 'xxx'
space           = 'xxx'
path_update_info= xxx
update_url      = 'http://xxx'
refershName     = 'xxx'
qiniu_uploader = UploadInfoToQiNiu(
    ak              = ak,
    sk              = sk,
    space           = space,
    path_update_info= path_update_info,
    update_url      = update_url,
    refershName     = refershName)
```

对[七牛云qshell的上传文件](https://github.com/qiniu/qshell)并刷新cdn的功能封装。



# 组合

每个模块可视为一个链表的节点，可以将多个节点用next指针连接起来组成一个环环相扣的链表。

1. 打包->上传到fir

```
builder.next                = ipa_uploader
builder.exec()
```

2. 打包->上传到fir->上传符号表到友盟

```
builder.next                = ipa_uploader
ipa_uploader.next           = symbol_uploader
builder.exec()
```

3. 打包->上传到fir->上传符号表到友盟->生成更新信息->上传更新信息到七牛云

```
builder.next                = ipa_uploader
ipa_uploader.next           = symbol_uploader
symbol_uploader.next        = update_info_builder
update_info_builder.next    = qiniu_uploader

builder.exec()
```





# 扩展

你可以任意新增一个类，在链表的任意环节插入或者替换一个节点，完成功能的扩展或者自定义。





# 更新

`update_apple_build_system`

