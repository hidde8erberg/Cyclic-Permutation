def permutation(x,y):
    final = []

    while not set(x) == set(final):
        cp = set(final)
        rem = [item for item in x if item not in cp]

        loc = x.index(rem[0])
        char = ''

        first = x[loc]
        final.append(first)
    
        while char != first:
            char = y[loc]
            if char != first: final.append(char)
            loc = x.index(char) 
    
    return final

if __name__ == "__main__":
    x = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    y = ['F', 'C', 'E', 'D', 'A', 'B', 'G']
    print(permutation(x,y)) 
