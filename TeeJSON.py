from easygui import *
import json

Title='TeeJson'

Items={}

def new():
    global Items
    Items={}

    while True:
            m=multenterbox(msg='开始手动输入键值对。\n按下Cancel键表示键值对的结束。',title=Title,fields=['键(key)','值(value)'])

            if m:
                if not m[0]:
                    msgbox('不支持空键(key)！',Title)
                Items[m[0]]=m[1]
            else:
                if len(Items.keys())<2:
                        msgbox('键值对数量({})太少(至少2)！'.format(len(Items.keys())),Title)
                        continue
                return


def loadfile():
    global Items
    i=choicebox('选择导入方式。按下Cancel键表示导入结束。',Title,choices=['导入键','直接导入json键值对'])

    if i=='导入键':
        k=fileopenbox('导入键',Title)
        with open(k,'r') as k:
            r=k.readlines()
            for j in r:
                Items[j]=''

    elif i=='直接导入json键值对':
        msgbox('注意：使用utf-8编码格式。',Title)
        try:
            r=json.load(open(fileopenbox('导入键值对',Title),'r',encoding='utf-8'))
            for j in r['translation']:
                Items[j['key']]=j['value']

        except json.decoder.JSONDecodeError as e:
            msgbox('解码json时发生了错误:{}'.format(e),Title)

    '''
    elif i=='导入值':
        k=fileopenbox('导入值',Title) 
        with open(k,'r') as k:
            r=k.readlines()
            for j in r:
                Items[j]=''
    '''




def moveitem():
    global Items
    c=choicebox('下面展示了当前所有的键。选中一个键进行移动。',Title,Items.keys())
    if c:
        while True:
            nk=enterbox('请输入新的键。',Title)
            if nk:
                break
            msgbox('不支持空键！',Title)

        if ynbox('移动键值对：{}:{} 到新的键 {} ？'.format(c,Items[c],nk),Title):
            Items[nk]=Items[c]
            Items.pop(c)
        return


def edititem():
    global Items
    
    while True:
        keys=[]
        for i in Items.keys():
            keys.append(i)
        keys+=(r'##%% 删除键值对 ##%%',r'##%% 移动键值对 ##%%')

        c=choicebox('下面展示了当前所有的键。选中一个键进行编辑。',Title,keys)
        if c:
            if c==r'##%% 删除键值对 ##%%':
                delitem()
                continue
            elif c==r'##%% 移动键值对 ##%%':
                moveitem()
                continue

            l=multenterbox('编辑键。',Title,['键：','值：'],[c,Items[c]])
        else:
            return

        if l:
            if not l[0]:
                l[0]=c
            Items[l[0]]=l[1]
            continue
        Items.pop(c)

def output():
    global Items
    g={'translation':[]}
    for k,v in Items.items():
        g['translation'].append({'key':k,'value':v})
    g=json.dumps(g, sort_keys=True, indent=4, separators=(',', ': '))
    p=filesavebox('导出文件',Title)
    with open(p,'w') as p:
        p.write(g)
        msgbox('已导出。',Title)


def main():
    while True:
        ChoiceList=()
        BoxName=''

        if Items:
            BoxName='已经创建了一个新的键值对！\n退出和新建将不保存键值对。'
            ChoiceList=('新建键值对','编辑键值对','导出键值对','退出')
        else:
            BoxName='TeeJSON:快速链接翻译文本！'
            ChoiceList=('新建键值对','导入键值对','退出')
        
        c=choicebox(BoxName,Title,choices=ChoiceList)

        if c=='新建键值对':
            new()
        elif c=='导入键值对':
            loadfile()
        elif c=='编辑键值对':
            edititem()
        elif c=='导出键值对':
            output()
        elif c=='退出' or (not c):
            return


if __name__=='__main__':
    main()