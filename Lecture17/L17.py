#!/user/bin/python3
import os,sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

len(df[(df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100)])

for Group in ['Plants','Animals','Fungi','Protists']:
     length = len(df[(df['Group'] == Group)])
     print('There are',length,'genomes has been sequenced in',Group)


hel = df[df.apply(lambda x : x['#Organism/Name'].startswith('Heliconius'), axis=1)]
hel[['#Organism/Name', 'Scaffolds']]

