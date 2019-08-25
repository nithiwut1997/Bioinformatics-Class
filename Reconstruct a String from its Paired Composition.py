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

#-----------------------------------------------------------

def dfs(graph, state, stack):
    for root in graph.keys():
            if state[root] == 0:
                dfs_recur(root, graph, state, stack)
                
#----------------------------------------------------------

f = open("rosalind_ba3j.txt", "r")
k, d = [int(e) for e in f.readline().split()]
graph = {}
state = {}
for line in f:
    text = line.strip().split("|")
    left = (text[0][:-1], text[1][:-1])
    right = (text[0][1:], text[1][1:])
    state[left] = 0
    if left not in graph:
        temp = []
        temp.append(right)
        graph[left] = list(temp)
    else:
        graph[left].append(right)
f.close()
stack = []
dfs(graph, state, stack)

#-----------------------------------------------------------

euler_path = []
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
start = euler_path[0][0]
end = euler_path[0][1]
euler_path.pop(0)
for pair in euler_path:
    start = pair[0][0] + start
    end = pair[1][0] + end
pairedReads = start[:k + d] + end
f = open("pairedReads.txt", "w")
f.write(pairedReads + "\n")
f.close()