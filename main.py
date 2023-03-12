f = open("Hello.bf", "r")
code = f.read()

f.close()

pointer = 0
tape = [0] * 1000

i = 0
while i < len(code):
   
    current = code[i]
    if current == '>':
        pointer += 1

    if current == '<':
        pointer -= 1

    if current == '+':
        tape[pointer] += 1

    if current == '-':
        tape [pointer] -= 1

    if current == '.':
        char = chr(tape[pointer])
        print (char, end="")
    if current == ',':
        i = input()
        tape[pointer] = ord(i)
    
    if current == '[':
        if tape[pointer] == 0:
            depth = 1
            while depth > 0:
                i += 1
                if code[i] == '[': 
                    depth += 1
                if code[i] == ']':
                    depth -= 1
            i += 1

    if current == ']':
        if tape[pointer] != 0:
            depth = 1
            while depth > 0:
                i-=1
                if code[i] == '[':
                    depth -= 1
                if code[i] == ']':
                    depth += 1
            i -= 1
    i += 1
