import plistlib


def findDuplicates(fileName):
    print('Finding duplicate tracks in {}\n'.format(fileName))
    plist = plistlib.readPlist(fileName)

    #get the tracks from the Track dictionary
    tracks = plist['Tracks']

    #create a track name dictionary
    trackNames = {}
    #iterate through the tracks
    for trackId, track in tracks:
        try:
            name = track['Name']
            duration = ['Total Time']
            #look up existing entries
            if name in trackNames:
                #if name and duration match, increment the count
                #round the track length to nearest second
                if duration//1000 == trackNames[name][0]//1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count+1)
            else:
                #add dictionary entry as tuple (duration, count )
                trackNames[name] = (duration, 1)
        except:
            pass

findDuplicates('Library.xml')