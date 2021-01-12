'''
This script can be used to rename the file with a specific extension. The file with the old and new names has to be
provided as a first argument and second argument of the script is the path to the main directory containing the files to
be renamed. If the script can't find the file name in the dictionary created from the sample ID file, then the name of
the file will not be changed.
Author: Riddhika
'''


import sys
from pathlib import Path
import pandas as pd
import subprocess

main_dir = sys.argv[2]
excel_file = sys.argv[1]
sample_id_df = pd.read_csv(excel_file, sep='\t')
#sample_id_df = pd.read_excel(excel_file)

#print(sample_id_df)

reference = dict(sample_id_df.dropna(subset=["Bam_Name","Sample_Name"]).set_index("Bam_Name")["Sample_Name"])

files = Path(main_dir).glob("*")

for file in files:
    new_name = reference.get(file.stem, file.stem )
    print(" ")
    print(file)
    print(" ")
    print(new_name)
    print(" ")
    new_ID = main_dir + "/" + new_name + file.suffix
    print(new_ID)
    print(" ")
    subprocess.Popen(["mv",file,new_ID])

    #file.rename(file.with_name(f"{new_name}{file.suffix}"))

