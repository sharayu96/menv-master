import os

x = input('Enter free form PDB_ID: ')
y = input('Enter bound form PDB_ID: ')

m = (x + '.pdb')
n = (y + '.pdb')

r = "a.pdb"
s = "b.pdb"

os.rename(m ,r)
os.rename(n ,s)
