#def rewrite_dict(d:dict[str, int]) -> dict[str,int]:
 #   somma= sum(list(d.values()))
  #  out={}
   # for key in d:
    #    out[key]=d[key]/somma
    #return out
#d = {"ciao": 2, "hello":3}
#output= rewrite_dict(d)
#print(output)
##
#x=5
#y=3
#def subtrack(x, y):
   # sub = x - y
  #  print(sub)
 #   return sub
#subtrack(x,y)
def diff_cum(l : list[float]) -> float:
    diff: float = l[0]
    for elem in l:
        
