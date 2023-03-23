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
stack=[]

def dfs(stack,graph,node):

    if node not in stack:
        print(node,end=" ")
        if(node=='G'):
            print("\n Goal Found")
            return
        
        for neighbour in graph[node]:
            dfs(stack,graph,neighbour)
            
        
dfs(visit,graph,'A')