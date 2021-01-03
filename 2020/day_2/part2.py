def check_validation(text: str):
    """Check password is valid or not
    """
    holder = text.split()
    indexes = holder[0].split('-')
    fx = int(indexes[0])
    sx = int(indexes[1])
    ch = holder[1][0]
    pw = holder[2]

    if (pw[fx-1]==ch) ^ (pw[sx-1]==ch):
        return True
    return False


if __name__ == "__main__":
    result = 0
    with open("input.txt") as File:
        Lines = File.readlines()
        for line in Lines:
            if check_validation(line):
                result += 1
    print(result)
