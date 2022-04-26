from tkinter import *
from tkinter import messagebox


def verifyNewName(newName, profile):
    # Verify name
    if newName.count(";") != 0 or newName.count(" ") == len(newName):
        return messagebox.showerror(
            title="Warning", message="Name is invalid!\n(Avoid using ';' as character).")
    if newName == profile:
        return messagebox.showerror(
            title="Warning", message="New Profile Name is the same as the current one!")
    return True


def saveNewProfileName(newName, currentName):
    with open("data.txt", "r", encoding="utf-8") as f:
        newText = ""
        for line in f:
            param = line.split(";")
            if param[0] == currentName:
                param[0] = newName
            newText = newText + ";".join(param)
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(newText)


def deleteProfile(profile):
    with open("data.txt", "r", encoding="utf-8") as f:
        newText = ""
        for line in f:
            param = line.split(";")
            if param[0] == profile:
                param = ""
            newText = newText + ";".join(param)
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(newText)
