try:
    file = open("sample.txt", "r")
    for line in file:
        print(line.strip())
    file.close()
except FileNotFoundError as fe:
    print("File not found.", fe)
