FileList=['Content.txt','Structure.txt','Article.txt']
Con=[]
St=[]
Art=[]
count=0
for Path in FileList:
    with open(Path) as Fl:
        if Path == 'Content.txt' :
            Con = Fl.readlines()
        elif Path== 'Structure.txt':
            St=Fl.readlines()
        elif Path == 'Article.txt':
            Art = Fl.readlines()
def rep(List):
    for x in range(len(List)):
        List[x-1]=List[x-1].replace('\n','')
    return List
def Cutstr(Str):
    collect=''
    result=[]
    ModUSE= False
    for x in Str:
        if x==' ' and ModUSE==False and collect!='':
            result.append(collect)
            collect=''
        elif x==' ' and ModUSE==False and collect=='':
            collect=''
        elif x=="'" and ModUSE==False:
            ModUSE=True
        elif x=="'" and ModUSE==True:
            result.append(collect)
            ModUSE=False
            collect=''
        elif x==' ' and ModUSE==True:
            collect=collect+x
        else:
            collect=collect+x
    if collect!='' :
        result.append(collect)
    return result
Con = rep(Con)
St = rep(St)
Art= rep(Art)
Con_2=[]
St_2=[]
for word in Con:
    Con_2.append(Cutstr(word))
for lis in Con_2:
    lis[1] = int(lis[1])
    lis[2] = int(lis[2])
Con=[]
for k in Con_2:
    Con.append(k[0])
for word in St:
    St_2.append(Cutstr(word))
def getArticle(Name):
    result = []
    for Na in Con_2:
        if Name == Na [0] :
            if len(Na) == 3:
                for co in range(Na[1],Na[2]+1):
                    result.append(Art [co])
            elif len(Na) == 2:
                result.append(Art [Na[1]] )
    for Line in result :
        print(Line)
def getInput(List):
    print('You can choose in',len(List),'options :')
    for i in range(len(List)):
        print(i+1 , List [i-1])
    result = -1
    while result<=0 or result >len(List):
        try:
            result = int( input(''))
        except:
                print('Invalid input')
    return result
def GetCaptionList(min ,max ,List):
    result = []
    for i in range(min,max):
        result.append(List[i][3])
    return result
def showtheword(Name):
    getArticle(Name)
    count = 0
    for Line in St_2:
        if Line[0] == Name :
            if Line [1] == 'then' :
                print('______')
                input('Continue')
                showtheword( Line [2] )
            elif Line [1] == 'Option' :
                List = GetCaptionList(count+1,(count)+int(Line[2])+1,St_2)
                result = getInput(List)
                To = St_2[count + result ][1]
                print('______')
                showtheword(To)
            elif Line [1] == 'end':
                print('end')
                input()
        count =count+1
text = St_2[0]
print('___Loading have been finished___')
if text[0] == 'Begin' and len(text)==4 and text[2]=='with':
    print(text[3])
    showtheword(text[1])
elif text[0] == 'Begin' and len(text)==2:
    showtheword(text[1])