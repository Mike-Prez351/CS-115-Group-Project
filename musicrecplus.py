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
    file = open("musicrecplus.txt", 'r')
    userLikes = {}
    for line in file:
        [user, likes] = line.strip().split(':')
        likeList = likes.split(',')
        likeList.sort()
        userLikes[user] = likeList
    file.close()
    return userLikes

def enterPreferences(user, userList):
    """
    takes username and list of prefs, writes to file in this syntax:
    username:artist1,artist2,artist3,...
    colon between username and list of artists, commas separating artists
    also takes care of title case
    DOES NOT TAKE CARE OF SORTING YET
    Jun Hong
    """
    addPrefs = ""
    for x in prefs:
        addPrefs = x.title() + ","
    addPrefs = addPrefs[:-1]
    if nameInFile("musicrecplus.txt", user):
        """
        possible idea for this (since i don't inserting into a line is a thing)
        find where the line is
        copy the line
        delete line from original file, either by reading all the lines first and not writing the line back or some other method
        append the new line, which is the original plus new recommendations
        """
        pass
    else:
        line = user + addPrefs + "\n"
        with open("musicrecplus.txt", "a") as file:
            file.writelines(line)

def getRecommendations(currentUser, prefs, userList):
    '''Returns artists that the program recommends to the user. It sets a variable called mostSimilarUser equal to the bestMatch function called with the parameters of the current user, prefs, and the userList to find the best and most similar user
    to the currentUser. Then a variable called recommendations is made that takes the mostSimilarUser and puts them into the notSimilar function with L1 being the currentUser prefs and L2 being the mostSimilarUser list. This will end up being a new list of 
    artists that are not in the currentUser prefs which is then returned(Charles)'''
    mostSimilarUser = bestMatch(currentUser, prefs, userList)
    recommendations = notMatch(prefs, userList[mostSimilarUser])
    return recommendations

def bestMatch(currentUser, userList, prefs):
    """This function checks each user in the userList to see which one is the best match. The way it does this is listing out the users in userList since it uses keys() which will only return the names of the users.
    Then it will loop through each one of those users and run that user through the matchCounter function to test and see if that user has the highest amount of matches. If that user has more matches than the previous 
    highestMatches user, then it becomes the new highestMatches user and that user is assigned to the variable "best" which is returned at the end(Charles)"""
    users = list(userList.keys())
    highestMatches = -1
    best = None
    for user in users: 
        matches = matchCounter(prefs, userList[user])
        if prefs not in userList[user]:
            if highestMatches < matches: 
                highestMatches = matchCounter(prefs, userList[user])
                best = user
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
    loop through the first list and each time will check if any given artist in L1 is also in L2, if it is then matches which was initialized to 0 will increase by 1(Charles)"""
    matches = 0
    for artist in L1: 
        if artist in L2: 
            matches += 1
    return matches

def saveUserPreferences(user, prefs, userList[user], userList): 
    """This will update the preferences that the currentUser had stored in prefs, and set it equal to the values of that user within userList, the user being the key to the prefs values. It then opens the file and 
    writes within the file the new data and closes it(Charles)"""
    userList[user] = prefs
    file = open("musicrecplus.txt", "w")
    for i in userList: 
        save = str(i) + ":" + ",".join(userList[i]) + "\n"
        file.write(save)
    file.close()

def temporaryDict(L): 
    """This function creates a dictionary called tempDict which is a temporary dictionary that'll be used in the functions that look for the popularity stuff. The parameter of this function is a list L, and it will be 
    looped through using a for loop and each time the element will be replaced with 0. Then tempDict is returned(Charles)"""
    tempDict = {}
    for i in L:
        tempDict[i] = 0
    return tempDict

def artistList(userList):
    """ff"""
    original = []
    filtered = []
    for user in userList: 
        original += userList[i]
    for artist in original: 
        if artist not in filtered: 
            filtered += [artist]
    return filtered

def mostPopularArtists():
    '''Returns which artist is liked by the most users. Written by ____'''
    pass

def popularity():
    '''Returns the number of users that like the most popular artist. 
    Written by ____'''
    pass

def mostLikes():
    '''Returns the user that likes the most artists. Written by
    ______'''
    pass

def nameInFile(filename, string):
    '''Returns whether or not a string is contained in a file. Written by
    Michael.'''
    with open(filename, "r") as f:
        for line in f:
            if line[0:len(string)] == string:
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
    '''The main function of the program. Written by ______.'''
    userList = loadUsers()
    fileExists()
    user = input('Please enter your name (put a $ symbol after your name if you wish your preferences to remain private): ')
    data = loadUsers('musicrecplus.txt')
    if not nameInFile('musicrecplus.txt', user):
        a = 'a'
        newUserLikes = []
        while a != '':
            a = input('Enter an artist that you like (Enter to finish): ')
            newUserLikes += [a]
        newUserLikes = newUserLikes[0:-1]
        data[user] = newUserLikes
        enterPreferences(user,newUserLikes)
    while True:
        selection = input('Enter a letter to choose an option:' + '\n' + 'e - enter preferences' + '\n' + 'r - get recommendations' + '\n' + 'p - show most popular artists'  + '\n' + 'h - how popular is the most popular artist' + '\n' + 'm - which user has the most likes ' + '\n' + 'q - save and quit' + '\n')
        if selection == 'e':
            a = 'a'
            newUserLikes = []
            while a != '':
                a = input('Enter an artist that you like (Enter to finish): ')
                newUserLikes += [a]
            newUserLikes = newUserLikes[0:-1]
            data[user] = newUserLikes
        if selection == 'r':
            print(recommendations())
        if selection == 'p':
            print(mostPopularArtists())
        if selection == 'h':
            print(popularity())
        if selection == 'm':
            print(mostLikes())
        if selection == 'q':
            # Update database if user is not private
            return None
        else:
            print('Please select one of the listed operations.')

if __name__ == '__main__': main()
