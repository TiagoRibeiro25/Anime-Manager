def getAnimeInfo(profile):
    totalNumberOfAnimes = 0
    totalNumberOfEp = 0
    totalNumberOfEpWatched = 0

    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            param = line.split(";")
            if param[0] == profile:
                # In case the selected profile has no anime in the list
                if len(param) == 1:
                    return totalNumberOfAnimes, totalNumberOfEp, totalNumberOfEpWatched
                # Calculate total number of animes
                totalNumberOfAnimes = (len(param)-2) / 5
                # Calculate total number of episodes
                i = 2
                while i < len(param):
                    totalNumberOfEp += int(param[i])
                    i += 5
                # Calculate total number of episodes watched
                i = 4
                while i < len(param):
                    totalNumberOfEpWatched += int(param[i])
                    i += 5
                break
    return totalNumberOfAnimes, totalNumberOfEp, totalNumberOfEpWatched


def getAnimeNames(profile):
    animeList = []
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            param = line.split(";")
            if param[0] == profile:
                if len(param) == 1:
                    break
                i = 1
                while i < len(param)-1:
                    animeList.append(param[i])
                    i += 5
                break

    return animeList


def deleteAnime(anime, profile):
    with open("data.txt", "r", encoding="utf-8") as f:
        newText = ""
        for line in f:
            param = line.split(";")
            if param[0] == profile:
                oldParam = param
                param = []
                i = 0
                while i < len(oldParam):
                    if oldParam[i] == anime:
                        i += 5
                    else:
                        param.append(oldParam[i])
                        i += 1
            newText = newText + ";".join(param)
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(newText)


def updateAnimeInfo(anime, profile):
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            param = line.split(";")
            if param[0] == profile:
                i = 1
                while i < len(param)-2:
                    if param[i] == anime:
                        return [param[i], param[i+1], param[i+2], param[i+3], param[i+4]]
                    i += 5


def writeNewAnimeInfo(anime, profile, info):
    # info = [Title, Episodes, Link, Current Episode, TimeStamp]
    newText = ""
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            param = line.split(";")
            if param[0] == profile:
                i = 1
                while i < len(param)-2:
                    if param[i] == anime:
                        param[i] = info[0]  # Title
                        param[i+1] = info[1]  # Episodes
                        param[i+2] = info[2]  # Link
                        param[i+3] = info[3]  # Current Episode
                        param[i+4] = info[4]  # TimeStamp
                        break
                    i += 5
            newText = newText + ";".join(param)
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(newText)
