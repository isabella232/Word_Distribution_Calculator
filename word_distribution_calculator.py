def calc_distribution(text, word):
    ''' Calculates the percentage of how many times word appears in text
        Percentage = number of times word appears / total amount of words * 100

        Input: "cat cat cat dog", "dog"
        Output: 25 (Since it is 25%)

        Input: "tomato tomatoes tomato", "tomato"
        Output: 66.66
    '''
    textData = word_counter(text)
    word_frequencies = textData[0]
    totalWords = textData[1]

    # check if word appears at all
    if word not in word_frequencies:
        return 0
    
    return word_frequencies[word] / totalWords * 100

def stringToWords(text):
    ''' Separates a string into a list of individual words.
        Words are denoted as having space in-between them.
        Assumes no duplicate spaces and no punctuation
        
        Input: "An example sentence"
        Output: ["An", "example", "sentence"]
    '''
    # initialize variables
    wordList = []
    numWords = 0 # index for wordList

    # indices for slicing text
    startIndex = 0
    stopIndex = 0

    # iterate through each character, finding appropriate slicing ranges
    for c in text:
        if (c == ' '):
            # space found, record word
            wordList.append(text[startIndex:stopIndex])
            numWords += 1

            # mark the startIndex at the next character
            startIndex = stopIndex + 1
        stopIndex += 1

    # add remaining characters as the last word
    wordList.append(text[startIndex:])
    return wordList


def word_counter(text):
    ''' Counts the number of words in text
        Returns a list containing two elements:
            a dictionary of words and their frequencies
            the total amount of words

        Input: "cat cat cat dog"
        Output: [ {("cat" : 3), ("dog" : 1)}, 4 ]
    '''
        
    word_counts = {}

    # format the raw string into a list of words
    wordList = stringToWords(text)

    # calculate the frequency of each word and total word count
    for word in wordList:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    return [word_counts, len(wordList)]

def main():
    # get raw text
    print("Please enter a string")
    text = input()

    # get word
    print("Please enter a word")
    word = input()

    # calculate word distribution in raw text
    distr = calc_distribution(text, word)

    # print result
    print(word + " makes up " + str(distr) + "%" + " of the words in " + text)
