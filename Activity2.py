# Function to check whether
# first and last character of strings are the same
def find_matching_strings(items):
    counter = 0
    matching_items = []

    for item in items:
        if len(item) > 1 and item[0] == item[-1]:
            counter += 1
            matching_items.append(item)

    print("Strings with matching first and last character:\n", matching_items)
    return counter


total = find_matching_strings(['level', 'apple', 'radar', 'hello', 'civic'])

print("Total number of strings with same first and last character:", total)
