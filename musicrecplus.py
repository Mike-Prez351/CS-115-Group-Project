################################################################################
# Names: Charles Villa, Jun Hong Wang, Michael Preziosi                        #
# Pledge: I pledge my honor that I have abided by the Stevens Honor System     #
# CS 115 - Group Project                                                       #
################################################################################

PREF_FILE = open("musicrecplus.txt", 'a')

def loadUsers(fileName):
    '''Reads in a file of stored users' preferences stored in the file
    fileName. Returns a dictionary containing a mapping of user names to a list
    of preferred artists. Written by Michael.'''
    file = open(fileName, 'r')
    userLikes = {}
    for line in file:
        if ':' in line:
            user, likes = line.split(':', 1)
            likes = likes[:-1]
            if likes == "":
                pass
            else:
                likeList = likes.split(',')
                likeList.sort()
                userLikes[user] = likeList
    file.close()
    if userLikes == {}:
        pass
    return userLikes

def findUser(searchUser, list):
    """
    tries to find a specific username in a list (which comes from a file)
    returns n, which is the line where the username is if it's in the list
    -1 if it isn't
    Jun Hong
    """
    for n in range(len(list)):
        line = list[n]
        username = line.split(":")[0]
        if username == searchUser:
            return n
    return -1

def enterPreferences(user, userDict):
    """
    takes username and list of prefs, writes to file in this syntax:
    username:artist1,artist2,artist3,...
    colon between username and list of artists, commas separating artists
    also takes care of title case
    Jun Hong
    """
    addPrefs = ""
    print(userDict)
    artists = sorted(userDict[user])
    for x in artists:
        addPrefs += x.strip().title() + ","
    addPrefs = addPrefs[:-1]
    if nameInFile("musicrecplus.txt", user):
        with open("musicrecplus.txt", "r") as fileRead:
            readContent = fileRead.readlines()
        userIndex = findUser(user,readContent)
        if userIndex != -1:
            if addPrefs != "":
                newLine = user + ":" + addPrefs + "\n"
                print(readContent[userIndex][:-1])
                with open("musicrecplus.txt", "w") as fileWrite:
                    newFile = ""
                    for i in range(len(readContent)):
                        if i == userIndex:
                            newFile += newLine
                        else:
                            newFile += readContent[i]
                    fileWrite.write(newFile)
    else:
        line = user + ":" + addPrefs + "\n"
        with open("musicrecplus.txt", "a") as file:
            file.writelines(line)

def getRecommendations(currentUser, prefs, userDict):
    '''Returns artists that the program recommends to the user. It sets a variable called mostSimilarUser equal to the bestMatch function called with the parameters of the current user, prefs, and the userDict to find the best and most similar user
    to the currentUser. Then a variable called recommendations is made that takes the mostSimilarUser and puts them into the notSimilar function with L1 being the currentUser prefs and L2 being the mostSimilarUser list. This will end up being a new list of 
    artists that are not in the currentUser prefs which is then returned(Charles)'''
    mostSimilarUser = bestMatch(currentUser, userDict, prefs)
    if mostSimilarUser != None:
        recommendations = notMatch(prefs, userDict[mostSimilarUser])
        print(recommendations)
    else:
        print("No recommendations available at this time.")

def bestMatch(user, userDict, prefs):
    """This function checks each user in the userDict to see which one is the best match. The way it does this is listing out the users in userDict since it uses keys() which will only return the names of the users.
    Then it will loop through each one of those users and run that user through the matchCounter function to test and see if that user has the highest amount of matches. If that user has more matches than the previous 
    highestMatches user, then it becomes the new highestMatches user and that user is assigned to the variable "best" which is returned at the end(Charles)"""
    users = list(userDict.keys())
    highestMatches = -1
    best = None
    for person in users: 
        matches = matchCounter(prefs, userDict[person])
        if user != person and '$' not in person:
            if highestMatches < matches and matches != 0: 
                highestMatches = matchCounter(prefs, userDict[person])
                best = person
    return best

def notMatch(L1,L2):
    """This function will check the two artist lists of the users for different artists. An empty list called L3 is made outside of the for loop, and the for loop itself loops through
    L2 to check if any given artist in L2 is in L1 or not, if an artist is found to be in L2 but not L1, then that artist will be added to L3(Charles)"""
    L3 = []
    for artist in L2: 
        if artist not in L1: 
            L3.append(artist)
    return L3

def matchCounter(L1,L2):
    """This function will check how many matches two given users have with the inputs being both of the user's lists of artists. It will
    loop through the first list and each time will check if any given artist in L1 is also in L2, if it is then matches which was initialized to 0 will increase by 1.
    However, if the length of L2 is equal to the amount of matches, it'll return -1 because that would mean it's a subset of the current user's list(Charles)"""
    matches = 0
    for artist in L1: 
        if artist in L2: 
            matches += 1
    if len(L2) == matches: 
        return -1
    return matches

def saveUserPreferences(user, prefs, userDict): 
    """This will update the preferences that the currentUser had stored in prefs, and set it equal to the values of that user within userDict, the user being the key to the prefs values. It then opens the file and 
    writes within the file the new data and closes it(Charles)"""
    userDict[user] = prefs
    file = open("musicrecplus.txt", "w")
    for i in userDict: 
        save = str(i) + ":" + ",".join(userDict[i]) + "\n"
        file.write(save)
    file.close()

def temporaryDict(L): 
    """This function creates a dictionary called tempDict which is a temporary dictionary that'll be used in the functions that look for the popularity stuff. The parameter of this function is a list L, and it will be 
    looped through using a for loop and each time the element will be replaced with 0. Then tempDict is returned(Charles)"""
    tempDict = {}
    for i in L:
        tempDict[i] = 0
    return tempDict

def artistList(userDict):
    """This function will create two empty lists called original and filtered. Original is a list of the original artists in userDict. Then filtered takes out any repeat artists. It does this by loping through userDict
    and adding the artists for each user and then again through original itself. Each artist will be added to filtered unless they are already in it(Charles)"""
    original = []
    filtered = []
    for user in userDict: 
        original += userDict[user]
    for artist in original: 
        if artist not in filtered: 
            filtered += [artist]
    return filtered

def popularity():
    '''This function creates a dictionary called artistDict which is defined by loadUsers() which creates a dictionary of the users and their prefs, then a list of the artists within that dictionary by using artistList, then 
    a temporary dictionary using temporaryDict. Then it loops through userDict and if $ is within the user, then it will continue which means it'll just go past it and act like it wasn't there. For any that doesn't have the $ symbol, 
    all of their artists will gain 1. Then a variable called mostPoints is initialized to 0, this will be used to track the artist that shows up the most throughout the lists, not including those with the $ symbol within their name. 
    Then it'll loop through a list of keys within artistDict and checks if each value is larger than the current value of mostPoints, so it'll keep updating until the highest number is found and there is nothing left to loop through(Charles)'''
    artistDict = temporaryDict(artistList(loadUsers("musicrecplus.txt")))
    userDict = loadUsers("musicrecplus.txt")
    for user in userDict:
        if '$' in user: 
            continue
        for artist in userDict[user]:
            artistDict[artist] += 1

    mostPoints = 0
    for artist in list(artistDict.keys()):
        if artistDict[artist] > mostPoints:
            mostPoints = artistDict[artist]

    return mostPoints

def threeMostPopular():
    '''
    returns 3 most popular 
    Jun Hong (first part copied from popularity to get a dictionary with all artists)
    '''
    artistDict = temporaryDict(artistList(loadUsers("musicrecplus.txt")))
    userDict = loadUsers("musicrecplus.txt")
    for user in userDict: 
        if '$' in user: 
            continue
        for artist in userDict[user]:
            if artist == "" or artist == '':
                continue
            else: 
                artistDict[artist] += 1

    sortedArtists = sorted(artistDict.items(), key=lambda x: x[1], reverse=True)

    num_artists = min(len(sortedArtists), 3)
    if num_artists > 0:
        for i in range(num_artists):
            print(sortedArtists[i][0])
    else:
        print("Sorry, no artists found.")

    
def mostLikes(userDict):
    '''This function creates a variable and initializes it to 0 called mostArtists, this will track the highest number of artists so far. The function loops through userDict and checks first if there's a dollar sign at the end 
    but if not then it checks the length of the artist list for a given user in userDict and if it's larger than the current mostArtists value then it becomes the new value. The name of that user is then stored in mostArtistsUser and then returned(Charles)'''
    mostArtists = 0
    for user in userDict: 
        if user[-1] != '$': 
            if len(userDict[user]) > mostArtists: 
                mostArtists = len(userDict[user])
                mostArtistsUser = user
    return mostArtistsUser

def nameInFile(filename, string):
    '''Returns whether or not a string is contained in a file. Written by
    Michael.'''
    with open(filename, "r") as f:
        for line in f:
            userInTxt = line.split(":")[0]
            if userInTxt == string:
                return True
    return False
        
def fileExists():
    """
    figures out if file exists, if it does, do nothing
    if it doesn't, create the file by writing an empty string
    Jun Hong
    """
    try:
        with open("musicrecplus.txt", "r") as file:
            pass
    except:
        with open("musicrecplus.txt", "w") as file:
            file.write("")

def main():
    '''The main function of the program. Written by Michael.'''
    fileExists()
    user = input('Please enter your name (put a $ symbol after your name if you wish your preferences to remain private): ')
    data = loadUsers('musicrecplus.txt')
    if not nameInFile('musicrecplus.txt', user):
        a = 'a'
        newUserLikes = []
        while a != '':
            a = input('Enter an artist that you like (Enter to finish): ')
            newUserLikes += [a.strip().title()]
        newUserLikes = newUserLikes[0:-1]
        data[user] = sorted(newUserLikes)
        enterPreferences(user,data)
    while True:
        selection = input('Enter a letter to choose an option:' + '\n' + 'e - enter preferences' + '\n' + 'r - get recommendations' + '\n' + 'p - show most popular artists'  + '\n' + 'h - how popular is the most popular artist' + '\n' + 'm - which user has the most likes ' + '\n' + 'q - save and quit' + '\n')
        if selection == 'e':
            a = 'a'
            newUserLikes = []
            while a != '':
                a = input('Enter an artist that you like (Enter to finish): ')
                if a not in data[user]:
                    newUserLikes += [a.strip().title()]
            newUserLikes = newUserLikes[0:-1]
            data[user] = sorted(newUserLikes + data[user])
            print(data[user])
            enterPreferences(user,data)
        if selection == 'r':
            getRecommendations(user, data[user], data)
        if selection == 'p':
            threeMostPopular()
        if selection == 'h':
            print(popularity())
        if selection == 'm':
            print(mostLikes(data))
        if selection == 'q':
            if '$' not in user:
                with open("musicrecplus.txt", "r") as fileRead:
                    content = fileRead.readlines()
                userList = []
                for line in content:
                    username = line.split(":")[0]
                    userList += [[username, data[username]]]
                userList.sort()
                with open("musicrecplus.txt", "w") as fileWrite:
                    for n in userList:
                        username, artists = [n[0], n[1]]
                        prefs = ""
                        for name in artists:
                            prefs += name + ","
                        line = username + ":" + prefs[:-1] + "\n"
                        fileWrite.write(line)
            return
        else:
            print(selection)
            print('Please select one of the listed operations.')

if __name__ == '__main__': main()
