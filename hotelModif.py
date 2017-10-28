import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os
from tkinter import scrolledtext as st
from time import strftime

root = tk.Tk()
root.title("Hotel Check-In") # title
root.resizable(0, 0) # if you want it resizeable, just remove this whole line

# create variables to hold string inputs 
firstname_sv = tk.StringVar()
lastname_sv = tk.StringVar()
id_sv = tk.StringVar()
age_sv = tk.StringVar()
phone_sv = tk.StringVar()
checkindate_sv = tk.StringVar()

#create lists for the following items
firstnameList = []
lastnameList = []
idList = []
ageList = []
phoneList = []
checkindateList = []

#function to clear entry fields
def onReset(*event):
    firstname_sv.set("")
    lastname_sv.set("")
    id_sv.set("")
    age_sv.set("")
    phone_sv.set("")
    checkindate_sv.set(strftime('%d.%m.%Y - %I:%M:%S'))

#on submit items are added to list
def onSubmit(*event):
    firstname = firstname_sv.get()
    lastname = lastname_sv.get()
    id = id_sv.get()
    age = age_sv.get()
    phone = phone_sv.get()
    checkindate = checkindate_sv.get()

    if firstname == "" or lastname == "" or id == "" or age == "" or phone == "" or checkindate == "":
        mb.showerror("Fill Up All Fields!", "Ensure all fields are completely filled!")
        return

    if id in idList:
        person = firstnameList[idList.index(id)] + " " + lastnameList[idList.index(id)]
        mb.showerror("Existing ID", "This ID is already taken by {}!".format(person))
        
        return

    # do not overload this function !
    firstnameList.append(firstname)
    lastnameList.append(lastname)
    idList.append(id)
    ageList.append(age+' years')
    phoneList.append('+234'+phone)
    checkindateList.append(checkindate)

    for i in range(len(firstnameList)):
        print(firstnameList[i], lastnameList[i], idList[i], ageList[i], phoneList[i], checkindateList[i])

    print("---------------------------------------------------------------------")


def showCheckin():#show all checked-in customers
    root2 = tk.Tk()
    root2.title("All Users")
    root2.resizable(0, 0)

    tk.Label(root2, text="First name", font="sans-serif 10 bold").grid(row=0, column=0, padx=10, pady=10, sticky='w')
    tk.Label(root2, text="Last name", font="sans-serif 10 bold").grid(row=0, column=1, padx=10, pady=10, sticky='w')
    tk.Label(root2, text="ID", font="sans-serif 10 bold").grid(row=0, column=2, padx=10, pady=10, sticky='w')
    tk.Label(root2, text="Age", font="sans-serif 10 bold").grid(row=0, column=3, padx=10, pady=10, sticky='w')
    tk.Label(root2, text="Phone", font="sans-serif 10 bold").grid(row=0, column=4, padx=10, pady=10, sticky='w')
    tk.Label(root2, text="Check-in date", font="sans-serif 10 bold").grid(row=0, column=5, padx=10, pady=10, sticky='w')

    for i in range(1, len(firstnameList)+1):
        tk.Label(root2, text=firstnameList[i-1]).grid(row=i, column=0, padx=10, pady=10, sticky='w')
        tk.Label(root2, text=lastnameList[i-1]).grid(row=i, column=1, padx=10, pady=10, sticky='w')
        tk.Label(root2, text=idList[i-1]).grid(row=i, column=2, padx=10, pady=10, sticky='w')
        tk.Label(root2, text=ageList[i-1]).grid(row=i, column=3, padx=10, pady=10, sticky='w')
        tk.Label(root2, text=phoneList[i-1]).grid(row=i, column=4, padx=10, pady=10, sticky='w')
        tk.Label(root2, text=checkindateList[i-1]).grid(row=i, column=5, padx=10, pady=10, sticky='w')

    

    # show checkins in the new window
    root2.mainloop()


def createMenu(): # create a menu
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    settingsMenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Settings", menu=settingsMenu)
    settingsMenu.add_command(label="Save to File", command=saveToFile)
    settingsMenu.add_command(label="Clear List", command=clearList)
    settingsMenu.add_separator()
    settingsMenu.add_command(label="Documentary", command=documentary)
    settingsMenu.add_command(label="About", command=about)
    settingsMenu.add_separator()
    settingsMenu.add_command(label="Exit", command=exitWindow)

def LoadFromFile(*event):
    if len(firstnameList) != 0:
        mb.showerror("Failed to load!", "It is only possible to load From a file, when all lists are empty!\nPlease clear all the lists before!")
        return

    path = fd.askopenfilename()

    if path == "":
        return

    fname, fext = os.path.splitext(path)

    if fext != ".txt":
        mb.showerror("Wrong extension!", "This is a wrong extension!\nJust *.txt allowed!")
    else:
        with open(path, 'r') as f:
            content = f.readlines()

        for i in range(len(content)):
            try:
                firstnameG, lastnameG, idG, ageG, phoneG, checkindateG = content[i].split(' ')
            except:
                mb.showerror("Wrong Format!", "This is a wrong Format!\nLine: {}".format(i + 1))
                return

            firstnameList.append(firstnameG)
            lastnameList.append(lastnameG)
            idList.append(idG)
            ageList.append(ageG+' years')
            phoneList.append('+234 '+phoneG)
            checkindateList.append(str(checkindateG).replace('\n', ''))

        mb.showinfo("Imported successfully", "Entries imported successfully!\nYou can view the Entries from check-in list!")

def clearList(*event):
    if len(firstnameList) == 0:
        mb.showerror("Nothing to clear!", "Your Check-in list is already empty!")
        return

    clear = mb.askyesno("Clear Lists", "Are you Sure you want to clear all Check-In Entries?")

    if clear == 1:
        firstnameList.clear()
        lastnameList.clear()
        idList.clear()
        ageList.clear()
        phoneList.clear()
        checkindateList.clear()
        mb.showinfo("Cleared", "Lists cleared successfully!")

def documentary(*event):
    rootDocumentary = tk.Tk()
    rootDocumentary.title("Documentary")
    rootDocumentary.geometry("528x297")
    rootDocumentary.resizable(0, 0)

    documentaryText = "hi"

    paper = st.ScrolledText(rootDocumentary, width=400, height=200, font=("Consolas", 11))
    paper.insert("1.0", documentaryText)
    paper.configure(state='disabled')
    paper.pack()

    rootDocumentary.mainloop()

def about(*event):
    rootAbout = tk.Tk()
    rootAbout.title("About the developers")
    rootAbout.geometry("528x297")
    rootAbout.resizable(0, 0)

    aboutText = cen(8)+"=====Hotel Check-In Software=====\nCo-Developed by a Nigerian and an Austrian\nFor more Information:\nMail princekelvin91@gmail.com\nCopyright 2017"

    paper = st.ScrolledText(rootAbout, width=400, height=200, font=("Consolas", 11))
    paper.insert("1.0", aboutText)
    paper.configure(state='disabled')
    paper.pack()

    rootAbout.mainloop()    

def exitWindow(*event):
    root.destroy()

def cen(x):
    y = " " * x
    return y

def saveToFile(*event):
    if len(firstnameList) == 0:
        mb.showerror("Nothing to store!", "Nothing to store!\nYour check-in list is already empty!")
        return

    path = fd.asksaveasfilename()

    if path == "":
        return

    fname, fext = os.path.splitext(path)

    if fext != ".txt":
        mb.showerror("Wrong extension!", "This is a wrong extension!\nSave it as *.txt!")
    else:
        with open(path, 'w') as f:
            for i in range(len(firstnameList)):
                f.write("{} ".format(firstnameList[i]))
                f.write("{} ".format(lastnameList[i]))
                f.write("{} ".format(idList[i]))
                f.write("{} ".format(ageList[i]))
                f.write("{} ".format(phoneList[i]))
                f.write("{}\n".format(checkindateList[i]))

       






# add the gui to the window
firstnamelabel = tk.Label(root, text="First Name: ").grid(row=0, column=0, padx=10, pady=10, sticky='w')
firstnameentry = tk.Entry(root, textvariable=firstname_sv).grid(row=0, column=1, padx=10, pady=1-0)

lastnamelabel = tk.Label(root, text="Last Name: ").grid(row=1, column=0, padx=10, pady=10, sticky='w')
lastnameentry = tk.Entry(root, textvariable=lastname_sv).grid(row=1, column=1, padx=10, pady=10)

idlabel = tk.Label(root, text="ID: ").grid(row=2, column=0, padx=10, pady=10, sticky='w')
identry = tk.Entry(root, textvariable=id_sv).grid(row=2, column=1, padx=10, pady=10)

agelabel = tk.Label(root, text="Age: ").grid(row=3, column=0, padx=10, pady=10, sticky='w')
ageentry = tk.Entry(root, textvariable=age_sv).grid(row=3, column=1, padx=10, pady=10)

phonelabel = tk.Label(root, text="Phone: ").grid(row=4, column=0, padx=10, pady=10, sticky='w')
phoneentry = tk.Entry(root, textvariable=phone_sv).grid(row=4, column=1, padx=10, pady=10)

checkindatelabel = tk.Label(root, text="Date of Check-in: ").grid(row=5, column=0, padx=10, pady=10, sticky='w')
checkindateentry = tk.Entry(root, textvariable=checkindate_sv, state="readonly").grid(row=5, column=1, padx=10, pady=10)
checkindate_sv.set(strftime('%d.%m.%Y - %H:%M:%S'))

chooseButton = tk.Button(root, text="Load From File...", command=LoadFromFile).grid(row=6, column=0, padx=10, pady=10, sticky='w')
ShowAllUsersButton= tk.Button(root, text="Show All Check-Ins", command=showCheckin).grid(row=6, column=1, padx=10, pady=10, sticky='w')
resetbutton = tk.Button(root, text="Reset", command=onReset).grid(row=6, column=2, padx=10, pady=10, sticky='e')
submitbutton = tk.Button(root, text="Submit", command=onSubmit).grid(row=6, column=3, padx=10, pady=10, sticky='w')

# bind and build
createMenu()
root.mainloop()
 
