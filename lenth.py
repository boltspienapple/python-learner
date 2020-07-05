# Add your code here.
def total_length(list_of_strings):
    total = 0
    for string in list_of_strings:
        total = total + len(string)
    return total
# Should return 6:
print(total_length(['foo', 'bar']))

# Should return 0 (it's an empty list):
print(total_length([]))