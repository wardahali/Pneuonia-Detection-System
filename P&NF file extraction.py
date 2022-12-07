# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:38:58 2022

@author: Admin
"""

import tarfile
import numpy as np
import pandas as pd
import os
import shutil


df = pd.read_csv(r'D:/University/FYP/dataset/img_able.csv')
df.drop(df.columns[0], axis=1, inplace=True)

path=r"D:/University/FYP/dataset/images_012/images"
#D:\University\FYP\dataset\No Findings\nf
Ptarget=r"D:/University/FYP/dataset/Pneumonia/New folder"
dfarr=np.array(df)
Pcount=0
nfcount=0
arrcount=0
filecount=0

for images,labels in dfarr:
    arrcount+=1
    print(arrcount)
    if labels=="Pneumonia": 
        if os.path.exists(path+"/"+images):
            source=path+"/"+images
            shutil.copy(source, Ptarget)
            Pcount+=1
            print("***************************")
            print(Pcount,"P file copied")
            print(images,labels)
            print("***************************")