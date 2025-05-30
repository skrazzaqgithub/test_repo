runs = []
FH = open("scores.txt")
for line in FH:
    #print(line)
    runs.append(int(line.strip()))

print(runs)
    
new_runs = sorted(runs)
print(new_runs)
