from tkinter import *
from tkinter import messagebox
import addFunctions
import infoFunctions
import listFunctions


def main_app(profile, color):

    # Functions
    def back():
        window.destroy()
        import select_profile

    def animeListInfo():
        info = listFunctions.getAnimeInfo(profile)

        listTotalAnimesInfoLbl.configure(text=int(info[0]))
        listTotalEpisodesInfoLbl.configure(text=int(info[1]))
        listTotalEpisodesWatchedInfoLbl.configure(text=int(info[2]))

    def addNewAnime():
        newName = addNameEntry.get()
        newTotalEp = addTotalEpisodesEntry.get()
        newLink = addLinkEntry.get()

        if addFunctions.verifyNewAnime(profile, newName, newTotalEp, newLink) != True:
            addSuccessLabel.configure(fg="black")  # Hides the Label
            return

        addFunctions.saveNewAnime(profile, newName, newTotalEp, newLink)
        addSuccessLabel.configure(fg="#00F200")  # Shows the label

        # Resets the window
        window.destroy()
        main_app(profile, "black")  # shows the label

    def changeName():
        infoSuccessLabel.configure(fg="black")  # Hides the Label
        newName = infoChangeProfileNameEntry.get()

        if infoFunctions.verifyNewName(newName, profile) != True:
            return

        infoFunctions.saveNewProfileName(newName, profile)
        profileSelected.configure(text=newName)

        # Resets the window
        window.destroy()
        main_app(newName, "#00F200")  # shows the label

    def deleteProfile():
        MsgBox = messagebox.askquestion(
            'Delete Profile', 'Are you sure you want to delete this profile?', icon='question')
        if MsgBox != 'yes':
            return
        infoFunctions.deleteProfile(profile)

    def deleteSelectedAnime():
        animeSelected = listClicked.get()
        listFunctions.deleteAnime(animeSelected, profile)
        window.destroy()
        main_app(profile, "black")

    def setEditAnimeInfo():
        listEditAnimeSuccessLbl.configure(fg="#181A1B")
        animeSelected = listClicked.get()

        # Clear input boxes
        listEditAnimeNameEntry.delete(0, END)
        listEditAnimeEpEntry.delete(0, END)
        listEditAnimeCurrentEpEntry.delete(0, END)
        listEditAnimeTimeStampEntry.delete(0, END)
        listEditAnimeLinkEntry.delete(0, END)

        # Get Anime Info
        # array = [Title, Episodes, Link, Current Ep, TimeStamp]
        animeInfo = listFunctions.updateAnimeInfo(animeSelected, profile)

        # Insert Anime Info in the input boxes
        listEditAnimeNameEntry.insert(0, animeInfo[0])
        listEditAnimeEpEntry.insert(0, animeInfo[1])
        listEditAnimeCurrentEpEntry.insert(0, animeInfo[3])
        listEditAnimeTimeStampEntry.insert(0, animeInfo[4])
        listEditAnimeLinkEntry.insert(0, animeInfo[2])

    def editAnimeInfo():

        animeSelected = listClicked.get()  # Name

        animeTitle = listEditAnimeNameEntry.get()  # Title
        animeEps = listEditAnimeEpEntry.get()  # Episodes
        animeLink = listEditAnimeLinkEntry.get()  # Link
        animeCurrentEp = listEditAnimeCurrentEpEntry.get()  # Current Episode
        animeTimeStamp = listEditAnimeTimeStampEntry.get()  # TimeStamp

        info = [animeTitle, animeEps, animeLink,
                animeCurrentEp, animeTimeStamp]

        listFunctions.writeNewAnimeInfo(animeSelected, profile, info)
        listEditAnimeSuccessLbl.configure(fg="#00F200")

    # ?_______________________________________________________________________________________

    # Create Main window
    window = Tk()
    window.geometry("1020x768")
    window.minsize(1020, 768)
    window.configure(background="#1C1E1F")
    window.title("App")

    # Profile Selected (centered title)
    profileSelected = Label(window, text=profile, font=(
        "Arial", 27), fg="#00F200", background="#1C1E1F")
    profileSelected.place(relx=0.50, rely=0.055, anchor="center")

    # Back button
    backBtn = Button(window, text="<< Back", font=("Arial", 19),
                     fg="#00F200", background="#1C1E1F", relief="flat", command=back)
    backBtn.place(relx=0.10, rely=0.056, anchor="center")

    # Down Alert
    warningText = "In the current state, you need to have at least 1 anime on your profile for the app to work properly. Do not run the app with a profile with 0 animes.\nWhen creating a new profile, the app will automatically create an Anime, which you can edit."
    profileSelected = Label(window, text=warningText, font=(
        "Arial", 10), fg="#00F200", background="#1C1E1F")
    profileSelected.place(relx=0.50, rely=0.95, anchor="center")

    # ?_______________________________________________________________________________________

    # ?List
    # TODO
    listSection = PanedWindow(
        window, width=400, height=608, background="black")
    listSection.place(relx=0.30, rely=0.5, anchor="center")

    listTitleLbl = Label(listSection, text="Anime List", font=("Arial", 15),
                         fg="#00F200", background="black")
    listTitleLbl.place(relx=0.5, rely=0.05, anchor="center")

    # Total Animes Info

    # Total Number of Animes
    listTotalAnimesLbl = Label(listSection, text="Number of animes in the list:", font=("Arial", 13),
                               fg="#00F200", background="black")
    listTotalAnimesLbl.place(x=30, y=90)

    listTotalAnimesInfoLbl = Label(listSection, text="", font=("Arial", 13), width=13,
                                   fg="medium aquamarine", background="black")
    listTotalAnimesInfoLbl.place(x=250, y=90)

    # Total Number of Episodes
    listTotalEpisodesLbl = Label(listSection, text="Total number of episodes:", font=("Arial", 13),
                                 fg="#00F200", background="black")
    listTotalEpisodesLbl.place(x=30, y=120)

    listTotalEpisodesInfoLbl = Label(listSection, text="", font=("Arial", 13), width=13,
                                     fg="medium aquamarine", background="black")
    listTotalEpisodesInfoLbl.place(x=250, y=123)

    # Total Number of Episodes Watched
    listTotalEpisodesWatchedLbl = Label(listSection, text="Total number of episodes\nwatched:", font=("Arial", 13),
                                        fg="#00F200", background="black")
    listTotalEpisodesWatchedLbl.place(x=30, y=150)

    listTotalEpisodesWatchedInfoLbl = Label(listSection, text="", font=("Arial", 13), width=13,
                                            fg="medium aquamarine", background="black")
    listTotalEpisodesWatchedInfoLbl.place(x=250, y=157)

    # Insert the animes info in the labels
    animeListInfo()

    # Edit Anime section
    listSelectAnimeLbl = Label(listSection, text="Select an Anime:", font=("Arial", 13),
                               fg="#00F200", background="black")
    listSelectAnimeLbl.place(x=30, y=220)

    # Dropdown Anime List
    listClicked = StringVar()
    listClicked.set(listFunctions.getAnimeNames(profile)[0])
    listDrop = OptionMenu(listSection, listClicked, *
                          listFunctions.getAnimeNames(profile))
    listDrop.config(bg="green", fg="white", width=30)
    listDrop["menu"].config(bg="medium aquamarine")
    listDrop["highlightthickness"] = 0
    listDrop.place(x=165, y=220)

    # Buttons
    listEditAnimeInfoBtn = Button(listSection, text="Edit Anime Info", fg="white", font=(
        "Arial", 12), relief="flat", background="green", width=15, command=setEditAnimeInfo)
    listEditAnimeInfoBtn.place(relx=0.1, y=270)

    listDeleteAnimeBtn = Button(listSection, text="Delete Anime", fg="white", font=(
        "Arial", 12), relief="flat", background="red", width=15, command=deleteSelectedAnime)
    listDeleteAnimeBtn.place(relx=0.55, y=270)

    # Edit Anime Info Section

    # Box where everything related to Edit section will be in
    listEditAnimeBox = PanedWindow(
        listSection, width=360, height=270, background="#181A1B", borderwidth=2, relief="groove")
    listEditAnimeBox.place(relx=0.50, rely=0.75, anchor="center")

    # Title Name
    listEditAnimeNameLbl = Label(listEditAnimeBox, text="Anime Title:", font=(
        "Arial", 13), fg="#00F200", background="#181A1B")
    listEditAnimeNameLbl.place(x=135, y=7)

    listEditAnimeNameEntry = Entry(listEditAnimeBox, width=36, font=(
        "Arial", 10), fg="medium aquamarine", background="#181A1B", justify="center")
    listEditAnimeNameEntry.place(x=50, y=35)

    # Amount of Episodes
    listEditAnimeEpLbl = Label(listEditAnimeBox, text="Episodes:", font=(
        "Arial", 13), fg="#00F200", background="#181A1B")
    listEditAnimeEpLbl.place(x=92, y=68)

    listEditAnimeEpEntry = Entry(listEditAnimeBox, width=10, font=(
        "Arial", 10), fg="medium aquamarine", background="#181A1B", justify="center")
    listEditAnimeEpEntry.place(x=178, y=69)

    # Current Episode being watched + timestamp
    listEditAnimeCurrentEpLbl = Label(listEditAnimeBox, text="Current Episode:", font=(
        "Arial", 13), fg="#00F200", background="#181A1B")
    listEditAnimeCurrentEpLbl.place(x=40, y=100)

    listEditAnimeCurrentEpEntry = Entry(listEditAnimeBox, width=10, font=(
        "Arial", 10), fg="medium aquamarine", background="#181A1B", justify="center")
    listEditAnimeCurrentEpEntry.place(x=65, y=127)

    listEditAnimeTimeStampLbl = Label(listEditAnimeBox, text="TimeStamp:", font=(
        "Arial", 13), fg="#00F200", background="#181A1B")
    listEditAnimeTimeStampLbl.place(x=210, y=100)

    listEditAnimeTimeStampEntry = Entry(listEditAnimeBox, width=10, font=(
        "Arial", 10), fg="medium aquamarine", background="#181A1B", justify="center")
    listEditAnimeTimeStampEntry.place(x=218, y=127)

    # Link
    listEditAnimeLinkLbl = Label(listEditAnimeBox, text="Link:", font=(
        "Arial", 13), fg="#00F200", background="#181A1B")
    listEditAnimeLinkLbl.place(x=155, y=155)

    listEditAnimeLinkEntry = Entry(listEditAnimeBox, width=36, font=(
        "Arial", 10), fg="medium aquamarine", background="#181A1B", justify="center")
    listEditAnimeLinkEntry.place(x=50, y=185)

    # Edit Button
    ListApplyBtn = Button(listEditAnimeBox, text="  Apply  ",
                          fg="white", font=("Arial", 14), relief="flat", background="green", command=editAnimeInfo)
    ListApplyBtn.place(x=174, rely=0.9, anchor="center")

    # Success alert label (invisible)
    listEditAnimeSuccessLbl = Label(listEditAnimeBox, text="Anime Info\nUpdated!", font=(
        "Arial", 10), fg="#181A1B", background="#181A1B")
    listEditAnimeSuccessLbl.place(x=30, y=220)

    # Insert Anime info in the input boxes
    setEditAnimeInfo()

    # ?_______________________________________________________________________________________

    # ? Info
    infoSection = PanedWindow(
        window, width=400, height=300, background="black")
    infoSection.place(relx=0.70, rely=0.3, anchor="center")

    infoTitleLbl = Label(infoSection, text="Profile Manager", font=("Arial", 15),
                         fg="#00F200", background="black")
    infoTitleLbl.place(relx=0.5, rely=0.1, anchor="center")

    infoChangeProfileNameLbl = Label(infoSection, text="Change Profile Name:", font=(
        "Arial", 13), fg="#00F200", background="black")
    infoChangeProfileNameLbl.place(relx=0.5, rely=0.3, anchor="center")

    infoChangeProfileNameEntry = Entry(infoSection, font=("Arial", 13), width=28,
                                       fg="medium aquamarine", background="black", justify="center")
    infoChangeProfileNameEntry.place(relx=0.5, rely=0.4, anchor="center")

    # Alert label, saying that new Profile Name has been changed (invisible)
    infoSuccessLabel = Label(infoSection, text="Profile Name has been changed", font=(
        "Arial", 11), fg=color, background="black")
    infoSuccessLabel.place(relx=0.5, rely=0.5, anchor="center")

    # Buttons
    infoApplyBtn = Button(infoSection, text="  Change Name  ",
                          fg="white", font=("Arial", 14), relief="flat", background="green", command=changeName)
    infoApplyBtn.place(relx=0.5, rely=0.68, anchor="center")

    infoDelBtn = Button(infoSection, text="  Delete  Profile  ",
                        fg="white", font=("Arial", 14), relief="flat", background="red", command=deleteProfile)
    infoDelBtn.place(relx=0.5013, rely=0.88, anchor="center")

    # ?_______________________________________________________________________________________

    # ? Add
    addSection = PanedWindow(
        window, width=400, height=300, background="black")
    addSection.place(relx=0.70, rely=0.7, anchor="center")

    addTitleLbl = Label(addSection, text="Add new Anime", font=("Arial", 15),
                        fg="#00F200", background="black")
    addTitleLbl.place(relx=0.5, rely=0.1, anchor="center")

    addNameLbl = Label(addSection, text="Name:", font=(
        "Arial", 13), fg="#00F200", background="black")
    addNameLbl.place(x=30, y=70)
    addNameEntry = Entry(addSection, font=("Arial", 13), width=28,
                         fg="medium aquamarine", background="black", justify="center")
    addNameEntry.place(x=100, y=70)

    addTotalEpisodesLbl = Label(addSection, text="Total amount of Episodes:", font=(
        "Arial", 13), fg="#00F200", background="black")
    addTotalEpisodesLbl.place(x=30, y=120)
    addTotalEpisodesEntry = Entry(addSection, font=("Arial", 13), width=12,
                                  fg="mediumaquamarine", background="black", justify="center")
    addTotalEpisodesEntry.place(x=245, y=120)

    addLinkLbl = Label(addSection, text="Link:", font=(
        "Arial", 13), fg="#00F200", background="black")
    addLinkLbl.place(x=30, y=170)
    addLinkEntry = Entry(addSection, font=("Arial", 13), width=29,
                         fg="mediumaquamarine", background="black", justify="center")
    addLinkEntry.place(x=93, y=170)

    addBtn = Button(addSection, text="  Add to List  ",
                    fg="white", font=("Arial", 14), relief="flat", background="green", command=addNewAnime)
    addBtn.place(relx=0.5, rely=0.8, anchor="center")

    # Alert label, saying that the new anime got added to the list (invisible)
    addSuccessLabel = Label(addSection, text="Anime was successfully added to the list.", font=(
        "Arial", 11), fg="black", background="black")
    addSuccessLabel.place(relx=0.5, rely=0.93, anchor="center")

    # ?_______________________________________________________________________________________
    window.mainloop()
