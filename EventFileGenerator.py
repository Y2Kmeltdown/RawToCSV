import pathlib
import subprocess
import tkinter

from tkinter import filedialog

# Copy Path to raw_to_dat Converter from the metavision toolbox installation and make sure there is double slashes between all directories e.g. "C:\Program Files" => "C:\\Program Files"
rawToDat = "C:\\Program Files\\Prophesee\\bin\\metavision_file_to_dat.exe"
# Copy Path to dat_to_es Converter from Alex's command line tools and make sure there is double slashes between all directories e.g. "C:\Program Files" => "C:\\Program Files"
DatToEs = "C:\\Users\\Path\\To\\DatToESConverter"
# Copy Path to es_to_csv Converter from Alex's command line tools and make sure there is double slashes between all directories e.g. "C:\Program Files" => "C:\\Program Files"
EsToCSV = "C:\\Users\\Path\\To\\EsToCSVConverter"


tkinter.Tk().withdraw()
files = filedialog.askopenfilenames()
for file in files:

    filePath = pathlib.Path(file)
    if filePath.suffix != ".raw":
        raise Exception(f"Program only accepts .raw File input. {filePath.name} was provided")
    datFile = pathlib.Path(file[:-4]+"_cd.dat")
    esFile = pathlib.Path(file[:-4]+".es")
    csvFile = pathlib.Path(file[:-4]+".csv")
    folderPath = filePath.parent

    cmd = '\"'+rawToDat+'\"'+" -i "+ '\"'+file+'\"'
    subprocess.run(cmd)
    print(f"Converted {filePath.name} to {datFile.name}")

    cmd = '\"'+DatToEs+'\"'+" "+ '\"'+str(datFile)+'\"' +" none "+"\""+str(esFile)+"\""
    subprocess.run(cmd)
    print(f"Converted {datFile.name} to {esFile.name}")

    cmd = '\"'+EsToCSV+'\"'+" "+'\"'+str(esFile)+'\"'+' '+"\""+str(csvFile)+"\"" 
    subprocess.run(cmd)
    print(f"Converted {esFile.name} to {csvFile.name}")

                    
                
