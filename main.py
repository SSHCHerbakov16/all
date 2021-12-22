lists=[1,1,2,3,5],[8,13,21,34],[55,89,144]
def merge(*lists):
  all=sum(lists,[])
  print(sorted(all))
merge(*lists)
