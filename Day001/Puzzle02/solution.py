import sys


digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
three_letter_digits = ["one", "two", "six"]
four_letter_digits = ["four", "five","nine"]
five_letter_digits = ["three", "seven", "eight"]

def get_first_digit(line, debug = False):
    three_letter_buffer = ""
    three_buffer_len = 0

    four_letter_buffer = ""
    four_buffer_len = 0

    five_letter_buffer = ""
    five_buffer_len = 0

    for ch in line:
        three_letter_buffer += ch
        three_buffer_len += 1

        four_letter_buffer += ch
        four_buffer_len += 1

        five_letter_buffer += ch
        five_buffer_len += 1

        if debug:
          print("ch =", ch)
          print("three_letter_buffer =", three_letter_buffer)
          print("four_letter_buffer =", four_letter_buffer)
          print("five_letter_buffer =", five_letter_buffer)
          print()

        if ch.isdigit():
            return int(ch)
        
        if three_buffer_len == 3:
            if three_letter_buffer in three_letter_digits:
                return digits.index(three_letter_buffer) + 1
            # Drop the first letter
            three_letter_buffer = three_letter_buffer[1:]
            three_buffer_len -= 1
        
        if four_buffer_len == 4:
            if four_letter_buffer in four_letter_digits:
                return digits.index(four_letter_buffer) + 1
            # Drop the first letter
            four_letter_buffer = four_letter_buffer[1:]
            four_buffer_len -= 1
        
        if five_buffer_len == 5:
            if five_letter_buffer in five_letter_digits:
                return digits.index(five_letter_buffer) + 1
            # Drop the first letter
            five_letter_buffer = five_letter_buffer[1:]
            five_buffer_len -= 1
                
    return 0

def get_last_digit(line, debug = False):
    three_letter_buffer = ""
    three_buffer_len = 0

    four_letter_buffer = ""
    four_buffer_len = 0

    five_letter_buffer = ""
    five_buffer_len = 0

    i = len(line) - 1
    while i >= 0:
        ch = line[i]

        three_letter_buffer = ch + three_letter_buffer
        three_buffer_len += 1

        four_letter_buffer = ch + four_letter_buffer
        four_buffer_len += 1

        five_letter_buffer = ch + five_letter_buffer
        five_buffer_len += 1
        
        if debug:
          print("ch =", ch)
          print("three_letter_buffer =", three_letter_buffer)
          print("four_letter_buffer =", four_letter_buffer)
          print("five_letter_buffer =", five_letter_buffer)
          print()

        if ch.isdigit():
            return int(ch)

        if three_buffer_len == 3:
            if three_letter_buffer in three_letter_digits:
                return digits.index(three_letter_buffer) + 1
            # Drop the first letter
            three_letter_buffer = three_letter_buffer[:-1]
            three_buffer_len -= 1
        
        if four_buffer_len == 4:
            if four_letter_buffer in four_letter_digits:
                return digits.index(four_letter_buffer) + 1
            # Drop the first letter
            four_letter_buffer = four_letter_buffer[:-1]
            four_buffer_len -= 1
        
        if five_buffer_len == 5:
            if five_letter_buffer in five_letter_digits:
                return digits.index(five_letter_buffer) + 1
            # Drop the first letter
            five_letter_buffer = five_letter_buffer[:-1]
            five_buffer_len -= 1

        i -= 1

def get_number(line):
    line = line.strip()
    return get_first_digit(line) * 10 + get_last_digit(line)

if __name__ == "__main__":
    # line = "eight2sevenkl"
    # print("get_first_digit")
    # first_digit = get_first_digit(line, debug=True)
    # print("first_digit =", first_digit)

    # print("get_last_digit")
    # last_digit = get_last_digit(line, debug=True)
    # print("last_digit =", last_digit)
    # sys.exit(0)
    with open("input.txt", "r") as file, open("debug.txt", "w") as dbg_file:
      total = 0
      for line in file:
        num = get_number(line)
        total += num
        dbg_file.write(f"{line} --> {num}\n")
    
    with open("output.txt", "w") as file:
        file.write(f"{total}")
