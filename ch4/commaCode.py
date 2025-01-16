spam = ['apples', 'banana', 'tofu', 'cats']
cheese = ['moose']
print(spam)
print(cheese)

def commaCode(list_here):
    if len(list_here) > 1:
        print(", ".join(list_here[:-1]) + ", and " + list_here[-1])

    else:
        print("There's only a " + str(list_here[0]) + " here")

commaCode(spam)
commaCode(cheese)