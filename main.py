def permutation(x, y):
    final = []
    output = []
    sub = []

    while not set(x) == set(final):
        sub.clear()
        cp = set(final)
        rem = [item for item in x if item not in cp]

        loc = x.index(rem[0])
        char = ''

        first = x[loc]
        final.append(first)
        sub.append(first)

        while char != first:
            char = y[loc]
            if char != first:
                final.append(char)
                sub.append(char)
            loc = x.index(char)

        output.append(sub[:])

    return output


if __name__ == "__main__":
    x = ['B', 'G', 'F', 'D', 'E', 'A', 'C']
    y = ['F', 'C', 'E', 'D', 'A', 'B', 'G']
    print(permutation(x, y))
