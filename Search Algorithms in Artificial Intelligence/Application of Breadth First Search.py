graph = {'A':['B','D'],
         'B':['C','E'],
         'C':[],
         'D':['E','G','H'],
         'E':['C','F'],
         'F':[],
         'G':['H'],
         'H':[]
        }

visit=[]
queue=[]

def bfs(visit,graph,node):
    visit.append(node)
    queue.append(node)
    
    while queue:    # loop runs unntill there is an element in the queue
        element=queue.pop(0)
        print(element,end=" ")
        if(element=='G'):
            print("\n Goal Found")
            return
        
        for neighbour in graph[element]:
            if neighbour not in visit:
                visit.append(neighbour)
                queue.append(neighbour)
                

bfs(visit,graph,'A')  