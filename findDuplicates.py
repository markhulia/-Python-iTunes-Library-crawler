import plistlib


def findDuplicates(fileName):
    print('Finding duplicate tracks in {}\n'.format(fileName))
    plist = plistlib.readPlist(fileName)

    #get the tracks from the Track dictionary
    tracks = plist['Tracks']

    #create a track name dictionary
    trackNames = {}
    #iterate through the tracks
    for trackId, track in tracks.items():
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
                # print(trackNames[name])
        #if track does not have name - pass
        except:
            pass

    #store duplicates as (name, count) tuples
    dups= []
    for k, v in trackNames.items():
        if v[1] >1:
            dups.append(v[1], k)

    #save duplicates to a file
    if len(dups)>0:
        print("Found {} duplicates. Track names saved to dups.txt".format(len(dups)))
        f = open("dups.txt", "w")
        for val in dups:
            f.write("{} {}\n".format(val[0], val[1]))
        f.close()
    else:
        print("No duplicats were found")




findDuplicates('Library.xml')