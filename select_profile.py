from tkinter import *
from tkinter import messagebox
import webbrowser


# ? Functions

def getUserNames():
    Users = []
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            param = line.split(";")
            Users.append(param[0])
    return Users


def createDropDownMenu():
    global clicked
    clicked = StringVar()
    clicked.set(getUserNames()[0])
    drop = OptionMenu(window, clicked, *getUserNames())
    drop.config(bg="green", fg="white")
    drop["menu"].config(bg="medium aquamarine")
    drop["highlightthickness"] = 0
    drop.place(relx=0.5, rely=0.25, anchor="center")


def addUserName():
    newUser = addUserEntry.get()
    if verifyUserName(newUser) != True:
        return
    else:
        with open("data.txt", "a", encoding="utf-8") as f:
            f.write(newUser + ";" + "Anime Title" + ";" + "0" + ";" +
                    "Link" + ";" + "0" + ";" + "0:00" + ";" + "\n")
        # update dropdown menu
        createDropDownMenu()


def verifyUserName(username):
    Users = getUserNames()
    for i in range(len(Users)):
        if username == Users[i]:
            return messagebox.showerror(
                title="Warning", message="Username already exists!")
    if username.count(";") != 0 or username.count(' ') == len(username):
        return messagebox.showerror(
            title="Warning", message="Username is invalid!\n(Avoid using ';' as character).")
    return True


def startApp():
    import app
    profileSelected = clicked.get()
    window.destroy()
    app.main_app(profileSelected, "black")


def gitHubLink():
    webbrowser.open_new_tab("https://github.com/TiagoRibeiro25/Anime-Manager")


# ? Create start window
window = Tk()
window.geometry("250x350")
window.minsize(250, 350)
window.configure(background="black")
window.title("App - Select a Profile")

# ? Widgets inside start window

# Choose User Profile
titleLabel = Label(window, text="Select your Profile", font=(
    "Arial", 15), fg="#00F200", background="black")
titleLabel.place(relx=0.5, rely=0.10, anchor="center")
createDropDownMenu()

# Start Button
startBtn = Button(window, text="    START    ", fg="black", font=("Arial", 13),
                  relief="raised", background="#00F200", command=startApp)
startBtn.place(relx=0.5, rely=0.4, anchor="center")

# Create new User Profile
addUserLabel = Label(window, text="Create new Profile", font=(
    "Arial", 15), fg="#00F200", background="black")
addUserLabel.place(relx=0.5, rely=0.60, anchor="center")

addUserEntry = Entry(window, fg="white", background="green",
                     font=("Arial", 13), justify="center")
addUserEntry.place(relx=0.5, rely=0.70, anchor="center")

addUserBtn = Button(window, text="Add username", fg="white",
                    relief="raised", background="green", command=addUserName)
addUserBtn.place(relx=0.5, rely=0.82, anchor="center")

# Git Hub Page link button
gitHubBtn = Button(
    window, text="GitHub Page", fg="#00F200", relief="flat", background="black", command=gitHubLink)
gitHubBtn.place(relx=0.0, rely=1.0, anchor="sw")


window.mainloop()
