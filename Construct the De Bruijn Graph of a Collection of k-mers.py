f = open("rosalind_ba3e.txt", "r")
text = []
for line in f:
    text.append(line.strip())
graph = {}
nodes = []
for t in text:
    if t[:-1] not in graph:
        temp = []
        nodes.append(t[:-1])
        temp.append(t[1:])
        graph[t[:-1]] = list(temp)
    else:
        graph[t[:-1]].append(t[1:])
f.close()

f = open("adjacencyListGraph.txt", "w")
for n in nodes:
    line = n + " -> "
    count = 1
    for s in sorted(graph[n]):
        if count == 1:
            line += s
        else:
            line += ","
            line += s
        count += 1
    f.write(line + "\n")
f.close()