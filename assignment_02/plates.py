def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # check punctuation and space rules
    punc = ''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in s:
        if char in punc:
            return False
        
    # check string length rules
    if len(s) > 6 or len(s) < 2:
        return False
    
    # check first two charss are alphabetical rule
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    
    for _ in range(1, len(s)-1):
        if s[_].isalpha() == True and s[_ + 1].isalpha() == False:  # checks for alpha char followed by num char
            # checks first number is not zero
            if s[_ + 1] == "0":
                 return False            
            # checks rest of string after alpha char for num char
            for i in range(_, len(s)-1):
                    if s[i].isalpha()  == False and s[i + 1].isalpha() == True:
                            return False
  
    return True

main()
