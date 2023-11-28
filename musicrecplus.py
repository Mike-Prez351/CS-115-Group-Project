################################################################################
# Names: Charles Villa, Jun Hong Wang, Michael Preziosi                        #
# Pledge: I pledge my honor that I have abided by the Stevens Honor System     #
# CS 115 - Group Project                                                       #
################################################################################

def loadUsers(fileName):
    '''Reads in a file of stored users' preferences stored in the file
    fileName. Returns a dictionary containing a mapping of user names to a list
    of preferred artists. Written by Michael.'''
    file = open(fileName, 'r')
    userLikes = {}
    for line in file:
        [user, likes] = line.strip().split(':')
        likeList = likes.split(',')
        likeList.sort()
        userLikes[user] = likeList
    file.close()
    return userLikes

def enterPreferences(user, prefs):
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

def recommendations():
    '''Returns artists that the program recommends to the user. Written by 
    ____'''
    pass

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
