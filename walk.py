class Walk:
    """Class for walks (in directed graphs)."""
    
    def __init__(self, vertexSeq):
        self.vertexSeq = vertexSeq
        
    def __str__(self):
        """Returns a nice string representation"""
        wstring = str(self.vertexSeq[0])
        for v in self.vertexSeq[1:]:
            wstring = wstring + "->" + str(v)
        return wstring    
    
    def length(self):
        """Length is the number of (implicit) edges involved"""
        return len(self.vertexSeq)-1
    
    def extend(self,vertex):
        """Creates new walk from given walk with given vertex added"""
        return Walk(self.vertexSeq + [vertex])
    
    def lastVertex(self):
        return self.vertexSeq[-1]
    
    def path(self):
        # no revisiting
        for i in range(len(self.vertexSeq)-1,-1,-1):
            # last instance of each vertex is also the first
            if self.vertexSeq.index(self.vertexSeq[i]) != i:
                return False
        return True
    
    def cycle(self):
        if self.length() < 1:
            return False
        # begins and ends at same vertex
        if self.vertexSeq[len(self.vertexSeq)-1] != self.vertexSeq[0]:
            return False
        # no other revisiting
        for i in range(len(self.vertexSeq)-2,-1,-1):
            if self.vertexSeq.index(self.vertexSeq[i]) != i:
                return False
        return True