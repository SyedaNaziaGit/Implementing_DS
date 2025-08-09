class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for key,val in self.edges:
            if key in self.graph_dict:
                self.graph_dict[key].append(val)
            else:
                self.graph_dict[key]=[val]
        print("Graph Dictionary :",self.graph_dict)
    def get_paths(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                newpaths= self.get_paths(node,end,path)
                for eachpath in newpaths:
                    paths.append(eachpath)
        return paths
    def get_min_path(self,start,end,path = []):
        path = path +[start]
        if start not in self.graph_dict:
            return None
        if start == end:
            return [path]
        shortest_path = None
        for node in  self.graph_dict[start]:
            if node not in path:
                minpath = self.get_min_path(node,end,path)
                if minpath:
                    if shortest_path is None or len(minpath)<len(shortest_path):
                        shortest_path = minpath
        return shortest_path
                    
        
        
if __name__ == "__main__":
    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]
    route_graph = Graph(routes)
    start = "Mumbai"
    end = "Bangaluru"
    print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    print("===============================================")
    print(f"Shortest path between {start} and {end}: ", route_graph.get_min_path(start=start,end=end))
    print("*******************************************************************************")
    start = "Mumbai"
    end = "Hyderabad"
    print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    print("===============================================")
    print(f"Shortest path between {start} and {end}: ", route_graph.get_min_path(start=start,end=end))
    
'''
Output:

Graph Dictionary : {'Mumbai': ['Pune', 'Surat'], 'Surat': ['Bangaluru'], 'Pune': ['Hyderabad', 'Mysuru'], 'Hyderabad': ['Bangaluru', 'Chennai'], 'Mysuru': ['Bangaluru'], 'Chennai': ['Bangaluru']}
All paths between: Mumbai and Bangaluru:  [['Mumbai', 'Pune', 'Hyderabad', 'Bangaluru'], ['Mumbai', 'Pune', 'Hyderabad', 'Chennai', 'Bangaluru'], ['Mumbai', 'Pune', 'Mysuru', 'Bangaluru'], ['Mumbai', 'Surat', 'Bangaluru']]
===============================================
Shortest path between Mumbai and Bangaluru:  None
*******************************************************************************
All paths between: Mumbai and Hyderabad:  [['Mumbai', 'Pune', 'Hyderabad']]
===============================================
Shortest path between Mumbai and Hyderabad:  [['Mumbai', 'Pune', 'Hyderabad']]
'''