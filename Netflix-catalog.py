import tkinter as tk
import pandas
from tkinter import font
from tkinter import messagebox
from googlesearch import *
import webbrowser
df = pandas.read_csv('/Users/victorroa/PycharmProjects/Final Project/venv/include/netflix_titles.csv')

def randommovie():
    rmovie = df.sample()
    getname = rmovie['title'].values[0]
    getyear = rmovie['release_year'].values[0]
    getgenre = rmovie['listed_in'].values[0]
    getinfo = rmovie['description'].values[0]
    getcat = rmovie['type'].values[0]
    getID = rmovie['show_id'].values[0]
    entry.delete(0, tk.END)
    entry.insert(0, getID)
    entry1.delete(0, tk.END)
    entry1.insert(0, getname)
    entry2.delete(0, tk.END)
    entry2.insert(0, getyear)
    entry3.delete(0, tk.END)
    entry3.insert(0, getgenre)
    entry5.delete(0, tk.END)
    entry5.insert(0, getcat)
    entry4.delete('1.0', tk.END)
    entry4.insert(tk.END, getinfo)

def searchmovie():
    searchid = entry.get()
    if searchid.isdigit():
        test1 = int(searchid)
        data = df.loc[df['show_id'] == test1]
        if len(data) > 0:
            getname = data['title'].values[0]
            getyear = data['release_year'].values[0]
            getgenre = data['listed_in'].values[0]
            getinfo = data['description'].values[0]
            getcat = data['type'].values[0]
            getID = data['show_id'].values[0]
            entry.delete(0, tk.END)
            entry.insert(0, getID)
            entry1.delete(0, tk.END)
            entry1.insert(0, getname)
            entry2.delete(0, tk.END)
            entry2.insert(0, getyear)
            entry3.delete(0, tk.END)
            entry3.insert(0, getgenre)
            entry5.delete(0, tk.END)
            entry5.insert(0, getcat)
            entry4.delete('1.0', tk.END)
            entry4.insert(tk.END, getinfo)
        else:
            messagebox.showwarning('Not Found', 'Record not found. Please insert a valid Show ID')

    else:
        messagebox.showwarning('Not Found', 'Record not found. Please insert a valid Show ID')

def nextmovie():
    searchid = entry.get()
    if searchid.isdigit():
        test1 = int(searchid)
        data = df.loc[df['show_id'] == test1]
        if len(data) > 0:
            if searchid == "70153404":
                messagebox.showwarning('Error', 'This is the last record.')
            else:
                data2 = int(df[df['show_id'] == test1].index.item())
                new_index = data2+1
                print(new_index)
                getname = df.loc[new_index, 'title']
                entry1.delete(0, tk.END)
                entry1.insert(0, getname)
                getyear = df.loc[new_index, 'release_year']
                entry2.delete(0, tk.END)
                entry2.insert(0, getyear)
                getgenre = df.loc[new_index, 'listed_in']
                entry3.delete(0, tk.END)
                entry3.insert(0, getgenre)
                getinfo = df.loc[new_index, 'description']
                entry4.delete('1.0', tk.END)
                entry4.insert(tk.END, getinfo)
                getcat = df.loc[new_index, 'type']
                entry5.delete(0, tk.END)
                entry5.insert(0, getcat)
                getID = df.loc[new_index, 'show_id']
                entry.delete(0, tk.END)
                entry.insert(0, getID)

        else:
            messagebox.showwarning('Error', 'Record not found. Please insert a valid Show ID or leave it in blank')
    elif searchid == "":
        getname = df.loc[0, 'title']
        entry1.delete(0, tk.END)
        entry1.insert(0, getname)
        getyear = df.loc[0,'release_year']
        entry2.delete(0, tk.END)
        entry2.insert(0,getyear)
        getgenre = df.loc[0 ,'listed_in']
        entry3.delete(0, tk.END)
        entry3.insert(0, getgenre)
        getcat = df.loc[0, 'type']
        entry5.delete(0, tk.END)
        entry5.insert(0, getcat)
        getID = df.loc[0, 'show_id']
        entry.delete(0, tk.END)
        entry.insert(0, getID)
        getinfo = df.loc[0, 'description']
        entry4.delete('1.0', tk.END)
        entry4.insert(tk.END, getinfo)
    else:
        messagebox.showwarning('Error', 'Record not found. Please insert a valid Show ID or leave it in blank')

def prevmovie():
    searchid = entry.get()
    if searchid.isdigit():
        test1 = int(searchid)
        data = df.loc[df['show_id'] == test1]
        if len(data) > 0:
            if searchid == "81145628":
                messagebox.showwarning('Error', 'This is the first record.')
            else:
                data2 = int(df[df['show_id'] == test1].index.item())
                new_index = data2-1
                print(new_index)
                getname = df.loc[new_index, 'title']
                entry1.delete(0, tk.END)
                entry1.insert(0, getname)
                getyear = df.loc[new_index, 'release_year']
                entry2.delete(0, tk.END)
                entry2.insert(0, getyear)
                getgenre = df.loc[new_index, 'listed_in']
                entry3.delete(0, tk.END)
                entry3.insert(0, getgenre)
                getinfo = df.loc[new_index, 'description']
                entry4.delete('1.0', tk.END)
                entry4.insert(tk.END, getinfo)
                getcat = df.loc[new_index, 'type']
                entry5.delete(0, tk.END)
                entry5.insert(0, getcat)
                getID = df.loc[new_index, 'show_id']
                entry.delete(0, tk.END)
                entry.insert(0, getID)
        else:
            messagebox.showwarning('Error', 'Record not found. Please insert a valid Show ID or leave it in blank')
    elif searchid == "":
        messagebox.showwarning('Error', 'No record')
    else:
        messagebox.showwarning('Error', 'Record not found. Please insert a valid Show ID or leave it in blank')

def searchgoogle():
    query = entry1.get()
    webbrowser.open("https://google.com/search?q=%s" % query)


app = tk.Tk()
HEIGHT = 600
WIDTH = 800
arial = font.Font(family='Arial', size=18)
arialbold = font.Font(family='Arial', size=18, weight='bold')
canvas = tk.Canvas(app, height=HEIGHT, width=WIDTH, bg='#E50914')
canvas.pack()

frame = tk.Frame(app, bg='black')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

entry = tk.Entry(frame, bg='gray', fg='white', font=arial)
entry.place(relx=0.10, rely=0.10, relheight=0.1, relwidth=0.4)
entry1 = tk.Entry(frame, bg='gray', fg='white', font=arial)
entry1.place(relx=0.12, rely=0.38, relheight=0.06, relwidth=0.4)
entry2 = tk.Entry(frame, bg='gray', fg='white', font=arial)
entry2.place(relx=0.12, rely=0.45, relheight=0.06, relwidth=0.4)
entry3 = tk.Entry(frame, bg='gray', fg='white', font=arial)
entry3.place(relx=0.12, rely=0.52, relheight=0.06, relwidth=0.4)
entry4 = tk.Text(frame, bg='gray', fg='white', font=arial)
entry4.place(relx=0.12, rely=0.59, relheight=0.38, relwidth=0.4)
entry5 = tk.Entry(frame, bg='gray', fg='white', font=arial)
entry5.place(relx=0.7, rely=0.45, relheight=0.06, relwidth=0.25)

button = tk.Button(frame, text="Search a movie", bg="gray", fg="red", font=arialbold,
                   command=searchmovie)
button.place(relx=0.50, rely=0.10, relheight=0.1, relwidth=0.4)
button1 = tk.Button(frame, text="Random Movie/TV Show!", bg="gray", fg="red", font=arialbold, command=randommovie)
button1.place(relx=0.1, rely=0.22, relheight=0.1, relwidth=0.4)
button2 = tk.Button(frame, text="Previous Show", bg="gray", fg="red", font=arialbold, command= prevmovie)
button2.place(relx=0.7, rely=0.68, relheight=0.1, relwidth=0.25)
button3 = tk.Button(frame, text="Next Show", bg="gray", fg="red", font=arialbold, command = nextmovie)
button3.place(relx=0.7, rely=0.57, relheight=0.1, relwidth=0.25)
button4 = tk.Button(frame, text="Search in Google", bg="gray", fg="red", font=arialbold,
                   command = searchgoogle)
button4.place(relx=0.50, rely=0.22, relheight=0.1, relwidth=0.4)
label1 = tk.Label(frame, text="Name:", bg='black', fg='#E50914', font=arial)
label1.place(relx=0.00005, rely=0.38, relheight=0.06, relwidth=0.1)
label2 = tk.Label(frame, text="Year:", bg='black', fg='#E50914', font=arial)
label2.place(relx=0.00005, rely=0.45, relheight=0.06, relwidth=0.1)
label3 = tk.Label(frame, text="Genre:", bg='black', fg='#E50914', font=arial)
label3.place(relx=0.00005, rely=0.52, relheight=0.06, relwidth=0.1)
label4 = tk.Label(frame, text="Info:", bg='black', fg='#E50914', font=arial)
label4.place(relx=0.00005, rely=0.59, relheight=0.06, relwidth=0.1)
logo = tk.PhotoImage(file='/Users/victorroa/PycharmProjects/Final Project/venv/include/netflix-logo.png')
label5 = tk.Label(frame, image=logo, )
label5.place(relx=0.67, rely=0.82, relheight=0.16, relwidth=0.3)
label6 = tk.Label(frame, text="Category:", bg='black', fg='#E50914', font=arial)
label6.place(relx=0.61, rely=0.38, relheight=0.06, relwidth=0.3)
app.mainloop()
