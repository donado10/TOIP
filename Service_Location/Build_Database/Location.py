#!/usr/bin/env python3

from sys import argv
import Build_Database.Database as Database

db = Database.Database(argv[1])
db.UpdateDispo()




'''''

NameArtiste = int(argv[1])

spotify = SpotifyService.SpotifyService
ListeAlbum = spotify.GetAlbum(NameArtiste)

for album in ListeAlbum:
    print(album[0][0],album[0][1],end='\n')

'''''