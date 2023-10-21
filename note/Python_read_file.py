# method 1
for line in open("/Users/kityua/PycharmProjects-gaoji/ETL-Python/note/a.txt", "r", encoding="UTF-8"):
    line = line.replace("\n", "")
    print(line)

# method 2
with open("/Users/kityua/PycharmProjects-gaoji/ETL-Python/note/a.txt", "r", encoding="UTF-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)