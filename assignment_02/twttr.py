message = input("Input: ")

for char in message:
    match char.lower():
        case "a" | "e" | "i" | "o" | "u":
            print("", end='', sep='')
        case _: 
            print(char, end='', sep='')