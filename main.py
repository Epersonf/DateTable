import os
import time
from folder_management import get_files
from create_table import generate_table
from image_date import extract_image_date

inputPath = input("Type the input folder path:\n")
outputPath = input("Type the output folder path:\n")
if not outputPath.endswith("/"):
    outputPath += "/"

matrix = [
    [
        "Creation Date",
        "File Name"
    ]
]

for file in get_files(inputPath):
    try:
        print("Reading file", file, "...")
        date = extract_image_date(inputPath, file)
        matrix.append([str(date), str(file)])
        print("File read successfully...\n")
    except:
        print("Error reading", file, "...")

generate_table(outputPath + "Table.xlsx", matrix)

input("Press enter to continue...")
