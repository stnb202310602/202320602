string = "This is a more advanced comprehension exercise to practice".split()

filtering = [i[::-1] for i in string if 5 <= len(i)]
print(filtering)