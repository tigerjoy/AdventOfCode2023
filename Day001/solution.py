def get_first_digit(line):
    for ch in line:
        if ch.isdigit():
            return int(ch)
    return 0

def get_last_digit(line):
    i = len(line) - 1
    while i >= 0:
        ch = line[i]
        if ch.isdigit():
            return int(ch)
        i -= 1

def get_number(line):
    return get_first_digit(line) * 10 + get_last_digit(line)

if __name__ == "__main__":
    with open("input.txt", "r") as file:
      total = 0
      for line in file:
        total += get_number(line)
    
    with open("output.txt", "w") as file:
        file.write(f"{total}")
