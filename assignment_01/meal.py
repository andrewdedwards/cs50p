#convert time (string) argument to time (floating point)
def convert(t_string):
    h, m = t_string.split(":")
    t_float = int(h) + int(m) / 60
    return(t_float)

#figures out which meal it's time for
def which_meal(time):
    if 7 <= time <= 8:
         return "breakfast"
    elif 12 <= time <= 13:
         return "lunch"
    elif 18 <= time <= 19:
         return "dinner"
    else:
         return 0

def main():
    #request user time input in ##.## or #.## (24 hr format)
    time_entry= input("what time is it? ")
    time_formatted = convert(time_entry)
    meal = which_meal(time_formatted)
    if meal != 0:
            print(f"it's {meal} time")

if __name__ == "__main__":       
    main()
