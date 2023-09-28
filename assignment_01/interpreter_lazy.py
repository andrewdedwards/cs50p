# user input
expression = input("expression: ")

# generate list var from expression
#expression_list = expression.strip().split(" ")
#x, y, z = [expression_list[i] for i in (0, 1, 2)]

x, y, z = expression.strip().split(" ")

# math
solution = float(eval(f"{x}{y}{z}"))

# output
print(float(solution))

