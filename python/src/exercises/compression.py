<<<<<<< HEAD
"""Implementing lossless compression techniques."""

def rle_simple(input_str: str) -> str:
    """Perform run-length encoding on the input string. The output is in 
    the form "cNdM...", where 'c' and 'd' are characters from the input, 
    and 'N' and 'M' are the numbers of time they are repeated. Only works 
    for input strings that don't contain numbers...why?
    """
    output = ''

    # We start with the first character
    count = 1

    # Loop through the string starting from the second character
    for i in range(1, len(input_str)):

        # If the current character is the same as the previous one
        if input_str[i] == input_str[i - 1]:
            count += 1  # Increment the count
        else:

            # Add previous character and its count to output
            output += f"{input_str[i - 1]}{count}"

            # Reset count for the new character
            count = 1

    # After the loop, we still need to add the last character group
    output += f"{input_str[-1]}{count}"

    return output

def rle_simple_expand(compressed_str: str) -> str:
    """Expand run-length encoding of the kind produced by rle_simple.
    """
    output = ''
    count = 0
    while count < len(compressed_str):
        output += compressed_str[count]*compressed_str[count+1]
        count += 2
    return output

def rle(the_input: str) -> list:
    """Apply run length encoding."""
    # We start with the first character
    output = [(the_input[0],1)]
    # Loop through the string starting from the second character
    for i in range(1, len(the_input)):
        # If the current character is the same as the previous one
        if the_input[i] == output[-1][0]:
            output[-1] = (output[-1][0], output[-1][1]+1)
        else:
            # Add current character and its count to output
            output.append((the_input[i],1))
    return output

def rle_rec(the_input: list) -> list:
    """A version of rle that uses a recursive helper function. This version
    returns a list of tuples (char, count).
    This version uses too much memory to be used on large texts.
    """
    if len(the_input) == 0:
        return []
    else:
        # call the helper function, passing in the first char and count of 1, 
        # and the tail of the list
        return rle_rec_helper((the_input[0],1), the_input[1:])

def rle_rec_helper(current, the_input):
    """A recursive function that counts how many times a character appears
    in succession, returning a list of (car, count) tuples."""
    if len(the_input) == 0:
        # input has ended, return a list with just the last character group in it
        return [current]
    elif current[0] == the_input[0]:
        # input continues with a duplicate. The function calls itself with
        # an incremented count and the tail of the list.  
        return rle_rec_helper((current[0], current[1]+1), the_input[1:])
    else:
        # input continues with a new char. The function adds the previous (char, count)
        # tuple to the list and calls itself with the next character group.
        return [current] + rle_rec_helper((the_input[0],1), the_input[1:])

def rle_expand(the_input: list) -> str:
    """Expand a run length encoded list"""
    result = ""
    for char,count in the_input:
        result += char*count
    return result

def space_invader() -> str:
    width = 28
    white = '_'
    black = 'X'
    all_white = width*white
    output = (all_white+'\n')*3
    output += 11*white + 6*black + 11*white + '\n'
    output += 10*white + black + 6*white + black + 10*white + '\n'
    output += 9*white + black + 8*white + black + 9*white + '\n'
    output += 9*white + black + white + black*2 + 2*white + black*2 + white + black + 9*white + '\n'
    output += 9*white + black + white + black*2 + 2*white + black*2 + white + black + 9*white + '\n'
    output += 10*white + black + 2*white + 2*black + 2*white + black + 10*white + '\n'
    output += 11*white + 2*black + 2*white + 2*black + 11*white + '\n'
    output += 8*white + black + 10*white + black + 8*white + '\n'
    output += 8*white + black + 2*white + 6*black + 2*white + black + 8*white + '\n'
    output += 8*white + black + 2*white + 6*black + 2*white + black + 8*white + '\n'
    output += 11*white + 2*black + 2*white + 2*black + 11*white + '\n'
    output += 10*white + black + white + black + 2*white + black + white + black + 10*white + '\n'
    output += 10*white + black + white + black + 2*white + black + white + black + 10*white + '\n'
    output += 9*white + black + white + black + 4*white + black + white + black + 9*white + '\n'
    output += (all_white+'\n')*3
    return output
    

def bwt(the_input: str) -> str:
    """Transform some text with the BWT."""
    # Append beginning and end markers.
    # Rather than the usual ^ and $, we use { and } as this makes sorting easier.
    current = "{" + the_input + "}"
    # start the table with the first row
    table = [current]
    # add all possible rotations to the table 
    for _ in range(len(the_input)+1):
        current = current[-1] + current[0:-1]
        table.append(current)
    # sort the table
    table.sort()
    # pull the last column out of the table
    result = ''
    for row in table:
        result += row[-1]
    return result

def bwt_invert(the_input: str) -> str:
    """Invert a BWT."""
    # create empty table
    table = []
    for _ in range(len(the_input)):
        table.append("")
    # add columns and sort
    for _ in range(len(the_input)):
        for i,c in enumerate(the_input):
            table[i] = c + table[i]
        table.sort()
    # find the row with markers in the right place
    for row in table:
        if row[0] == '{' and row[-1] == '}':
            # return row without the markers
            return row[1:-1]

def compress(the_input: str) -> list:
    """Compress some input by applying a BWT then RLE."""
    bwt_enc = bwt(the_input)
    return rle(bwt_enc)
    
def decompress(the_input: list) -> str:
    """Decompress some input by inverting RLE then inverting BWT."""
    exp = rle_expand(the_input)
    return bwt_invert(exp)

test_str = "THE.MAN.AND.THE.DOG.WAITED.AT.THE.STATION.FOR.THE.TRAIN.TO.THE.CITY"

def test_book():
    with open('the_tempest.txt', encoding="utf8") as book:
        first_100 = [next(book).strip() for _ in range(100)]
        first_100 = ' '.join(first_100)
        cmp = compress(first_100)
        decmp = decompress(cmp)
        compression = 100 - (len(cmp)/len(first_100))*100
        print(f"Compression achieved: {compression:.2f}%")
        assert(first_100 == decmp)
        
=======
"""Implementing lossless compression techniques."""

def rle_simple(input_str: str) -> str:
    """Perform run-length encoding on the input string. The output is in 
    the form "cNdM...", where 'c' and 'd' are characters from the input, 
    and 'N' and 'M' are the numbers of time they are repeated. Only works 
    for input strings that don't contain numbers...why?
    """
    output = ''

    # We start with the first character
    count = 1

    # Loop through the string starting from the second character
    for i in range(1, len(input_str)):

        # If the current character is the same as the previous one
        if input_str[i] == input_str[i - 1]:
            count += 1  # Increment the count
        else:

            # Add previous character and its count to output
            output += f"{input_str[i - 1]}{count}"

            # Reset count for the new character
            count = 1

    # After the loop, we still need to add the last character group
    output += f"{input_str[-1]}{count}"

    return output

def rle_simple_expand(compressed_str: str) -> str:
    """Expand run-length encoding of the kind produced by rle_simple.
    """
    output = ''
    count = 0
    while count < len(compressed_str):
        output += compressed_str[count]*compressed_str[count+1]
        count += 2
    return output

def rle(the_input: str) -> list:
    """Apply run length encoding."""
    # We start with the first character
    output = [(the_input[0],1)]
    # Loop through the string starting from the second character
    for i in range(1, len(the_input)):
        # If the current character is the same as the previous one
        if the_input[i] == output[-1][0]:
            output[-1] = (output[-1][0], output[-1][1]+1)
        else:
            # Add current character and its count to output
            output.append((the_input[i],1))
    return output

def rle_rec(the_input: list) -> list:
    """A version of rle that uses a recursive helper function. This version
    returns a list of tuples (char, count).
    This version uses too much memory to be used on large texts.
    """
    if len(the_input) == 0:
        return []
    else:
        # call the helper function, passing in the first char and count of 1, 
        # and the tail of the list
        return rle_rec_helper((the_input[0],1), the_input[1:])

def rle_rec_helper(current, the_input):
    """A recursive function that counts how many times a character appears
    in succession, returning a list of (car, count) tuples."""
    if len(the_input) == 0:
        # input has ended, return a list with just the last character group in it
        return [current]
    elif current[0] == the_input[0]:
        # input continues with a duplicate. The function calls itself with
        # an incremented count and the tail of the list.  
        return rle_rec_helper((current[0], current[1]+1), the_input[1:])
    else:
        # input continues with a new char. The function adds the previous (char, count)
        # tuple to the list and calls itself with the next character group.
        return [current] + rle_rec_helper((the_input[0],1), the_input[1:])

def rle_expand(the_input: list) -> str:
    """Expand a run length encoded list"""
    result = ""
    for char,count in the_input:
        result += char*count
    return result

def space_invader() -> str:
    width = 28
    white = '_'
    black = 'X'
    all_white = width*white
    output = (all_white+'\n')*3
    output += 11*white + 6*black + 11*white + '\n'
    output += 10*white + black + 6*white + black + 10*white + '\n'
    output += 9*white + black + 8*white + black + 9*white + '\n'
    output += 9*white + black + white + black*2 + 2*white + black*2 + white + black + 9*white + '\n'
    output += 9*white + black + white + black*2 + 2*white + black*2 + white + black + 9*white + '\n'
    output += 10*white + black + 2*white + 2*black + 2*white + black + 10*white + '\n'
    output += 11*white + 2*black + 2*white + 2*black + 11*white + '\n'
    output += 8*white + black + 10*white + black + 8*white + '\n'
    output += 8*white + black + 2*white + 6*black + 2*white + black + 8*white + '\n'
    output += 8*white + black + 2*white + 6*black + 2*white + black + 8*white + '\n'
    output += 11*white + 2*black + 2*white + 2*black + 11*white + '\n'
    output += 10*white + black + white + black + 2*white + black + white + black + 10*white + '\n'
    output += 10*white + black + white + black + 2*white + black + white + black + 10*white + '\n'
    output += 9*white + black + white + black + 4*white + black + white + black + 9*white + '\n'
    output += (all_white+'\n')*3
    return output
    

def bwt(the_input: str) -> str:
    """Transform some text with the BWT."""
    # Append beginning and end markers.
    # Rather than the usual ^ and $, we use { and } as this makes sorting easier.
    current = "{" + the_input + "}"
    # start the table with the first row
    table = [current]
    # add all possible rotations to the table 
    for _ in range(len(the_input)+1):
        current = current[-1] + current[0:-1]
        table.append(current)
    # sort the table
    table.sort()
    # pull the last column out of the table
    result = ''
    for row in table:
        result += row[-1]
    return result

def bwt_invert(the_input: str) -> str:
    """Invert a BWT."""
    # create empty table
    table = []
    for _ in range(len(the_input)):
        table.append("")
    # add columns and sort
    for _ in range(len(the_input)):
        for i,c in enumerate(the_input):
            table[i] = c + table[i]
        table.sort()
    # find the row with markers in the right place
    for row in table:
        if row[0] == '{' and row[-1] == '}':
            # return row without the markers
            return row[1:-1]

def compress(the_input: str) -> list:
    """Compress some input by applying a BWT then RLE."""
    bwt_enc = bwt(the_input)
    return rle(bwt_enc)
    
def decompress(the_input: list) -> str:
    """Decompress some input by inverting RLE then inverting BWT."""
    exp = rle_expand(the_input)
    return bwt_invert(exp)

test_str = "THE.MAN.AND.THE.DOG.WAITED.AT.THE.STATION.FOR.THE.TRAIN.TO.THE.CITY"

def test_book():
    with open('the_tempest.txt', encoding="utf8") as book:
        first_100 = [next(book).strip() for _ in range(100)]
        first_100 = ' '.join(first_100)
        cmp = compress(first_100)
        decmp = decompress(cmp)
        compression = 100 - (len(cmp)/len(first_100))*100
        print(f"Compression achieved: {compression:.2f}%")
        assert(first_100 == decmp)
        
>>>>>>> e17717b004d54d8ef3892e881679ca9d7103cd3d
    