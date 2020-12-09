from csv import reader, DictReader
from sys import argv

sequences = {}
data = {}
#check for correct number or args
if len(argv) != 3:
    print("Usage: ./speller database sequence")
    exit()

#read and store the database
with open(argv[1], 'r') as datafile:
    #create reading object
    datareader = reader(datafile)
    #jump over first row
    headers = next(datareader)
    #go over each row
    for row in datareader:
        datalist = row
        #take key=name into key variable
        key = datalist[0]
        #initiate list
        value = []
        #put all other values of the row into the value list
        for i in range(1, len(datalist)):
                value.append(datalist[i])
        #add key and value list into the data dictionary
        data[key] = value

# read and store the dna sequence into a string
with open(argv[2], 'r') as seqfile:
    seqreader = reader(seqfile)
    for row in seqreader:
        seqlist = row
sequence = seqlist[0]

#search for repitition in sequence
#first get a list with all the names of the keysequences
with open(argv[1], 'r') as sequencecode:
    #create reading object
    sequenceq = reader(sequencecode)
    #jump over first row
    #go over each row
    for row in sequenceq:
        dnaSequences = row
        dnaSequences.pop(0)
        break
# create a dictionary with the dnasequences are the keys and the value ist first set to one but will be iterated in the screening process
for item in dnaSequences:
    sequences[item] = 1



for key in sequences:
    #get the length of the respective key to use it whilst going through the dna sequence
    length = len(key)
    # storing values rep for current count and repmax for comparison and the storeage of the bigger
    rep = 0
    repmax = 0
    for i in range(len(sequence)):
        #to not overwrite
        while rep > 0:
            rep -= 1
            continue
        #go through the dna sequence i to i+length
        if sequence[i: i+length] == key:
            #if the above snippet matches the key- compare it to the next snippet in the sequence
            while sequence[i-length: i] == sequence[i: i + length]:
                #each time the snippets matches (the sequence repeats) add to the rep count
                rep += 1
                i += length
            #If this repetition value is bigger then the repmax value, store it into the repmax value
            if rep > repmax:
                repmax = rep

    sequences[key] += repmax

#get the name of the person matching the dna sequence
#get values from sequences dict into list to make comparison easier
values = []
for key in sequences:
    values.append(sequences[key])
#go through each pattern and compare the database value to the sequence value
for key in data:
    match = 0
    #go through every persons(key) value (i) and compare each to the sequence value, if they match- counter mactches+1
    for i in range(len(sequences)):
        if int(data[key][i]) == values[i]:
            match += 1
    #If the counter for this person(key) matches the amount of patterns, this is the wanted person - stop the program
    if match == len(sequences):
        print(key)
        exit()
print("No match.")