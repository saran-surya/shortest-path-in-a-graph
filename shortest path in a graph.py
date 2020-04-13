def find(graph, var):
    for i in graph:
        if var in graph[i] and i == 1:
            return True
        else:
            if var in graph[i]:
                var = i
                return find(graph, var)
    return False

def weightchange(graph, weights):
    weight_ref = [0]*n
    #print(weight_ref)
    #print(graph)
    #print(weights)
    for i in weights.items():
        for j in graph[i[0][0]]:
            for k in weights:
                if i[0] == k and i[0][-1] == j:
                    if weight_ref[j-1] == 0:
                        weight_ref[j-1] = i[1][0]
                    else:
                        #print(i)
                        #print(j)
                        #print("weight",weight_ref[j-1])
                        #print("weight - i ", weight_ref[i[0][0]-1])
                        total = i[1][0] + weight_ref[i[0][0]-1]
                        if total < weight_ref[j-1]:
                            weight_ref[j-1] = total
    return(weight_ref)

n, m = map(int,input().split())
graph = {}
weights = {}
for i in range(m):
    u, v, w = map(int,input().split())
    if u not in graph:
        graph[u] = [v]
    else:
        tem = graph[u]
        tem.append(v)
        graph[u] = tem
    weights[(u,v)] = [w]
var = n
if find(graph, var):
    x = weightchange(graph, weights)
    print(x[-1])
else:
    print("-1")


'''
5 6
1 2 2
2 5 5
2 3 4
1 4 1
4 3 3
3 5 1
'''