import tkinter as tkinter
from tkinter import filedialog
from tkinter import messagebox
from folder_management import get_files
from create_table import generate_table
from image_date import extract_image_date


def create_gui():
    top = tkinter.Tk()
    top.title("DateTable")
    top.geometry("250x250+0+0")

    # Code to add widgets will go here...
    label_input = tkinter.Label(text="Null")
    label_input.grid(row=0, column=5)
    tkinter.Button(text="Browse input", command=lambda: browse_directory(label_input)).grid(row=0, column=0)

    label_output = tkinter.Label(text="Null")
    label_output.grid(row=1, column=5)
    tkinter.Button(text="Browse output", command=lambda: browse_directory(label_output)).grid(row=1, column=0)

    tkinter.Button(text="Run",
                   command=lambda: run(label_input["text"], label_output["text"])).grid(row=3, column=0)
    # Code to add widgets will go here...
    top.mainloop()


def browse_directory(label):
    path = filedialog.askdirectory()
    if path == "":
        return None
    label.config(text=path)
    return path


def run(input_path, output_path):
    if input_path == "Null" or output_path == "Null":
        messagebox.showinfo("Error", "Invalid paths")
        return
    if not output_path.endswith("/"):
        output_path += "/"

    matrix = [
        [
            "Creation Date",
            "File Name"
        ]
    ]

    error_files = []
    for file in get_files(input_path):
        try:
            date = extract_image_date(input_path, file)
            matrix.append([str(date), str(file)])
        except:
            error_files.append(str(file))

    generate_table(output_path + "Table.xlsx", matrix)
    messagebox.showinfo("Success", "Table generated at output folder.\nErrors:" + str(len(error_files)) + "\nFiles: " + str(error_files)[1:-1])
