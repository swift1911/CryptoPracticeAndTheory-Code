word_list=''
with open("input.txt") as dictionary:
    word_list += dictionary.read()

COPRIMES_TO_26 = [3,5,7,11,15,17,19,21,23,25]

def shift_alphabet(word,operation):
    output = ''
    for letter in word:
        letter_as_number = ord(letter) - ord('A')
        shifted_letter_as_number = operation(letter_as_number) % 26
        output += chr(shifted_letter_as_number + ord('A'))
    return output

def score_word(word):
    return word.lower() in word_list

def solve_affine(ciphertext):
    """ Assumes ciphertext is a string composed of only spaces and
        letters. """
    solutions = []
    words = ciphertext.split()
    for addition_factor in range(1,27):
        for multiplication_factor in COPRIMES_TO_26:
            # affine shift
            shift_operation = lambda letter: (letter*multiplication_factor) + addition_factor
            # apply to all words
            solution = list(map(lambda word: shift_alphabet(word,shift_operation), words))
            solution_score = sum(map(score_word,solution))
            solutions.append((solution_score, solution))
    # return the best scoring solution
    return " ".join(sorted(solutions)[-1][1])

print(word_list.replace('\n',''))
print(solve_affine(word_list.replace('\n','')))