"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_in_string = open(file_path).read()


    return file_in_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = open_and_read_file(input_path)
    words = words.split()
  

    for i in range(len(words)-2):
        key = (words[i], words[i+1]) 
        if key in chains:
            value_list = chains[key]
            value_list.append(words[i+2])
            chains[key] = value_list          
    
        else:
            first_value_list = []
            first_value_list.append(words[i+2])
            chains[key] = first_value_list
        
    return chains
    

def make_text(chains):
    """Return text from chains."""
    chains_dict = make_chains(input_text)
    words = []
    random_key = choice(list(chains_dict))
    words.extend(list(random_key))

    while True:
        try:
            random_dict_value = choice(list(chains_dict[random_key])) 
            next_tuple = (random_key[1], random_dict_value)
            words.append(random_dict_value)
            random_key = next_tuple
        except KeyError:
            break    

    return " ".join(word for word in words)

input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
