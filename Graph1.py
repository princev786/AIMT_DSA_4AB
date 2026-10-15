graph = []

def createGraph(v):
    for i in range(0,v+1):
        graph.append([])

def addEdge(src,dest):
    graph[src].append(dest)
    graph[dest].append(src)

def dltEdge(src,dest):
    graph[src].remove(dest)
    graph[dest].remove(src)

def bfs(src,v):
    visited =[]
    for i in range(v+1):
        visited.append(False)
    que = []
    visited[src] = True
    que.append(src)

    while len(que)!=0:
        curr = que[0]
        del que[0]
        print(curr ,end =" ")
        for neighbour in graph[curr]:
            if visited[neighbour]!=True:
                visited[neighbour] = True
                que.append(neighbour)

def dfs(src,v, visited):
    visited[src]=True
    print(src,end=" ")
    for neighbour in graph[src]:
        if visited[neighbour]!=True:
            dfs(neighbour,v,visited)

def ispathexist(src,dest):
    if src==dest:
        return True
    visited = []
    for i in range(v+1):
        visited.append(False)
    que=[]
    visited[src]=True
    que.append(src)
    while len(que)!=0:
        curr=que[0]
        print(curr ,end=" ")
        for neighbour in graph[curr]:
            if visited [neighbour]!=True:
                visited [neighbour] =True
                que.append(neighbour)


def countcomp(v):
    visited = []
    for i in range(v+1):
        visited.append(False)
    c=0
    for i in range(1,v+1):
        if visited[i] != True:
            dfs(i,v,visited)
            c+=1
    return c 

if __name__ == "__main__":
    v = 6
    createGraph(v)        
    addEdge(1,2)    
    addEdge(4,6)    
    addEdge(4,5)    
    addEdge(5,6)  
    print(countcomp(v))  
    # bfs(1,v)
    print()
    # visited=[]
    # for i in range(v+1):
    #     visited.append(False)
    # dfs(1,v,visited)

