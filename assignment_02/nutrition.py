'''
fruits = [
    {"name" : "apple", "calories" : "130"},
    {"name" : "avocado", "calories" : "50"},
    {"name" : "banana", "calories" : "110"},
    {"name" : "cantaloupe", "calories" : "50"},
    {"name" : "grapefruit", "calories" : "60"},
    {"name" : "grapes", "calories" : "90"},
    {"name" : "honeydew melon", "calories" : "50"},
    {"name" : "kiwifruit", "calories" : "90"},
    {"name" : "lemon", "calories" : "15"},
    {"name" : "lime", "calories" : "20"},
    {"name" : "nectarine", "calories" : "60"},
    {"name" : "orange", "calories" : "80"},
    {"name" : "peach", "calories" : "60"},
    {"name" : "pear", "calories" : "100"},
    {"name" : "pineapple", "calories" : "50"},
    {"name" : "plums", "calories" : "70"},
    {"name" : "strawberries", "calories" : "50"},
    {"name" : "sweet cherries", "calories" : "100"},
    {"name" : "tangerine", "calories" : "50"},
    {"name" : "watermelon", "calories" : "80"},
]
'''
fruits = {
    "apple" : "130",
    "avocado" : "50",
    "banana" : "110",
    "cantaloupe" : "50",
    "grapefruit" : "60",
    "grapes" : "90",
    "honeydew melon" : "50",
    "kiwifruit" : "90",
    "lemon" : "15",
    "lime" : "20",
    "nectarine" : "60",
    "orange" : "80",
    "peach" : "60",
    "pear" : "100",
    "pineapple" : "50",
    "plums" : "70",
    "strawberries" : "50",
    "sweet cherries" : "100",
    "tangerine" : "50",
    "watermelon" : "80",
}
item = input("Item: ").lower()

if item in fruits:
    print(fruits[item])