#-------------------------------------------------------------------------------
# Program by Peter Niemeyer 2017/08/5
# MCLA Python / Mark Cohen
# Search program EXAM #4
#
# This program: Gets imput from user for a search term (case insensitive)
# searches ALL .txt files in directory
# out uts line instance and provides a count
#-------------------------------------------------------------------------------

import NEMO
import os

files = os.listdir('.')
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def newFiles(files):
    files2 = []
    for f in files:
        if ".txt" in f:
            files2.append(f)
    return files2   
    
#-------------------------------------------------------------------------------
# simple function that gets users search string and makes it uppercase in order
# to be serached later againbst uppercase modified text to insure case-
# insensitivity
#-------------------------------------------------------------------------------
def getSearch():
    search = NEMO.userString("Enter a search term:")
    search = search.upper()
    print
    print "HERE ARE YOUR RESULTS:"
    return search
    
#-------------------------------------------------------------------------------
# searches each line in files gotten from the list of files for the search
# word and prints line as it appears in the text
# returns counter = total number of "hits"
# note: search is case insensitive by seaching .UPPER but print out is original
#-------------------------------------------------------------------------------
def look(search, files2):
    counter = 0 # counter for number of instances of foud text
    for f in files2:
        for line in open(f):
            line = line.strip() #remove excess space
            line2 = line.upper()
            if search in line2:
                counter = counter + 1
                print '%s:   %s' %(f, line)
    return counter
    
#-------------------------------------------------------------------------------
# gives a report of count: Verb number adjusted and sing/plur accounted for 
#-------------------------------------------------------------------------------
def counterPrint(counter):
    sornos=NEMO.singPlur(counter)
    wasorwere=NEMO.wasWere(counter)
    print "\nThere %i %s result%s in your search." % (counter, wasorwere, sornos)
    

#-------------------------------------------------------------------------------
# main is the main main that does the main thing (stated at top of code)
#-------------------------------------------------------------------------------
def main():
    files2 = newFiles(files) #makes proper file list from directory
    search = getSearch() #gets user search
    counter = look(search, files2) #counts up instances and prints lines
    counterPrint(counter) #produces a gramatically proper outut for count
    
main()    