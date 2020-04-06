##
# count lines when char's in txt file
##


def count_lines(file="./counters.txt"):
    lines = 0
    with open(file) as f:
        for line in f:
            lines += 1
        return lines


def count_chars(file="./counters.txt"):
    chars = 0
    with open(file) as f:
        for line in f:
            lines = line.split()
            chars += sum(len(word) for word in lines)
        return chars


if __name__ == "__main__":
    print("lines: ", count_lines())
    print("chars: ", count_chars())
