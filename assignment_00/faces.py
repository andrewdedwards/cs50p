def convert(text):
    converted = text.replace(":)","🙂").replace(":(","🙃")
    print("Here is your fixed message, you classless bafoon:\n",converted)

def main():
    convert(input("Enter some text with smiley faces but not emojis you early 2000s hack: "))
    
main()
