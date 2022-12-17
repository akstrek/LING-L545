import sys

text_line = sys.stdin.readline()

while text_line is not '':
    for text in '.':
        text_line = text_line.replace(text, text + '\n')

    sys.stdout.write(text_line)

    text_line = sys.stdin.readline()