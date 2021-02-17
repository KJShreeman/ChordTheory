#Global Variables
isMajor = False
notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B'] #all sharps
notes_summarized = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
majorpattern = [2,2,1,2,2,2,1]
minorpattern = [2,1,2,2,1,2,2]
chordlist = []
sequence = ['Major','Minor','Minor','Major','Major','Minor','Diminished'] #major
sequence2 = ['Minor','Diminished','Major','Minor','Major','Major','Major'] #minor
scale = [] #Used in keynotes to write the notes of a key

"""
1-Any
2-5^7
3-6
4-1 or 5^7
5-1
6-2 or 4
"""

def song(song):
    with open("{}.txt".format(song),'w') as file:
        file.write("Song Name: {}".format(song))

def writeline(x,songname):
    """Writes a string to the file"""
    x = str(x)
    with open("{}.txt".format(songname),'a') as file:
        file.write('\n'+x+'\n')

def major(key, majororminor,isMajor,songname):
    """Sets isMajor boolean and adds key to txt file. Calls writeline(x)"""
    if majororminor == "Major":
        isMajor = True
    key = key + " " + majororminor
    writeline(key,songname)
    return isMajor

def keynotes(key,isMajor):
    """Creates and returns a list of notes in the given key"""
    j = notes.index(key)
    scale2 = scale[:]
    scale2.append(key)
    if isMajor:
        for k in majorpattern:
            index = j+k
            if index <= len(notes):
                note = notes[index]
                scale2.append(note)
                j = j+k
    else:
        for k in minorpattern:
            index = j+k
            if index <= len(notes):
                note = notes[index]
                scale2.append(note)
                j = j+k
    return removeextra(scale2)



def removeextra(scale):
    """Removes extra notes and returns scale"""
    if len(scale) == 8:
        del scale[7]
    return scale

def printmenu():
    print('-----------------')
    print("1: Print Notes")
    print("2: Print Chords")
    print("3: Change Key")
    print("4: Quit")
    option = int(input("Option 1 or 2 or 3 (4 to quit)?: "))
    print('-----------------')
    return option

def chords(key,isMajor):
    """Returns a list of chords in a given key. Calls keynotes() function to return list of notes in a key"""
    x = keynotes(key,isMajor)
    y = []
    for i in range(len(x)): #length of keynotes and sequence is same
        if isMajor:
            string = x[i]+" "+sequence[i]
            y.append(string)
        else:
            string = x[i] + " " + sequence2[i]
            y.append(string)
    return y

def chordnotes(keynote,chord):
    """Prints chord and chord notes in each line. Accepts list of chords and list of notes for a specific key"""
    keynote+=keynote #Use add sign to concatenate (not append which adds as element)
    for i in range(len(chord)):
        print(chord[i],keynote[i],keynote[i+2],keynote[i+4],sep=' ')

def notearray():
    """Returns a list of notes user knows"""
    num = int(input("Number of notes you know (no flats): "))
    array = []
    for i in range(num):
        note_name = input("Note {}: ".format(i+1))
        array.append(note_name)
    return array

def chordarray():
    """Returns a list of chords user knows"""
    array = []
    num = int(input("Number of chords you know (no flats): "))
    print("Example Format: A# Major / B Minor")
    for i in range(num):
        chord_name = input("Chord {}: ".format(i+1))
        array.append(chord_name)
    return array

def scaledict(notes_summarized):
    """Creates and returns a dictionary of 24 major and minor scales. Calls keynotes() to get notes"""
    dict = {}
    for note in notes_summarized:
        list1 = keynotes(note,True)
        list2 = keynotes(note,False)
        string1 = note + ' ' + 'Major'
        string2 = note + ' ' + 'Minor'
        dict[string1] = list1
        dict[string2] = list2
    return dict

def chordlist(notes_summarized):
    """Returns a dict containing '<major/minor name>': [chords]. Calls scale_dict() to get get initial dict"""
    dict = scaledict(notes_summarized)
    emptydict = {} #Storing dict
    emptylist = []
    for key,value in dict.items():
        if 'j' in list(key): #If major key
            for i in range(len(value)):  # length of keynotes and sequence is same
                string = value[i] + " " + sequence[i]
                emptylist.append(string)
            emptydict[key] = emptylist
            emptylist = []
        else: #If minor key
            for i in range(len(value)):  # length of keynotes and sequence is same
                string = value[i] + " " + sequence2[i]
                emptylist.append(string)
            emptydict[key] = emptylist
            emptylist = []
    return emptydict

def key_and_chordnum():
    """Returns dictionary for number of occurrences of chords in each key"""
    count_max = 0
    empty_dict = chordlist(notes_summarized)
    array = chordarray()
    for key,value in empty_dict.items():
        for chord in array:
            for val in range(len(value)):
                if chord == value[val]:
                    count_max+=1
        empty_dict[key] = count_max
        count_max = 0
    return empty_dict

def key_and_num():
    """Return dictionary for number of occurrences of notes in each key"""
    count_max = 0
    dict = scaledict(notes_summarized)
    empty_dict = {}
    array = notearray()
    for key,value in dict.items():
        for note in array:
            for val in range(len(value)):
                if note == value[val]:
                    count_max+=1
        empty_dict[key] = count_max
        count_max = 0
    return empty_dict

def printscale(empty_dict):
    """Returns list of scale names containing most number of inputted notes and chords"""
    max_val = 0 #Maximum num of occurrences
    scales = []
    for key,value in empty_dict.items(): #Sets max_val
        if value > max_val:
            max_val = value
    for key,value in empty_dict.items():
        if max_val == value:
            scales.append(key)
    return scales


def chordprogression(chord, songname, choice, key, majororminor,emptylist):
    """Creates and writes a chord progression using chords in chord"""
    if choice in chord:
        index = chord.index(choice)
        emptylist.append(index)
        with open('{}.txt'.format(songname), 'a') as song:
            song.write(choice + '->')
    else:
        print("Chord inputted is not within {} {}".format(key, majororminor))
        ask = input("Are you sure about your choice? (Y/N): ")
        index = 'None'
        emptylist.append(index)
        if ask == 'Y':
            with open('{}.txt'.format(songname), 'a') as song:
                song.write(choice + '->')


def showchordsequence(list):
    """Returns a string showing chord progression from the list formatted"""
    rxp = {0: 'I', 1: 'II', 2: 'III', 3: 'IV', 4: 'V', 5: 'VI', 6: 'VII','None':'None'}
    emptylist = []
    for num in list:  # Create list of roman numerals
        for key, val in rxp.items():
            if num == key:
                emptylist.append(val)
                continue
    s = '->'
    return s.join(emptylist)  # Returns as a string

def main(isMajor,songname):
    """Creates a song and runs menu options. Disciple to all()"""
    song(songname)
    #Gather Input
    key = input("Key (A/B/C/D/E/F/G): ")
    majororminor = input("Major/Minor: ")
    majororminor = majororminor.title()

    isMajor = major(key, majororminor,isMajor,songname) #Major/Minor Key?
    option = printmenu()
    while option != 4:
        if option == 0:
            chord = chords(key, isMajor)
            emptylist = []
            count = 1
            choice = input("Chord {} (q to quit): ".format(count))
            while choice != 'q': #User enters chords till done
                chordprogression(chord, songname, choice, key, majororminor,emptylist)
                count +=1
                choice = input("Chord {} (q to quit): ".format(count))
            show = input("Show chord sequence? (Y/N): ")
            if show == 'Y':
                print(showchordsequence(emptylist))
                break
        if option == 1:
            print(keynotes(key, isMajor))
            option = printmenu()
        elif option == 2:
            chord = chords(key,isMajor)
            print(chord)
            z = input("Do you want the notes to the chords (Y/N)?: ")
            if z == 'Y':
                print('---------------------------------------')
                keynote = keynotes(key,isMajor)
                chordnotes(keynote,chord)
            option = printmenu()
        elif option == 3:
            key = input("Key (A/B/C/D/E/F/G): ")
            majororminor = input("Major/Minor: ")
            majororminor = majororminor.title()
            isMajor = major(key, majororminor,isMajor,songname)
            option = printmenu()

    print("Bye!")

def all(isMajor):
    """Main Program Run"""
    print("Welcome to Piano Production!")
    print("1: Figure out the key")
    print("2: Create a song immediately")
    try: #Use in biggest function to control everything!
        option = int(input("Number? : "))
        if option > 2 or option <= 0:
            raise SyntaxError #Go except
        elif option == 2:
            songname = input("Song Name: ")
            main(isMajor,songname)
        elif option == 1:
            print("1: From the chords you know ")
            print("2: From the notes you know ")
            ask1 = int(input("Option 1/2? : "))
            if ask1 == 2:
                emptydict = key_and_num()
                print("List of possible majors/minors:",printscale(emptydict))
                ask2 = input("Do you want to create a song (Y/N)?: ")
                if ask2 == 'Y':
                    songname = input("Song Name: ")
                    main(isMajor, songname)
                else:
                    print("Bye!")
            elif ask1 == 1:
                emptydict = key_and_chordnum()
                print("List of possible majors/minors:",printscale(emptydict))
                ask2 = input("Do you want to create a song (Y/N)?: ")
                if ask2 == 'Y':
                    songname = input("Song Name: ")
                    main(isMajor, songname)
                else:
                    print("Bye!")
            else:
                print("Invalid option chosen")

    except(SyntaxError):
        print("Integer Outside Range (please choose 1 or 2 only)")
    except:
        print("Invalid input")

#Initiate code#
all(isMajor)






#FIXME: Chord Progression (2)
# new line after line 2

"""
Until user is done:
    Append chord + '->' to file
    - Warn user if chord not inside the major/minor
    - Gets index of chord and append to chord_seq_list
    - Enter q to quit
    - Option to show chord sequence
        - Read from list and format in roman numerals with ->
    




"""






