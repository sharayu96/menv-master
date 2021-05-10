# server to calculate free energy changes
# delG calculation based on protein microenvironment changes
# delG can currently be computed for two differnt conformations of the same protein. For example, a protein with same sequence but in alpha helical and beta sheet conformation or a protein in its free form and in its ligand bound form.
# Hence, ensure that the residue numbers in two PDB files are matching, otherwise, this calculation will give wrong results
......................................................................................................................
1. To execute the file run the script4 file (this is a shell script)
2. input to script4 is a file named "list"
list should contain two file names, in PDB format, in two separate lines. For example, 
xxxx.pdb
yyyy.pdb
3. Download and store only two pdb files in the same directory (in case you have more than two PDB files those will be merged together and produce wrong results)
4. preprocessing will be done in next few steps
a. user has to change the directory names, as given in line 14
subsequently change the directory names in the lines 14, 16, 17, 20, 21, 24, 30 and 34 (of script4) after downloading the files on your local machine
b. change the directories for the following files:
standalone.tcl, newrenumber.sh, del_G, temp-psfgen-scripts.tcl
5. Download the necessary libraries
.......................................................................................................................
6. Once the file directory is changed, it is required the acivate the executable as follows:
chmod +x path/psfgen..; micro_debug_
7. compile the following programs
using comand line: gfortran -O2 -o psfpdb-crd-conv2 psfpdb-crd-conv2.f
similarly, gfortran -O2 -o ssbond.exe ssbond-detect.f
 a. psfpdb-crd-conv2.f
 b. ssbond-detect.f
# The del_G calculations will be printed in 'data.csv' file (raw data containing delG values for individual functional groups)
# A separte statement will pop up stating the difference between two conformations of the protein
