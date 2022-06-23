from pathlib import Path
import os
import shutil
import sys


def is_valid_argument():
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Invalid Argument Passed! Please See how to run script Below")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        
        print("python copyfiles.py ","C:/path-to-source-folder", "C:/path-to-destination-folder")
        exit()
    

def copyfiles(source_path, destination_path):
    
    source = Path(source_path)
    target = Path(destination_path)

    for source_filename in os.listdir(source):
        if source_filename.endswith(".yaml"):
            # construct path from filename
            source_file_path = os.path.join(source, source_filename)
            shutil.copy(source_file_path, target)
            




def main():
    
    is_valid_argument()
         
    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    copyfiles(source_directory, destination_directory)
    
    print("PROGRAM: SIMPLE FILE COPIER")
    print("AUTHOR: ENGR. PETER GOTEH")
    print("GITHUB: https://github.com/edwardpeter547/filecopier")
    print("\n")

    print("All Files Copied! \n")

    print("Thanks for using this script!!")
    
    

if __name__ == "__main__":
    main()