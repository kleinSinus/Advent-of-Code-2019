class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def __str__(self):
        return f"The graph has {len(self.vertices)} vertices and {len(self.edges)} edges."
    
    def hasVertex(self, vert):
        for vertex in self.vertices:
            if vertex == vert:
                return True
        return False
    
    def hasEdge(self, edg):
        for edge in self.edges:
            if edg == edge:
                return True
        return False
    
    def addVertex(self, vert):
        if (not self.hasVertex(vert)):
            self.vertices.append(vert)
    
    def addEdge(self, vert_in, vert_out):
        nuEdge = [vert_in, vert_out]
        if (not self.hasEdge(nuEdge)):
            self.edges.append(nuEdge)

    def rmVertex(self, vert):
        out = []
        for vertex in self.vertices:
            if not vert == vertex:
                out.append(vert)
        self.vertices = out
    
    def getInDegrees(self):
        out = [0] * (len(self.vertices))
        for index in range(len(self.vertices)):
            for edge in self.edges:
                if edge[1] == self.vertices[index]:
                    out[index] += 1
        return out
    
    def getOutDegrees(self):
        out = [0] * (len(self.vertices))
        for index in range(len(self.vertices)):
            for edge in self.edges:
                if edge[0] == self.vertices[index]:
                    out[index] += 1
        return out
    
    def getIndex(self,vertex):
        if self.hasVertex(vertex):
            for i in range(len(self.vertices)):
                if vertex == self.vertices[i]:
                    return i
        else:
            return len(self.vertices)

    def swap(self, a, b):
        if (self.hasVertex(a) and self.hasVertex(b)):
            ia = self.getIndex(a)
            ib = self.getIndex(b)
            self.vertices[ia] = b
            self.vertices[ib] = a

    def sortByIndegree(self): # ascendingly bubblesorts the vertices by their respective indegrees
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)-(i+1)):
                if(self.getInDegrees()[j] > self.getInDegrees()[j+1]):
                    self.swap(self.vertices[j], self.vertices[j+1])

    def dominator(self, v1, v2): # returns the dominating between two vertices v1 and v2
        if (not (self.hasVertex(v1) or self.hasVertex(v2))):
            print("One or both vertices not found")
            return "err"
        for edge in self.edges:
            if(edge[0] == v1 and edge[1] == v2):
                return v1
            if(edge[0] == v2 and edge[1] == v1):
                return v2
        if (self.hasVertex(v1)):
            return v1
        elif (self.hasVertex(v2)):
            return v2
        else:
            return 'err'

    def sortVertexList(self, list): # sorts a list of vertices according to their hierarchy in the graph
        result = []
        for i in range(len(list)): # insertionsort
            #print('Inserting ' + list[i] + ': ')
            if (len(result) == 0):
                result.append(list[i])
            else:
                done = False
                for j in range(len(result)):
                    front = result[:j]
                    back = result[j:]
                    if (self.dominator(list[i],result[j]) == list[i]): # new vertex dominates current result vertex
                        #print(list[i] + ' dominates over ' + result[j])
                        result = front + [list[i]] + back
                        done = True
                        break
                    elif (self.dominator(list[i],result[j]) == result[j]):
                        pass
                        #print(list[i] + ' subordinates to ' + result[j])
                if(not done):
                    result.append(list[i])
            # print(result)
        return result