import requests
import json
import unicodedata
import ConfigParser
import pandas as pd

class lyrics():
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read("settings.ini")
        settings = "info"

        self.mBUrl = config.get(settings, 'mBUrl')
        self.lUrl = config.get(settings, 'lUrl')
        self.jsonFormat = config.get(settings, 'json')
        self.workType = config.get(settings, 'workType')

        self.searchTerm = raw_input("Please enter the artists name: ")
        
        self.songList, self.lyricList = [], []
        self.idUrl = self.mBUrl + 'artist?query=' + self.searchTerm + self.jsonFormat

        self.i = 1

    def findAverages(self):
        # Find artist ID using 
        artistResponse = requests.get(self.idUrl).json()
        artistId = artistResponse['artists'][0]['id']

        # Obtain song titles using the artist id
        songResponse = requests.get(self.mBUrl + 'work?artist=' + artistId + self.workType + self.jsonFormat + '&limit=50')
        songData = songResponse.json()

        for song in songData['works']:
            self.songList.append(song['title'])

        # Using song titles list, obtain song lyrics
        for song in self.songList:
            searchLyric = self.lUrl + self.searchTerm + '/' + song
            self.lyricList.append(requests.get(searchLyric).json())
            print('Total songs searched: ' + str(self.i))
            self.i += 1

        # Pass lyrics to a panda dataframe
        df = pd.DataFrame(self.lyricList)

        # Add additional 
        df['Lyrics length'] = df['lyrics'].map(str).apply(len)
        summedValues = df.median()

        # Remove errors (all errors have three characters) and zero values
        errorNames = df[df['Lyrics length']==3].index
        df.drop(errorNames , inplace=True)

        removeZeros = df[df['Lyrics length']==0].index
        df.drop(removeZeros , inplace=True)
    

        # Using a for loop allows median to be printed without
        # numpy info
        for val in summedValues:
            print("\nThe average number of lyrics for " + self.searchTerm + " is: " + str(val) + '\n')


run = lyrics()
run.findAverages()



