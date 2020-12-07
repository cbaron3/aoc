from collections import defaultdict

# Copy-pasted from geeks for geeks
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
   
    def printContents(self):
        print(self.graph)

    def getVertices(self):
        return self.graph.keys()

    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
       
     # Use BFS to check path between s and d 
    def isReachable(self, s, d): 
        # Mark all the vertices as not visited 
        visited = defaultdict(bool)
   
        # Create a queue for BFS 
        queue=[] 
   
        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True
   
        while queue: 
  
            #Dequeue a vertex from queue  
            n = queue.pop(0) 
              
            # If this adjacent node is the destination node, 
            # then return true 
            if n == d: 
                return True
  
            #  Else, continue to do BFS 
            for i in self.graph[n]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
        # If BFS is complete without visited d 
        return False

# 0 vertices
bag_graph = Graph(0)

def extract_vertices(rule):
    # Extract base color
    base = rule[:rule.index('bags')-1]

    # How many could contain at least 1, dont need to check count
    # Extract 
    contents = rule[rule.index('contain')+len('contain')+1:-1]

    if contents != 'no other bags':
        base_contents = []
        for content in contents.split(','):
            d = content.strip().split(' ')[1:-1]
            bag_graph.addEdge(base, ' '.join(d))

with open("Input.txt") as file:
    for line in file:
        extract_vertices(line)

    counter = 0
    keys = list(bag_graph.getVertices())
    for key in keys:
        if key != 'shiny gold':
            # If a key can reach the shiny gold vertex in the graph, increase the counter by 1
            if bag_graph.isReachable(key, 'shiny gold'):
                counter += 1

    print(counter)
