# This program reads the 3 letter amino acid code from a file, 
# Each amino acid has a specific Hydrophobicity scale (HA) 
# Fom which ΔG can be calculated as: ΔG = Hscl x delrHpy respective amino acid

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
		
df = pd.read_csv('/home/leucine/Downloads/menv-server-master-main/file.txt', sep="\t")
df.head()

residue = HA.keys()

#rHpy is calculated from menv-server
rHpy1 = df['rHpy1']
rHpy2 = df['rHpy2']

res = df ['res_name']
num = df ['res_num']

# rHpy difference between two different protein structure (PDB ids)
del_rHpy = rHpy2 - rHpy1
df ['del_rHpy'] = del_rHpy

#Hscl is hydrophobicity scale for each individual residue
Hscl = np.array([HA[residue] for residue in res])
df ['HA'] = Hscl

#ΔG is free energy
df ['del_G per residue'] = Hscl*del_rHpy

df.at[0, 'del_G'] = np.sum(df['del_G per residue'])
df.at[0, 'average del_G'] = np.average(df['del_G per residue']) 
df.at[0, 'standard deviation'] = np.std(df['del_G per residue']) 

df.to_csv('data.csv', index=False)

print('ΔG (free energy change is): ', df.at[0, 'del_G'], 'Kcal/mol')
print('Average free energy change is): ', df.at[0, 'average del_G'], 'Kcal/mol')
print('standard deviation is (σ): ', df.at[0, 'standard deviation'])


