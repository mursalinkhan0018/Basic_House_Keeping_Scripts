#! usrbinenv python3

import os
import pandas as pd
import glob

# Set the working directory (optional)
#os.chdir('/mnt/e/Basic_House_Keeping_Scripts')
#os.chdir('/mnt/e/Two_Species_Analysis_10_Reads/dmel_only/Final_mel_data_files')
os.chdir('/mnt/e/Two_Species_Analysis_10_Reads/dsim_only/Final_sim_data_files')

# Loop through all files ending with 1135.txt
for txt_file in glob.glob("*11505.txt"):
    # Define new filename with .csv extension
    csv_file = txt_file.replace(".txt", ".csv")

    # Read the text file assuming it's tab- or comma-separated
    try:
        df = pd.read_csv(txt_file, sep=None, engine='python')  # Automatically detect delimiter
        df.to_csv(csv_file, index=False)
        print(f"Converted: {txt_file} → {csv_file}")
    except Exception as e:
        print(f"Failed to convert {txt_file}: {e}")
