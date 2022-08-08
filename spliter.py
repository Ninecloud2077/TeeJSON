s=e=0
a=[]
with open('TeeJSON.py','r',encoding='utf-8') as fo:
    for i in fo.readlines():
        for j in range(len(i)):      
            if i[j]=="'":
                if s:            
                    e=j
                    a.append(i[s+1:e])
                    s=e=0
                else:
                    s=j
na=[]
for i in a:
    if i+'\n' not in na:
        na.append(i+'\n')                   
with open('trans.txt','w',encoding='utf-8') as w:
    w.writelines(na)