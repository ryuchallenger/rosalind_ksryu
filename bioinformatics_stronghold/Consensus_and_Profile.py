with open("test.txt", "r") as f:
    str = f.read()

parts = str.split("\n")

parts = [i.replace("\\", "") for i in parts]

id = []
DNA = []
for line in parts:
    if line.startswith(">"):
        id.append(line)
    elif len(line) < 2:
        next
    else: 
        DNA.append(line)


d = dict(zip(id,DNA))

print(d)