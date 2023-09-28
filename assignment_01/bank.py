# Prompt user for greeting
greeting = input("Greeting: ")

# Remove greeting case
greeting = greeting.lower().strip()

# Respond based on greeting characteristics
if greeting == "hello":
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")