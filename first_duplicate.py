# Given a list of numbers, find the first duplicate number. If there’s no duplicate, print "No duplicates found".

def all_duplicate(lst):
    seen = set()
    duplicates = set()
    for num in lst:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return duplicates if duplicates else "No duplicates found"

def first_duplicate(lst):
    seen = set()
    for num in lst:
        if num in seen:  # Checking membership in a set is O(1)
            return num, seen
        seen.add(num)
    return "No duplicates found"

init_list = [5, 8, 2, 9, 6, 7, 9, 5]
print(all_duplicate(init_list))