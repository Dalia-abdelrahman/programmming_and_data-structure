def islower(c):
    # Check if the character's Unicode code point is between that of 'a' and 'z'
    return ord('a') <= ord(c) <= ord('z')

print(islower('c'))