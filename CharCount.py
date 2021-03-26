from os import strerror

f = 'CharCountText.txt'
char_dict = {}

try:
    with open(f, 'r') as stream:
        ch = stream.read(1)
        while ch:
            if ch.isalpha():
                ch = ch.lower()
                if ch in char_dict:
                    char_dict[ch] += 1
                else:
                    char_dict[ch] = 1
            ch = stream.read(1)

except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)

for ch in sorted(char_dict.keys()):
    print(f"{ch} -> {char_dict[ch]}")
