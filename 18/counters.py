def count_lines(f):
    lines = 0
    for line in f:
        lines += 1
    return lines


def count_chars(f):
    chars = 0
    for line in f:
        lines = line.split()
        chars += sum(len(word) for word in lines)
    return chars


def main(filename):
    with open(filename) as f:
        print(count_lines(f))
        f.seek(0)
        print(count_chars(f))


if __name__ == "__main__":
    main("./lessons/18/counters.txt")
