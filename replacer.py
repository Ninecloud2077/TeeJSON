with open('cn.txt','r',encoding='utf-8') as r:
    Label=[i.strip('\n')for i in r.readlines()]

with open('TeeJSON.py','r',encoding='utf-8') as fo:
    Read=fo.read()
    for i in range(len(Label)):
        Read=Read.replace("'{}'".format(Label[i]),'lang[{}]'.format(i))
    Read=Read.replace('rlang','lang')
    
with open('out.py','w',encoding='utf-8') as w:
    w.write(Read)