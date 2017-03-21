#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-
import zipfile
def embed():
    # odsファイルの取得。
    
        
    with zipfile.ZipFile('spam.zip', 'w') as myzip:
        myzip.write('eggs.txt')


if __name__ == "__main__":
    sys.exit(embed())