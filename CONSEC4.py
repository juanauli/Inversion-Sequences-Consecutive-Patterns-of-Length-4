# Finding and counting inversion sequences avoiding consecutive
# patterns of length 4
# Uses the file consec_detect4.py and gen_inv_seq.py


import consec_detect4
import gen_inv_seq

# Counts the number of inversion sequences of a given length
# that avoid a given consecutive pattern of length 4.
# Parameters: length is an integer, pattern is a string.
# Returns the number of inversion sequences of the given length
# that avoid the pattern, an integer.


def count_inv_avoiding4(length, pattern):
    return consec_detect4.count_avoid(gen_inv_seq.inv_seq(length), pattern)

# Finds the inversion sequences of a given length that avoid
# a given consecutive pattern of length 4.
# Parameters: length is an integer, pattern is a string.
# Returns the inversion inversion sequences of the given length
# that avoid the pattern, a list.


def find_inv_avoiding4(length, pattern):
    return consec_detect4.find_avoid(gen_inv_seq.inv_seq(length), pattern)
