import pandas as pd
from sklearn import preprocessing
import tkinter as tk
import pickle
from tkinter import filedialog
import csv
from xlsxwriter.workbook import Workbook
import openpyxl
import os
import webbrowser

high = 500
wide = 800
app = tk.Tk()
app.resizable(width=False, height=False)
canvas = tk.Canvas(app, width=wide, height=high)
canvas.pack()
background_image = tk.PhotoImage(file='BG2.png')
background_label = tk.Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
intro_frame = tk.Frame(app, bg='#ba8a8a')
intro_frame.place(relx=0.05, rely=0.01, relwidth=0.9, relheight=0.98)
intro_frame.tkraise()

install_frame = tk.Frame(app, bg='#ba8a8a')
install_frame.place(relx=0.05, rely=0.01, relheight=0.98, relwidth=0.9)

add_data_frame = tk.Frame(app, bg='#ba8a8a')
add_data_frame.place(relx=0.05, rely=0.01, relheight=0.98, relwidth=0.9)

open_result_frame = tk.Frame(app, bg='#ba8a8a')
open_result_frame.place(relx=0.05, rely=0.01, relheight=0.98, relwidth=0.9)

file1 = None
file_name = None

app.title("Car Evaluation")

intro = "                               INTRO\n\n\n"\
    "This application is used to evaluate cars in 4 classes namely,\n"\
    "Unacceptable, Acceptable, Good, Very-Good.\n" \
    "The application uses KNN Algorithm to classify objects.\n"\
    "The added data file should be of the csv format.\n"\
    "Please read the read me file for instructions.\n"\
    "An example data file is given with the program.\n\n"\
    "Click Open File to see the example data file."

var = tk.StringVar()
var.set("Choose the data file")

result_file_loc = os.getcwd() + '/FinalResult.xlsx'

loaded_model = pickle.load(open('knnModel_file', 'rb'))

names = ["unacc", "acc", "good", "vgood"]

ex_data_file = os.getcwd() + '/Ex-Data.txt'


def open_data():
    webbrowser.open_new(ex_data_file)
    

def file_open():
    global file1, file_name
    file1 = tk.filedialog.askopenfile().name
    print(file1)
    file_name = file1.title()
    print(file_name)
    var.set(file1)

    workbook = Workbook('FinalResult.xlsx')
    worksheet = workbook.add_worksheet('Result')
    with open(file1, 'rt', encoding='utf8') as fff:
        reader = csv.reader(fff)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()
    submit['state'] = 'normal'


def submit_file():
    try:
        data = pd.read_csv(file1)

        le = preprocessing.LabelEncoder()
        buying = le.fit_transform(list(data["buying"]))
        maint = le.fit_transform(list(data["maint"]))
        door = le.fit_transform(list(data["door"]))
        persons = le.fit_transform(list(data["persons"]))
        lug_boot = le.fit_transform(list(data["lug_boot"]))
        safety = le.fit_transform(list(data["safety"]))

        x = list(zip(buying, maint, door, persons, lug_boot, safety))

        predicted = loaded_model.predict(x)
        xfile = openpyxl.load_workbook('FinalResult.xlsx')
        sheet = xfile.get_sheet_by_name('Result')
        col = 'G'
        row = 2
        for r in range(len(predicted)):
            cell = col + str(row)
            sheet[cell] = str(names[predicted[r]])
            row += 1
        xfile.save('FinalResult.xlsx')
        xfile.close()
        next_button2['state'] = 'normal'
    except TypeError:
        pass


def open_file_location():
    webbrowser.open_new(result_file_loc)


def to_frame2():
    install_frame.tkraise()


def to_frame3():
    add_data_frame.tkraise()


def back_home():
    intro_frame.tkraise()


def result_frame():
    open_result_frame.tkraise()


def exit():
    app.destroy()


app_intro = tk.Label(intro_frame, text=intro, justify='left', anchor='nw', bg='#ffffff')
app_intro.config(font=("Courier", 14))
app_intro.place(anchor='nw', relx=0.02, rely=0.07, relheight=0.833, relwidth=0.96)
ex_data = tk.Button(intro_frame, text="Open File", command=open_data)
ex_data.place(relx=0.02, rely=0.75, relheight=0.07, relwidth=0.15)
next_button0 = tk.Button(intro_frame, text="Next", command=to_frame3)
next_button0.place(relx=0.8, rely=0.75, relheight=0.07, relwidth=0.15)

add_data = tk.Label(add_data_frame, textvariable=var, justify='left', anchor='nw', bg='#ffffff')
add_data.config(font=("Courier", 12))
add_data.place(anchor='nw', relx=0.02, rely=0.25, relheight=0.07, relwidth=0.72)
browse = tk.Button(add_data_frame, text="Add Data File", command=file_open)
browse.place(relx=0.8, rely=0.25, relheight=0.07, relwidth=0.18)
submit = tk.Button(add_data_frame, text='Submit Data File', command=submit_file, state='disabled')
submit.place(relx=0.8, rely=0.5, relheight=0.07, relwidth=0.18)
next_button2 = tk.Button(add_data_frame, text="Result", command=result_frame, state='disabled')
next_button2.place(relx=0.8, rely=0.75, relheight=0.07, relwidth=0.18)
back_button1 = tk.Button(add_data_frame, text="Back", command=back_home)
back_button1.place(relx=0.02, rely=0.75, relheight=0.07, relwidth=0.15)

file_location = tk.Label(open_result_frame, text=result_file_loc, justify='left', anchor='nw', bg='#ffffff')
file_location.config(font=("Courier", 12))
file_location.place(anchor='nw', relx=0.02, rely=0.2, relheight=0.07, relwidth=0.8)
open_folder = tk.Button(open_result_frame, text='Open Result', command=open_file_location)
open_folder.place(relx=0.85, rely=0.2, relheight=0.07, relwidth=0.15)
back_button2 = tk.Button(open_result_frame, text="EXIT", command=exit)
back_button2.place(relx=0.02, rely=0.75, relheight=0.07, relwidth=0.15)

intro_frame.tkraise()
app.mainloop()
