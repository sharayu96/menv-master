''' THIS PROGRAM WORKS WITH UBUNTU PLATFORM ONLY !''' 

#server to calculate free energy changes
# ΔG calculation based on protein microenvironment changes
# ΔG can currently be computed for two differnt conformations of the same protein. For example, a protein with same sequence but in     alpha helical and beta sheet conformation or a protein in its free form and in its ligand bound form.
# Hence, ensure that the residue numbers and names in two PDB files are matching, otherwise, this calculation will give wrong results
......................................................................................................................

1. Download the necessary libraries:
 a. gfortran
 b. python3 - pandas, numpy 

......................................................................................................................

2. It is required the acivate the executable as follows:
 a. chmod +x /path/psfgen and similarly; 
 b. chmod +x /path/micro_debug_
 
3. compile the following programs using comand line: 
 a. gfortran -O2 -o psfpdb-crd-conv2 psfpdb-crd-conv2.f
 b. gfortran -O2 -o ssbond.exe ssbond-detect.f
 
......................................................................................................................

4. To execute the file run the script4 file (this is a shell script)
5. input to script4 is a file named "list"
list should contain two file names, in PDB format, in two separate lines. For example, 
xxxx.pdb
yyyy.pdb
6. Download and store only two pdb files in the same directory (in case you have more than two PDB files those will be merged together and produce wrong results)
7. preprocessing will be done in next few steps
 a. user has to change the directory names (path), as given in line 14
    subsequently change the directory names in the lines 16, 17, 20, 21, 24, 30 and 34 (of script4) 
    after downloading the files on your local machine
 b. change the directories for the following files:
    psf-pdb-gen-standalone.tcl (line 3), newrenumber.sh (line 10, 34, 70), del_G, temp-psfgen-scripts.tcl (line 8)

.......................................................................................................................
# The ΔG calculations will be printed in 'data.csv' file (raw data containing ΔG values for individual functional groups)
# A separte statement will pop up stating the difference between two conformations of the protein
