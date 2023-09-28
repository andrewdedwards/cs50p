# user input
expression = input("expression: ")

# generate list var from expression
expression_list = expression.strip().split(" ")

# format list elements 
x = float(expression_list[0])
y = expression_list[1]
z = float(expression_list[2])


# math
match expression_list[1]:
    case "+":
        solution = x + z

match expression_list[1]:
    case "-":
        solution = x - z

match expression_list[1]:
    case "*":
        solution = x * z

match expression_list[1]:
    case "/":
        solution = x / z

# output
print (solution)