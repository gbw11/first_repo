arr = ["MC", "BTS", "BTS", "MC", "BTS"]

d = dict()

for a in arr :
    d[a] = 0

for a in arr :
    d[a] +=1



for key, value in d.items():
    print(f"{key} {value}")