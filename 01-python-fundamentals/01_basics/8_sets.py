# in , | , & , -

vowel = {'a','e','u'}
other = {'a','b','c','d','e'}

wor = vowel | other # used for union

print(f"{wor}")

inter = vowel & other

print(f"{inter}")

unique_only_in_vowel = vowel - other

print(f"{unique_only_in_vowel}")

print(f"present in vowel ;{'a' in vowel}")

# there is a concept of frozen set too