# This is a test change
input = raw_input

total = input("what would you like, you can type furniture or tech or car parts or mattresses: ")

if total == "furniture":
        sectionFruniture = input("would you like a couch or a chair or a table")
        if sectionFruniture == "couch":
            print("we have couches from ikea")
        if sectionFruniture == "chair":
            print("we have chairs from ikea")
        if sectionFruniture == "table":
            print("we have tables from ikea")


if total == "tech":
    sectionTech = input("")

if total == "car parts":
    sectionCarParts = input("")

if total == "mattresses":
    sectionMattresses = input("")
