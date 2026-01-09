def space_invader() -> str:
    """String representing a space invader.magic mou"""
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