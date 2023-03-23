class Graph:
    def __init__(self,adj_list):
        self.adjacency_list=adj_list
    
    def get_neighbors(self,v):
        return self.adjacency_list[v]
    
    def h(self,n):
        Hue={ 'S': 4,
              'A': 2,
              'B': 6,
              'C': 3,
              'D': 2,
              'G': 0, 
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
                
        print("path does not exsists")
        return None
    
adj_list={'S':[('A',1),('G',12)],
          'A':[('B',3),('C',1)],
          'B':[('D',3)],
          'C':[('D',1),('G',2)],
          'D':[('G',3)],
          'G':[]         
         }

gr=Graph(adj_list)
gr.A_star_algo('S', 'G')