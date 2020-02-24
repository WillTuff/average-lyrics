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
        self.limit = config.get(settings, 'limit')

        self.searchTerm = raw_input("Please enter the artists name: ")
        
        self.songList, self.lyricList = [], []
        self.idUrl = self.mBUrl + 'artist?query=' + self.searchTerm + self.jsonFormat

        self.i = 1

    def findArtistData(self):
        artistResponse = requests.get(self.idUrl).json()
        artistId = artistResponse['artists'][0]['id']

        # Obtain song titles using the artist id
        songResponse = requests.get(self.mBUrl + 'work?artist=' + artistId + self.workType + self.jsonFormat + self.limit)
        songData = songResponse.json()

        for song in songData['works']:
            self.songList.append(song['title'])

    def findLyrics(self):        
        for song in self.songList:
            searchLyric = self.lUrl + self.searchTerm + '/' + song
            self.lyricList.append(requests.get(searchLyric).json())
            print('Total songs searched: ' + str(self.i))
            self.i += 1
    
    def calcAverages(self):
        df = pd.DataFrame(self.lyricList)

        # Add additional column to calculate 
        df['Lyrics length'] = df['lyrics'].map(str).apply(len)
        summedValues = df.median()

        # Remove errors (all errors have three characters) and zero values
        errorNames = df[df['Lyrics length']==3].index
        df.drop(errorNames , inplace=True)

        removeZeros = df[df['Lyrics length']==0].index
        df.drop(removeZeros , inplace=True)
    
        # For loop prevents numpy info being included
        for val in summedValues:
            print("\nThe average number of lyrics for " + self.searchTerm + " is: " + str(val) + '\n')

    def findAverages(self):
        self.findArtistData()
        self.findLyrics()
        self.calcAverages()

def main():
    run = lyrics()
    run.findAverages()


main()
