
while True:
    try:
        f = input()
        s = input()

        # Convert both strings to lowercase for case-insensitive comparison
        f = f.lower()
        s = s.lower()

        # Compare the two strings lexicographically
        if f < s:
            print("-1")
        elif f > s:
            print("1")
        else:
            print("0")
    except EOFError:
        break
