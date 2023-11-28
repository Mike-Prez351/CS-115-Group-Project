################################################################################
# Names: Charles Villa, Jun Hong Wang, Michael Preziosi                        #
# Pledge: I pledge my honor that I have abided by the Stevens Honor System     #
# CS 115 - Group Project                                                       #
################################################################################

def loadUsers(fileName):
    '''Reads in a file of stored users' preferences stored in the file
    fileName. Returns a dictionary containing a mapping of user names to a list
    of preferred artists. Written by ______.'''
    file = open(fileName, 'r')
    userLikes = {}
    for line in file:
        [user, likes] = line.strip().split(':')
        likeList = likes.split(',')
        likeList.sort()
        userLikes[user] = likeList
    file.close()
    return userLikes

def enterPreferences():
    '''Enters the user's preferences into the database. Written by ______.'''
    while input('Enter an artist that you like (Enter to finish).') != '':
        newUserLikes = user

def recommendations():
    '''Returns  Written by ____'''
    pass

def mostPopularArtists():
    '''Returns which artist is a preference for the most users. Written by
    ____'''
    pass

def popularity():
    '''Returns the number of users that have the most popular artist as a
    preference. Written by ____'''
    pass

def mostLikes():
    '''Returns the user that likes the most artists. Written by
    ______'''
    pass

def isInFile(filename, string):
    '''Returns whether or not a string is contained in a file. Written by
    ______.'''
        with open(filename, "r") as f:
        counter = 0
        for line in f:
            if string in f:
                counter += 1
        if counter = 0:
            return False
        return True
            

def main():
    '''The main function of the program. Written by ______.'''
    user = input('Please enter your name (put a $ symbol after your name if you wish your preferences to remain private): ')
    if not isInFile(musicrecplus.txt, user):
        like = input('Enter an artist that you like (Enter to finish): ')
        
    while True:
        selection = input('Enter a letter to choose an option:' + '\n' + 'e - enter preferences' + '\n' + 'r - get recommendations' + '\n' + 'p - show most popular artists'  + '\n' + 'h - how popular is the most popular artist' + '\n' + 'm - which user has the most likes ' + '\n' + 'q - save and quit' + '\n')
        if selection == 'e':
            a = loadUsers(musicrecplus.txt)
            

            return enterPreferences()
        if selection == 'r':
            print(recommendations())
        if selection == 'p':
            print(mostPopularArtists())
        if selection == 'h':
            print(popularity())
        if selection == 'm':
            print(numOfLikes())
        if selection == 'q':
            if not $ in user
                updatedFile = open(filename, 'w')
            
            return None
        else:
            print('Please select one of the listed operations.')


if __name__ == '__main__': main()
