class StringAlignmentTable:
    
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2
        self.table = []
        # builds the table
        for _ in range(len(self.s1)+1):
            column = []
            for _ in range(len(self.s2)+1):
                column.append(None) # i.e. empty cell
            self.table.append(column)
                
    def __str__(self):  
        ostr = "        "
        for i in range(0,len(self.s1)+1):
            if i > 0:
                # top row of letters
                ostr = ostr + "   " + self.s1[i-1]
        ostr = ostr + '\n'
        for j in range(0,len(self.s2)+1):
            if j > 0:
                # first column of letters
                ostr = ostr + "   " + self.s2[j-1]
            else:
                ostr = ostr + "    "
            for i in range(0,len(self.s1)+1):
                # ordinary cells, width 4, with
                # distance and operation letter
                ostr = ostr + ("    " +  \
                        str(self.table[i][j][0]) + \
                        self.table[i][j][1])[-4:]
            ostr = ostr + '\n'
        return ostr 