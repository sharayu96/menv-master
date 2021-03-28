# This program reads the 3 letter amino acid code from a file, 
# Each amino acid has a specific Hydrophobicity scale (HA) 
# Fom which delta G can be calculated as: del G = Hscl x delrHpy respective amino acid

import pandas as pd
import numpy as np

HA = {
    "SER" : 0.05,
    "CYS" : 1.15,
    "ILE" : 0.97,
    "LEU" : 0.87,
    "PHE" : 0.85,
    "VAL" : 0.83,
    "TRP" : 0.67,
    "TYR" : 0.6,
    "MET" : 0.54,
    "ALA" : 0.33,
    "PRO" : 0.32,
    "HIS" : 0.25,
    "THR" : 0.21,
    "ARG" : -0.01,
    "GLN" : -0.05,
    "ASN" : -0.07,
    "ASP" : -0.22,
    "GLU" : -0.24,
    "LYS" : -0.4,
    "HSP" : 0.25,
    "GLY" : 0
} 
#Hydrophobicity scale of individual residue
		
df = pd.read_csv('/home/sharayu/Downloads/menv-server-master/1.csv', sep="\t")
df.head()

residue = HA.keys()

rHpy1 = df['rHpy1']
rHpy2 = df['rHpy2']
#rHpy is calculated from menv-server

res = df ['res_name']
num = df ['res_num']

del_rHpy = rHpy1 - rHpy2
# rHpy difference between two different protein structure (PDB ids)

Hscl = np.array([HA[residue] for residue in res])
df ['HA'] = Hscl
#Hscl is hydrophobicity scale for each individual residue

df ['del_G'] = Hscl*del_rHpy
#del_G is free energy

df ['sum'] = np.sum(df['del_G'])
df ['average'] = np.average(df['del_G']) 
df ['standard deviation'] = np.std(df['del_G']) 

df.to_csv('data.csv', index=False)

