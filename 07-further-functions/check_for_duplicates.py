data_list = [1, 1, 1, 2, 3, 2, 3, 4, 6, 8, 1, 0]

# Get a list of all duplicated values
duplicates = list(filter(lambda i: data_list.count(i) > 1, data_list))
print(duplicates)

# Just the values that have duplicates
duplicated_values = set(filter(lambda i: data_list.count(i) > 1, data_list))
print(duplicated_values)


# Get a count of each duplicate value
dupes = filter(lambda i: data_list.count(i) > 1, data_list)
dupe_count = set((i, data_list.count(i)) for i in dupes)
print(dupe_count)
