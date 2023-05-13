#!/bin/python

from requests import get
from subprocess import run
from glob import glob
from os import chdir, makedirs
from os.path import exists
from re import search
from shutil import rmtree



def downloadFile(url, path):
    rmtree(path)
    run(['wget','-P', path, url])

def getVersion():
    res = get('https://github.com/ventoy/Ventoy/releases')
    x = search(r'ventoy-(\d+\.\d+\.\d+)-windows.zip:\s+(\S{64})', res.text)
    return x.group(1)



    
print('---ventoy.py---')
version = getVersion()
path='download/ventoy/'
if not exists(path):
    makedirs(path)
# Watch out: garbage code ahead!
try:
    with open('version/ventoy-version.txt', 'r+') as file:
        if file.read() != version:
            file.truncate(0)
            file.write(version)
            downloadFile(f'https://github.com/ventoy/Ventoy/releases/download/v{version}/ventoy-{version}-windows.zip', path)

except FileNotFoundError:
    with open('version/ventoy-version.txt', 'w') as file:
        file.write(version)
        downloadFile(f'https://github.com/ventoy/Ventoy/releases/download/v{version}/ventoy-{version}-windows.zip', path)