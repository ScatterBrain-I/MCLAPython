# Program by Peter Niemeyer 2017/07/16
# MCLA Python / Mark Cohen
# This program:
# Pulls data on varience of global temp from NASA site
# Promputs user to set ranges of early and late data to allow comparrison
# Returns an average deviation from 'norm' and counts years in excess of norm

import NEMO
import urllib2

# read the temps from a NASA file online (Had to research urllib2)
# and return them in a list
def readTemps():
    temps = []
    file = urllib2.urlopen('https://climate.nasa.gov/system/internal_resources/details/original/647_Global_Temperature_Data_File.txt', 'r')
    for line in file:
        data = line.split('     ')
        temp = data[1].replace(" ", "")
        temps.append(float(temp))  
    return temps  # new list is now float, not string  

# gets user defined splits for data comparrison
# applies a conversion to get a decimal equivalent of percentage
# places the userSplit into a list for later use
def userSplit():
    split = []
    print ("Nasa has compiledannual global tempertaure varience since 1880.\
\nThis program will compare a percentage of the data starting in 1880 \
with a percentage of the most recent data.")
    split1 = NEMO.userInt("\nWhat percent from the start of the data set do you \
to use for comparrison?\n(Enter as an integer please):")
    split.append(NEMO.percentToDecimal(split1))
    split1 = NEMO.userInt("\nWhat percent from the end of the data set do you \
want to use for comparrison?\n(Enter as an integer please):")
    split.append(NEMO.percentToDecimal(split1))
    return split

# calculates the average of a range of numbers
# as specified by start (inclusive) and stop (inclusive)
# def calculateAve(temps, start, stop):
def dataSet(): # determines the total number of datapoints in the NASA Data
    dataLen = len(readTemps())
    return dataLen

# main function:
# pulls function from above defs.
# generates properly sized list, averages data in list, counts instances of +data
# returns data for user to compare
def main():
    
    # calls defs from above to use in making calculations 
    temps = readTemps()
    split = userSplit()
    dataLen = dataSet()
    
    # establishes list of data to be addressed for both 'early' and 'recent'
    # range uses inline calculation of # as f(x) of % input from user
    # calculates average of data in new list
    # counts instances of positive (not negative) data points
    early = temps[0:int(round(split[0] * dataLen))]
    earlyAverage = sum(early) / len(early)
    earlyCount = sum(1 for data in early if float(data) > 0)
   
    recent = temps[int(round(dataLen - dataLen * split[1])):dataLen]
    recentAverage = sum(recent) / len(recent)
    recentCount = sum(1 for data in recent if float(data) > 0)
    
    # output for user
    # averages are set at 2 significant digits to correspond with data set
    print
    print "During the first %i years (%i%% of the available data set), the \
average deviation from the temperature anomaly is \
%.2f degrees celcius." %(len(early), split[0]*100, earlyAverage)
    print "During those %i years, %i were warmer than 1951-1980 'norm' \
eastablished by NASA" % (len(early), earlyCount)
    print
    print "During the last %i years (%i%% of the available data set), the \
average deviation from the temperature anomaly is \
%.2f degrees celcius." %(len(recent), split[1]*100, recentAverage)
    print "During those %i years, %i were warmer than 1951-1980 'norm' \
eastablished by NASA" % (len(recent), recentCount)

main() 
