#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(str.maketrans("", "",string.punctuation))

        ### project part 2: comment out the line below
        #words = text_string
        stemmer = SnowballStemmer("english")
        list_of_stems = []
        list_of_words = text_string.split(' ')
        for i in list_of_words:
            if i == '':
                list_of_words.remove(i)
        for word in list_of_words:
            a = stemmer.stem(word)

            list_of_stems.append(a)
        word_stems = ' '.join(list_of_stems)
        print(list_of_stems)
        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        




    return word_stems

    

def main():
    ff = open("D://PycharmProjects//untitled//cкрипты Python//udacity_intro_to_machine_learning//text learning//test_email.txt", "r")
    text = parseOutText(ff)
    print (text)


if __name__ == '__main__':
    main()

