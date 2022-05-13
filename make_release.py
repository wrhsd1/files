import os
import re

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from settings import DEBUG, PATCH_FOLDER, LANG, TRANS_RELEASE_FOLDER, USE_PROXY, PROXIES, VERSION_INFO_OVERRIDE, \
    force_version_info_full, VERSION_INFO_OVERRIDE_BETA, force_version_info_full_beta

# disable warning if we use proxy
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

COMPRESS_TOOL = '7z'

COMPRESS_LEVEL = 9

REPO_NAME = 'zadam/trilium'
TRANS_RELEASE_FOLDER = '/workdir/trilium-trans-release/'
TRANS_RELEASE_FOLDER_MAC = '/workdir/trilium-trans-release/mac'
PATCH_FOLDER = '/workdir/trilium-trans-patch/'
BASE_FOLDER = '/workdir/trilium-trans/'
VERSION_INFO_OVERRIDE = False
VERSION_INFO_OVERRIDE_BETA = False
DO_DOWNLOAD = False

# 是否删除临时文件
# whether delete template files
DO_DELETE = False


# DO_DELETE = False


def decompress_package(file_name):
    print(f'decompress {file_name}')
    if file_name.endswith('tar.xz'):
        try:
            os.system(f'xz -d {file_name}')
        except:
            pass
        try:
            os.system(f'tar -xf {file_name[:-3]}')
            if DO_DELETE:
                os.system(f'rm -f {file_name[:-3]}')
        except:
            pass
    elif file_name.endswith('.zip'):
        try:
            os.system(f'unzip -o {file_name}')

            if DO_DELETE:
                os.system(f'rm -f {file_name}')
        except:
            pass




def patch_mac(file_name):
    if not file_name.endswith('.zip'):
        print('windows 文件名有问题')
        exit()

    file_path = TRANS_RELEASE_FOLDER_MAC + file_name
    print('file_path', file_path)
    decompress_package(file_path)

    asar_folder = TRANS_RELEASE_FOLDER_MAC + 'trilium-mac-x64/Trilium Notes.app/Contents/Resources'
    asar_path = asar_folder + '/app.asar'
    print(asar_path)

    # asar解包
    # asar unpack
    os.chdir(asar_folder)
    os.system('asar extract app.asar ./app/')

    # 打补丁
    # apply patch
    os.system(f'cp -rf {PATCH_FOLDER}* "{asar_folder}/app/"')

    # asar封包
    # asar pack
    os.system('asar pack app/ app.asar')

    # 删除解包文件
    # remove unpacked files
    cmd = f'rm -rf "{asar_folder}/app/"'
    print('cmd', cmd)
    os.system(cmd)

    # 打zip包
    # make zip package
    new_name = f'trilium-{LANG}-mac-x64.zip'
    print('new_name', new_name)
    os.system(f'rm -f {new_name}')
    patched_root_folder = 'trilium-mac-x64'
    os.chdir(TRANS_RELEASE_FOLDER_MAC)
    if COMPRESS_TOOL == '7z':
        cmd = f'7z a {new_name} -r {patched_root_folder}'
    else:
        cmd = f'zip -{COMPRESS_LEVEL} -r {new_name} {patched_root_folder}'
    print('压缩命令', cmd)
    os.system(cmd)

    if DO_DELETE:
        os.system('rm -rf trilium-mac-x64')

    return new_name


list_data=os.listdir(TRANS_RELEASE_FOLDER_MAC) 
for fmac in list_data:
       # 打补丁
    # patch

    # linux
    patch_mac(fmac)

    
