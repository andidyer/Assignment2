from fsa import FSA as FSA
import ourexamples

def sortprint(strs):
    strs.sort()
    print(strs)

fsaApa = FSA(['s0','s1','s2','s3','s4','s5','s6','s7','s8'], \
  ['a','n','o','p','r','s'], 's0', ['s3','s4','s5','s7'], \
  [('s0','a','s1'), ('s1','p','s2'), ('s2','a','s3'), ('s2','o','s6'), \
   ('s3','n','s5'), ('s3','s','s4'), ('s5','s','s4'),('s6','r','s7'), \
   ('s7','n','s8'),('s7','s','s4'),('s8','a','s5')])

sortprint(fsaApa.generate(100))

fsaEaEb = FSA(['s0','s1','s2','s3'],['a','b'],'s0',['s0'], \
              [('s0','a','s1'),('s0','b','s2'),('s1','a','s0'),('s1','b','s3'), \
               ('s2','a','s3'),('s2','b','s0'),('s3','a','s2'),('s3','b','s1')])

print(fsaEaEb.accepts('aabbaa'))
print(fsaEaEb.accepts('aababaa'))
print(fsaEaEb.accepts('aabbbaa'))

sortprint(fsaEaEb.generate(5))
sortprint(fsaEaEb.generate(8))

sortprint(ourexamples.fsaAA.generate(100))
sortprint(ourexamples.fsaRegEx.generate(10))



