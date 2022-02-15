from functools import reduce
from operator import sub
import string
import re

def process_file(fname, enc):
    # open file for "r" eading
    with open(fname, "r", encoding=enc) as file:
        dat = file.read() # read file
        dat = perform_re(dat)
    return dat.split() # return read data, split at spaces
# end def process_file(fname, enc):

def write_results(fname, data, enc):
    # open a file for "w"riting
    with open(fname, "w", encoding=enc) as file:
        file.write(data)
# end def write_results("fname", data, enc):

def words_to_dict(all_words, dictionary):
    for w in all_words: # for each word
        w = clean_word(w) # send word for cleaning
        if w in dictionary: # if word was counted before
             dictionary[w] += 1 # increment count
        else:
             dictionary[w] = 1 # begin count for new word
# end words_to_dict(all_words, dictionary):

def clean_word(word):
    for p in string.punctuation:
        word = word.replace(p, "") # delete punctuation
    return word.lower()
# end def clean_word(word):

def perform_re(text):
    text = re.sub(r"(CHAPTER) ([IVXLC] +.)", "\\1\\2", text)
    return text
# end def perform_re(text):

BOOKS = {"1": {"filename":"a_modest_proposal.txt","title":"Modest Proposal"},"2": {"filename":"a_tale_of_two_cities.txt","title":"A Tale of Two Cities"},"3": {"filename":"alice.txt","title":"Alice"},"4": {"filename":"the_great_gatsby.txt", "title":"The Great Gatsby"},"5": {"filename":"the_yellow_wallpaper.txt","title":"The Yellow Wallpaper"}

def main():

    valid_selection = False
    book_words= {}

    ttr = []
    while not valid_selection:
        choice = input("Please choose any two text to compare.\nPlease separate your selection by ',' \n\n1.A Modest Proposal\n2.A Tale of Two Cities\n3.Alice\n4.The Great Gatsby\n5.The Yellow Wallpaper\n")

        split_choice = choice.split(",")
        valid_selection = all([int(book) in range(1,6) for book in split_choice])

        for data in split_choice:
            book = BOOKS[data]["filename"]
            unique_words = {} # empty dictionary for word counts
            words = process_file(book, "utf-8")
            words_to_dict(words, unique_words)

            book_words[BOOKS[data]["title"]] = unique_words

            total_unique_words = len(unique_words.keys())
            total_words = len(words)

            print("Found {0} unique words.".format(total_unique_words))
            print("There is a total of {0} words.".format(total_words))

            ttr.append(total_words)
        
        ttr_value = abs(reduce(lambda x, y: x-y,ttr))

        print(ttr_value)

        if ttr_value < 3000:
            print("TTR is not a reliable comparison for chosen texts.")
        else:
            print("TTR is between comparable texts.")

        search_phrase = input("enter a word to search for in books:  \n")
        
        for k,v in book_words.items():
            if search_phrase in v:
                print(f"Your search word '{search_phrase}' was found in {k}\n")

        to_continue = input("Do you want to replay.?\nType 'Y' or any key to quit.\n")

        if to_continue.lower() == "y":
            valid_selection = False
            

    # join the words in the list with new line chars
    #write_results("perline.txt", "\n".join(words), "utf-8")
# end def main():

if __name__ == "__main__":
    main()
