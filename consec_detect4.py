# Detection of consecutive patterns of length 4

# Detects the pattern 0123.


def detect0123(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] < sequence[index + 1] < sequence[index + 2] <\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 0132.


def detect0132(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] < sequence[index + 1] < sequence[index + 3] <\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 0213.


def detect0213(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] < sequence[index + 2] < sequence[index + 1] <\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 0231.


def detect0231(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] < sequence[index + 3] < sequence[index + 1] <\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 0312.


def detect0312(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] < sequence[index + 2] < sequence[index + 3] <\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 0321.


def detect0321(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] < sequence[index + 3] < sequence[index + 2] <\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 1023.


def detect1023(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] < sequence[index] < sequence[index + 2] <\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 1032.


def detect1032(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] < sequence[index] < sequence[index + 3] <\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 1203.


def detect1203(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 2] < sequence[index] < sequence[index + 1] <\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 1230.


def detect1230(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 3] < sequence[index] < sequence[index + 1] <\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 1302.


def detect1302(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 2] < sequence[index] < sequence[index + 3] <\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 1320.


def detect1320(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 3] < sequence[index] < sequence[index + 2] <\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 2013.


def detect2013(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] < sequence[index + 2] < sequence[index] <\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 2031.


def detect2031(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] < sequence[index + 3] < sequence[index] <\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 2103.


def detect2103(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 2] < sequence[index + 1] < sequence[index] <\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 2130.


def detect2130(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 3] < sequence[index + 1] < sequence[index] <\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 2301.


def detect2301(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 2] < sequence[index + 3] < sequence[index] <\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 2310.


def detect2310(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 3] < sequence[index + 2] < sequence[index] <\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 3012.


def detect3012(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] < sequence[index + 2] < sequence[index + 3] <\
                sequence[index]:
            return True
        index += 1
    return False

# Detects the pattern 3021.


def detect3021(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] < sequence[index + 3] < sequence[index + 2] <\
                sequence[index]:
            return True
        index += 1
    return False

# Detects the pattern 3102.


def detect3102(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 2] < sequence[index + 1] < sequence[index + 3] <\
                sequence[index]:
            return True
        index += 1
    return False

# Detects the pattern 3120.


def detect3120(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 3] < sequence[index + 1] < sequence[index + 2] <\
                sequence[index]:
            return True
        index += 1
    return False

# Detects the pattern 3201.


def detect3201(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 2] < sequence[index + 3] < sequence[index + 1] <\
                sequence[index]:
            return True
        index += 1
    return False

# Detects the pattern 3210.


def detect3210(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 3] < sequence[index + 2] < sequence[index + 1] <\
                sequence[index]:
            return True
        index += 1
    return False

# Detects the pattern 0000.


def detect0000(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] == sequence[index + 1] == sequence[index + 2] ==\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 0001.


def detect0001(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] == sequence[index + 1] == sequence[index + 2] <\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 0010.


def detect0010(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] == sequence[index + 1] == sequence[index + 3] <\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 0100.


def detect0100(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] == sequence[index + 2] == sequence[index + 3] <\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 1000.


def detect1000(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] == sequence[index + 2] == sequence[index + 3] <\
                sequence[index]:
            return True
        index += 1
    return False

# Detects the pattern 1110.


def detect1110(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] == sequence[index + 1] == sequence[index + 2] >\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 1101.


def detect1101(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] == sequence[index + 1] == sequence[index + 3] >\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 1011.


def detect1011(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] == sequence[index + 2] == sequence[index + 3] >\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 0111.


def detect0111(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] == sequence[index + 2] == sequence[index + 3] >\
                sequence[index]:
            return True
        index += 1
    return False

# Detects the pattern 0011.


def detect0011(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] == sequence[index + 1] < sequence[index + 2] ==\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 0101.


def detect0101(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] == sequence[index + 2] < sequence[index + 1] ==\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 0110.


def detect0110(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] == sequence[index + 3] < sequence[index + 1] ==\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 1001.


def detect1001(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] == sequence[index + 2] < sequence[index] ==\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 1010.


def detect1010(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] == sequence[index + 3] < sequence[index] ==\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 1100.


def detect1100(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 2] == sequence[index + 3] < sequence[index] ==\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 0012.


def detect0012(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] == sequence[index + 1] < sequence[index + 2] <\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 0021.


def detect0021(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] == sequence[index + 1] < sequence[index + 3] <\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 0102.


def detect0102(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] == sequence[index + 2] < sequence[index + 1] <\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 0201.


def detect0201(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] == sequence[index + 2] < sequence[index + 3] <\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 0120.


def detect0120(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] == sequence[index + 3] < sequence[index + 1] <\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 0210.


def detect0210(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] == sequence[index + 3] < sequence[index + 2] <\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 1002.


def detect1002(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] == sequence[index + 2] < sequence[index] <\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 2001.


def detect2001(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] == sequence[index + 2] < sequence[index + 3] <\
                sequence[index]:
            return True
        index += 1
    return False

# Detects the pattern 1020.


def detect1020(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] == sequence[index + 3] < sequence[index] <\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 2010.


def detect2010(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] == sequence[index + 3] < sequence[index + 2] <\
                sequence[index]:
            return True
        index += 1
    return False

# Detects the pattern 1200.


def detect1200(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 2] == sequence[index + 3] < sequence[index] <\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 2100.


def detect2100(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 2] == sequence[index + 3] < sequence[index + 1] <\
                sequence[index]:
            return True
        index += 1
    return False

# Detects the pattern 1102.


def detect1102(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 2] < sequence[index] == sequence[index + 1] <\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 1120.


def detect1120(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 3] < sequence[index] == sequence[index + 1] <\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 1012.


def detect1012(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] < sequence[index] == sequence[index + 2] <\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 1210.


def detect1210(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 3] < sequence[index + 2] == sequence[index] <\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 1021.


def detect1021(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] < sequence[index] == sequence[index + 3] <\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 1201.


def detect1201(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 2] < sequence[index] == sequence[index + 3] <\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 0112.


def detect0112(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] < sequence[index + 1] == sequence[index + 2] <\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 2110.


def detect2110(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 3] < sequence[index + 1] == sequence[index + 2] <\
                sequence[index]:
            return True
        index += 1
    return False

# Detects the pattern 0121.


def detect0121(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] < sequence[index + 1] == sequence[index + 3] <\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 2101.


def detect2101(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 2] < sequence[index + 1] == sequence[index + 3] <\
                sequence[index]:
            return True
        index += 1
    return False

# Detects the pattern 0211.


def detect0211(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] < sequence[index + 2] == sequence[index + 3] <\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 2011.


def detect2011(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] < sequence[index + 2] == sequence[index + 3] <\
                sequence[index]:
            return True
        index += 1
    return False

# Detects the pattern 2201.


def detect2201(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 2] < sequence[index + 3] < sequence[index] ==\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 2210.


def detect2210(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 3] < sequence[index + 2] < sequence[index] ==\
                sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 2021.


def detect2021(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] < sequence[index + 3] < sequence[index] ==\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 2120.


def detect2120(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 3] < sequence[index + 1] < sequence[index] ==\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 2012.


def detect2012(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] < sequence[index + 2] < sequence[index] ==\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 2102.


def detect2102(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 2] < sequence[index + 1] < sequence[index] ==\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 0221.


def detect0221(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] < sequence[index + 3] < sequence[index + 1] ==\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 1220.


def detect1220(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 3] < sequence[index] < sequence[index + 1] ==\
                sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 0212.


def detect0212(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] < sequence[index + 2] < sequence[index + 1] ==\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 1202.


def detect1202(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 2] < sequence[index] < sequence[index + 1] ==\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 0122.


def detect0122(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index] < sequence[index + 1] < sequence[index + 2] ==\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects the pattern 1022.


def detect1022(sequence):
    index = 0
    while index < len(sequence) - 3:
        if sequence[index + 1] < sequence[index] < sequence[index + 2] ==\
                sequence[index + 3]:
            return True
        index += 1
    return False

# Detects a pattern in a sequence.
# Parameter: sequences is a list, pattern is a string.
# Return: True if the pattern is found and False otherwise.


def detect_pattern(sequence, pattern):
    if pattern == '0123':
        return detect0123(sequence)
    elif pattern == '0132':
        return detect0132(sequence)
    elif pattern == '0213':
        return detect0213(sequence)
    elif pattern == '0231':
        return detect0231(sequence)
    elif pattern == '0312':
        return detect0312(sequence)
    elif pattern == '0321':
        return detect0321(sequence)
    elif pattern == '1023':
        return detect1023(sequence)
    elif pattern == '1032':
        return detect1032(sequence)
    elif pattern == '1203':
        return detect1203(sequence)
    elif pattern == '1230':
        return detect1230(sequence)
    elif pattern == '1302':
        return detect1302(sequence)
    elif pattern == '1320':
        return detect1320(sequence)
    elif pattern == '2013':
        return detect2013(sequence)
    elif pattern == '2031':
        return detect2031(sequence)
    elif pattern == '2103':
        return detect2103(sequence)
    elif pattern == '2130':
        return detect2130(sequence)
    elif pattern == '2301':
        return detect2301(sequence)
    elif pattern == '2310':
        return detect2310(sequence)
    elif pattern == '3012':
        return detect3012(sequence)
    elif pattern == '3021':
        return detect3021(sequence)
    elif pattern == '3102':
        return detect3102(sequence)
    elif pattern == '3120':
        return detect3120(sequence)
    elif pattern == '3201':
        return detect3201(sequence)
    elif pattern == '3210':
        return detect3210(sequence)
    elif pattern == '0000':
        return detect0000(sequence)
    elif pattern == '0001':
        return detect0001(sequence)
    elif pattern == '0010':
        return detect0010(sequence)
    elif pattern == '0100':
        return detect0100(sequence)
    elif pattern == '1000':
        return detect1000(sequence)
    elif pattern == '1110':
        return detect1110(sequence)
    elif pattern == '1101':
        return detect1101(sequence)
    elif pattern == '1011':
        return detect1011(sequence)
    elif pattern == '0111':
        return detect0111(sequence)
    elif pattern == '0011':
        return detect0011(sequence)
    elif pattern == '0101':
        return detect0101(sequence)
    elif pattern == '0110':
        return detect0110(sequence)
    elif pattern == '1001':
        return detect1001(sequence)
    elif pattern == '1010':
        return detect1010(sequence)
    elif pattern == '1100':
        return detect1100(sequence)
    elif pattern == '0012':
        return detect0012(sequence)
    elif pattern == '0021':
        return detect0021(sequence)
    elif pattern == '0102':
        return detect0102(sequence)
    elif pattern == '0201':
        return detect0201(sequence)
    elif pattern == '0120':
        return detect0120(sequence)
    elif pattern == '0210':
        return detect0210(sequence)
    elif pattern == '1002':
        return detect1002(sequence)
    elif pattern == '2001':
        return detect2001(sequence)
    elif pattern == '1020':
        return detect1020(sequence)
    elif pattern == '2010':
        return detect2010(sequence)
    elif pattern == '1200':
        return detect1200(sequence)
    elif pattern == '2100':
        return detect2100(sequence)
    elif pattern == '1102':
        return detect1102(sequence)
    elif pattern == '1120':
        return detect1120(sequence)
    elif pattern == '1012':
        return detect1012(sequence)
    elif pattern == '1210':
        return detect1210(sequence)
    elif pattern == '1021':
        return detect1021(sequence)
    elif pattern == '1201':
        return detect1201(sequence)
    elif pattern == '0112':
        return detect0112(sequence)
    elif pattern == '2110':
        return detect2110(sequence)
    elif pattern == '0121':
        return detect0121(sequence)
    elif pattern == '2101':
        return detect2101(sequence)
    elif pattern == '0211':
        return detect0211(sequence)
    elif pattern == '2011':
        return detect2011(sequence)
    elif pattern == '2201':
        return detect2201(sequence)
    elif pattern == '2210':
        return detect2210(sequence)
    elif pattern == '2021':
        return detect2021(sequence)
    elif pattern == '2120':
        return detect2120(sequence)
    elif pattern == '2012':
        return detect2012(sequence)
    elif pattern == '2102':
        return detect2102(sequence)
    elif pattern == '0221':
        return detect0221(sequence)
    elif pattern == '1220':
        return detect1220(sequence)
    elif pattern == '0212':
        return detect0212(sequence)
    elif pattern == '1202':
        return detect1202(sequence)
    elif pattern == '0122':
        return detect0122(sequence)
    elif pattern == '1022':
        return detect1022(sequence)

# Counts the number of sequences in a collection that avoid a given pattern.
# Parameter: collection is a list of lists, pattern is a string.
# Return: an integer.


def count_avoid(collection, pattern):
    count = 0
    for sequence in collection:
        if not detect_pattern(sequence, pattern):
            count += 1
    return count

# Finds the sequences in a collection that avoid a given pattern.
# Parameter: collection is a list of lists, pattern is a string.
# Return: a list of lists.


def find_avoid(collection, pattern):
    avoiding = list()
    for sequence in collection:
        if not detect_pattern(sequence, pattern):
            avoiding.append(sequence)
    return avoiding
