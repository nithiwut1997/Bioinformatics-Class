def dfs_recur(root, graph, state, stack):
    state[root] = 1
    if root in graph:
        for v in graph[root]:
            if v in graph:
                if state[v] == 0:
                    dfs_recur(v, graph, state, stack)
            else:
                stack.append(v)
    stack.append(root)
    
#------------------------------------------------------------

def dfs(graph, state, stack):
    for root in graph.keys():
            if state[root] == 0:
                dfs_recur(root, graph, state, stack)

#------------------------------------------------------------

f = open("rosalind_ba3g.txt")
graph = {}
state = {}
for line in f:
    temp = line.strip().split(" -> ")
    graph[temp[0]] = temp[1].split(",")
    state[temp[0]] = 0
f.close()

#-------------------------------------------------------------

stack = []
dfs(graph, state, stack)
euler_path = []
path = ""
stack = stack[-1:]
while len(stack) > 0:
    top = stack[-1]
    if top in graph:
        if len(graph[top]) > 0:
            v = graph[top][0]
            graph[top].pop(0)
            stack.append(v)
        else:
            euler_path.append(top)
            stack.pop()
    else:
        euler_path.append(top)
        stack.pop()
for node in euler_path:
    path  = "->" + node + path
path = path[2:]
f = open("euler_path.txt", "w")
f.write(path + "\n")
f.close()