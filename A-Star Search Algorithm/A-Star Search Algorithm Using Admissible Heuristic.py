class Graph:
    def __init__(self,adj_list):
        self.adjacency_list=adj_list
    
    def get_neighbors(self,v):
        return self.adjacency_list[v]
    
    def h(self,n):
        Hue={ "Arad": 316,
              "Bucharest": 0,
              "Craiova": 110,
              "Dobreta": 192,
              "Eforie": 111,
              "Fagaras": 126,
              "Giurgiu": 27,
              "Hirsowa": 101,
              "Lasi": 174,
              "Lugoj": 194,
              "Mehadia": 1911,
              "Neamt": 184,
              "Oradea": 330,
              "Pitesti": 50,
              "Rimnicu Vilcea": 143,
              "Sibiu": 203,
              "Timisoara": 289,
              "Urziceni": 30,
              "Vaslui": 149,
              "Zerind": 324
             }
        return Hue[n]
    
    def A_star_algo(self, start_node, end_node):
        open_list=set([start_node])
        closed_list=set()
        
        g={}
        
        g[start_node]=0
        
        parents={}
        parents[start_node]=start_node
        
        while len(open_list)>0:
            n=None
            
            for v in open_list:
                if n==None or g[v]+self.h(v)<g[n]+self.h(n):
                    n=v
                    
            if n==end_node:
                reconst_path=[]
                
                while parents[n] !=n:
                    reconst_path.append(n)
                    n=parents[n]
                    
                reconst_path.append(start_node)
                reconst_path.reverse()
                print("path found {} ".format(reconst_path))
                return reconst_path
            
            for (m,weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m]=n
                    g[m]=g[n]+weight
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        parents[m]=n
                        
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
                            
            open_list.remove(n)
            closed_list.add(n)
            #print("parent list", parents) 
                
   
        print("path does not exists")
        return None
    
adj_list={"Arad":[("Zerind",75),("Sibiu",140),("Timisoara",118)],
          "Zerind":[("Oradea",71)],
          "Timisoara":[("Lugoj",111)],
          "Sibiu":[("Fagaras",99),("Rimnicu Vilcea",80)],
          "Lugoj":[("Mehadia",70)],
          "Fagaras":[("Bucharest",211)],
          "Rimnicu Vilcea":[("Pitesti",97),("Craiova",146)],
          "Mehadia":[("Dobreta",75)],
          "Bucharest":[("Urziceni",85),("Giurglu",90)],
          "Pitesti":[("Craiova",138),("Bucharest",101)],
          "Craiova":[("Rimnicu Vilcea",146)]
         }
gr=Graph(adj_list)
gr.A_star_algo("Arad", "Bucharest")