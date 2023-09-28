# requests file name with extension
file_name = input("Enter a filename: ")

# parse extension
file_extension = file_name.lower().rsplit(".",1)[1]

#extension correction
if file_extension == "jpg":
    file_extension = "jpeg"

# categorize extension
match file_extension:
    case "gif" | "jpg" | "jpeg" | "png":
        file_category = "image"
    case "zip" | "pdf":
        file_category = "application"
    case "txt":
        file_category = "text"

# output with type and extension
print(file_category,"/",file_extension, sep='')