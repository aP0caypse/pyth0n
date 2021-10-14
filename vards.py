va="skonto"
fu=open("es.txt","w",encoding="utf-8")
for i in range (len(va)):
    print(" "*i,va,file=fu)
fu.close
