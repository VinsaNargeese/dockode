rows = int(input("enter rows"))
columns = int(input("enter columns"))
for r in range(rows):
    if not r:
        for c in range(columns-rows+1):
            print(" ___   ", end=" ")
        print()

    for c in range(columns-rows):
        print("/   \\___", end="")
    print("/   \\", end="")
    print()

    for c in range(columns-rows+1):
        print("\\___/   ", end="")
    print()
