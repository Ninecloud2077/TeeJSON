from easygui import *
import json

Title='TeeJson'

Items={}


def initlang(language='cn.txt'):
    global lang
    with open('lang/'+language,'r',encoding='utf-8') as l:
        lang=[i.replace('\\n','\n')for i in l.readlines()]
initlang()

def new():
    global Items
    Items={}

    while True:
            m=multenterbox(msg=lang[0],title=Title,fields=[lang[1],lang[2]])

            if m:
                if not m[0]:
                    msgbox(lang[3],Title)
                Items[m[0]]=m[1]
            else:
                if len(Items.keys())<2:
                        msgbox(lang[4].format(len(Items.keys())),Title)
                        continue
                return


def loadfile():
    global Items
    i=choicebox(lang[5],Title,choices=[lang[6],lang[7]])

    if i==lang[6]:
        msgbox(lang[8],Title)
        k=fileopenbox(lang[6],Title)
        if k:
            with open(k,'r',encoding='utf-8') as k:
                r=k.readlines()
                for j in r:
                    Items[j]=''

    elif i==lang[7]:
        msgbox(lang[8],Title)
        try:
            k=fileopenbox(lang[9],Title)
            if k:
                r=json.load(open(k,'r',encoding='utf-8'))
                for j in r['translation']:
                    Items[j['key']]=j['value']

        except json.decoder.JSONDecodeError as e:
            msgbox(lang[10].format(e),Title)

    '''
    elif i=='导入值':
        k=fileopenbox('导入值',Title) 
        with open(k,'r') as k:
            r=k.readlines()
            for j in r:
                Items[j]=''
    '''


def delitem():
    global Items
    c=choicebox(lang[11],Title,Items.keys())
    if c and ynbox(lang[12].format(c,Items[c]),Title):
        if len(Items.keys())<=3:
            msgbox(lang[13],Title)
            return
        Items.pop(c)
        msgbox(lang[14],Title)
    return


def moveitem():
    global Items
    c=choicebox(lang[15],Title,Items.keys())
    if c:
        while True:
            nk=enterbox(lang[16],Title)
            if nk:
                break
            msgbox(lang[17],Title)

        if ynbox(lang[18].format(c,Items[c],nk),Title):
            Items[nk]=Items[c]
            Items.pop(c)
            msgbox(lang[19],Title)
        return


def edititem():
    global Items
    
    while True:
        keys=[]
        for i in Items.keys():
            keys.append(i)
        keys+=(lang[20],lang[21])

        c=choicebox(lang[22],Title,keys)
        if c:
            if c==lang[20]:
                delitem()
                continue
            elif c==lang[21]:
                moveitem()
                continue

            l=multenterbox(lang[23],Title,[lang[24],lang[25]],[c,Items[c]])
        else:
            return

        if l:
            if not l[0]:
                l[0]=c
            Items[l[0]]=l[1]
            continue
        elif len(Items.keys())>2:
            Items.pop(c)


def editempty():
    global Items
    msgbox(lang[26])
    for k,v in Items.items():
        if not v:
            while True:
                nv=enterbox(lang[27].format(k),Title)
                if nv:
                    Items[k]=nv
                    break
                return


def output():
    global Items
    g={'translation':[]}
    for k,v in Items.items():
        g['translation'].append({'key':k,'value':v})
    g=json.dumps(g, sort_keys=True, indent=4, separators=(',', ': '))
    p=filesavebox(lang[28],Title)
    with open(p,'w',encoding='utf-8') as p:
        p.write(g)
        msgbox(lang[29],Title)

def langswitch():
    c=choicebox(lang[38],Title,lang[39:41])
    if c:
        if c==lang[39]:
            initlang('cn.txt')
        elif c==lang[40]:
            initlang('en.txt')



def main():
    while True:
        ChoiceList=()
        BoxName=''

        if Items:
            BoxName=lang[30]
            ChoiceList=(lang[31],lang[32],lang[33],lang[34],lang[35],lang[37])
        else:
            BoxName=lang[36]
            ChoiceList=(lang[31],lang[9],lang[35],lang[37])
        
        c=choicebox(BoxName,Title,choices=ChoiceList)

        if c==lang[31]:
            new()
        elif c==lang[9]:
            loadfile()
        elif c==lang[32]:
            edititem()
        elif c==lang[33]:
            editempty()
        elif c==lang[34]:
            output()
        elif c==lang[37]:
            langswitch()
        elif c==lang[35] or (not c):
            return


if __name__=='__main__':
    main()