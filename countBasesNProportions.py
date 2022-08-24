def countBases(sequence):
    """
    This function counts the number of bases in a sequence, and returns it as a dictionary.

    Parameters
    ----------
    sequence : String
        A string representing a sequence of bases.

    Returns
    -------
    baseDictionary
        A dictionary containung counts of all the bases.
    """
    
    baseDictionary = dict()
    
    #Walk thru sequence
    for base in sequence:
        #If the base is not in the dictionary, add it
        if base not in baseDictionary:
            baseDictionary[base] = 1
            
        #If the base IS in the dictionary, increment its count
        else:
            baseDictionary[base] += 1
    
    return baseDictionary

def calcBaseProportions(sequence):
    """
    This function takes a sequence, and returns the proportion of each base that makes up the sequence.

    Parameters
    ----------
    sequence : String
        A string representing a sequence of bases.
    """
    
    print('freqs')
    
    #Count total # of bases
    total = float(sum([sequence[base] for base in sequence.keys()]))
    
    #Print the proportion of bases that make up the sequence
    for base in sequence.keys():
        print(base + ':' + str(sequence[base]/total))

calcBaseProportions(countBases('ATCTGACGCGCGCCGC'))
