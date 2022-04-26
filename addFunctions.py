from tkinter import *
from tkinter import messagebox


def verifyNewAnime(profile, newName, newTotalEp, newLink):
    # Verify name
    if newName.count(";") != 0 or newName.count(" ") == len(newName):
        return messagebox.showerror(
            title="Warning", message="Name is invalid!\n(Avoid using ';' as character).")

    # verify if it's already in the list
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            param = line.split(";")
            if param[0] == profile:
                i = 1
                while i < len(param):
                    if param[i] == newName:
                        return messagebox.showerror(
                            title="Warning", message="This anime is already on the list.")
                    else:
                        i += 5

    # Verify amount of episodes
    if newTotalEp.count(";") != 0 or newTotalEp.count(" ") == len(newTotalEp) or newTotalEp.isdecimal() == False or newTotalEp == "0":
        return messagebox.showerror(
            title="Warning", message="Invalid amount of Episodes!")

    # Verify Link
    if newLink.count(";") != 0 or newLink.count(" ") == len(newLink):
        return messagebox.showerror(
            title="Warning", message="Invalid Link!")
    verify = 0
    if newLink.count("https:") != 0:
        verify = 1
    elif newLink.count("www.") != 0:
        # If it has "https:" and "www." (it's very likely not to be a valid link)
        if verify == 1:
            return messagebox.showerror(
                title="Warning", message="Invalid Link!")
        verify = 1
    else:
        return messagebox.showerror(
            title="Warning", message="Invalid Link!")

    # If the function reached this far (didn't return anything), it means all the input data is valid
    # (so let's return a True so the main app can know the data is valid)
    return True


def saveNewAnime(profile, newName, newTotalEp, newLink):
    newText = ""
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            param = line.split(";")
            if param[0] == profile:
                param[len(param)-1] = newName + ";" + \
                    newTotalEp + ";" + newLink + ";0;0:00;\n"
            newText = newText + ";".join(param)
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(newText)
