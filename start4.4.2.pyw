import pygame,pgzrun,random,time,os,get
TITLE='祈愿-version 4.4.2'#标题栏
ICON='icon.png'#图标图片
WIDTH = 1013#宽
HEIGHT = 566#高
bjnum=52#班级人数
os.environ ['SDL_VIDEO_CENTERED'] ='1'#窗口居中
history=[]
historytime=[]
getlist1=['0','0','0','0','0','0','0','0','0','0']
getlist2=['p','p','p','p','p','p','p','p','p','p']
goldlist=['51','34','49','48','9','17']
types=['1','1']
historytype='1'
bgct=1
pz=['1','1','1','1','1','1','1','1','1','1']
#name=['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ']
name=['曹雨凡','陈凯瑜','陈琳','陈默希','陈欣怡','陈逸航','陈毅霖','陈宇阳','陈正熙','陈子尧','陈梓裕','程浩轩','傅晨轩','关凯悦','金诗妍','李楚熙','李景峰','李智源','李梓轩','梁艺栩','林铭轩','林子壕','刘思鹏','潘泽心','邱丹娜','谭锦悦','唐宇艳','王锦轩','王子霂','王子煜','吴家昊','肖朝一','谢宗栩','余思锦','岳梓康','张楚铷','张钰涵','张子健','赵辅仁','赵嘉俊','郑惠如','郑振从','钟宝怡','陈罗阳','陈子涵','郭梓晴','何咏锶','李梓彤','苏芷樱','邬月霞','张婉碧','麦嘉俊']
#name对应的是各个学号相应的同学，可改，共52人
goldlists=[['52','4'],['52','4'],['52','4'],['52','4']]#每个卡池的金，可改,可无限添加，但是范围要在1~班级人数 之间
goldlist=goldlists[int(types[0])-1]
ui='main'
card=1
page=1
bk=True
skip=False
whitemb=Actor('whitemb.png',[538, 173])
bg=Actor('bg1.png')
for i in range(10):
    pz[i]=Actor('pzn.png',[140,283])
YiLianButtom=Actor('1.png',[710,530])
ShiLianButtom=Actor('10.png',[890,530])
publicnotice=Actor('shopbt.png',[81, 545])
skipbt=Actor('skipbtf.png',[472, 531])
os.startfile(os.getcwd()+'/公告/start.pyw')
def read():
    global ys,jczy,xyzy
    file1 = open(os.getcwd()+'/assets/user/lzx/file1.txt','r')
    list1=list(file1.read())
    file1.close()
    ys=''
    jczy=''
    xyzy=''
    i=0
    while True:
        if list1[i]=="#":
            i+=1
            break
        else:
            ys+=list1[i]
            i+=1
    while True:
        if list1[i]=="#":
            i+=1
            break
        else:
            jczy+=list1[i]
            i+=1
    while True:
        if list1[i]=="#":
            i+=1
            break
        else:
            xyzy+=list1[i]
            i+=1
    ys=int(ys)
    jczy=int(jczy)
    xyzy=int(xyzy)
def history_read():
    historytime_read()
    global history,historytype
    history=[]
    ys=''
    f=0
    b = open(os.getcwd()+'/assets/user/lzx/history'+historytype+'.txt','r')
    list1=list(b.read())
    b.close()
    b = open(os.getcwd()+'/assets/user/lzx/history'+historytype+'num.txt','r')
    a=b.read()
    b.close()
    for i in range(int(a)*3):
        if list1[i]=="#":
            i+=1
            history.append(int(ys))
            f+=1
            ys=''
        else:
            ys+=list1[i]
            i+=1
    if int(a)%5!=0:
        for i in range(5-int(a)%5):
            history.append(0)
    elif int(a)==0:
        for i in range(5):
            history.append(0)
def historytime_read():
    global historytime,historytype
    historytime=[]
    ys=''
    f=0
    b = open(os.getcwd()+'/assets/user/lzx/history'+historytype+'time.txt','r')
    list1=list(b.read())
    b.close()
    b = open(os.getcwd()+'/assets/user/lzx/history'+historytype+'num.txt','r')
    a=b.read()
    b.close()
    for i in range(int(a)*20):
        if list1[i]=="#":
            i+=1
            historytime.append(ys)
            f+=1
            ys=''
        else:
            ys+=list1[i]
            i+=1
    if int(a)%5!=0:
        for i in range(5-int(a)%5):
            history.append('0000-00-00 00:00:00')
    elif int(a)==0:
        for i in range(5):
            history.append('0000-00-00 00:00:00')
def write():
    global ys,jczy,xyzy
    file1 = open(os.getcwd()+'/assets/user/lzx/file1.txt','w')
    file1.write(str(ys)+"#"+str(jczy)+"#"+str(xyzy)+"#")
    file1.close()
def bgplay():
    global getlist1,getlist2,types,bgct
    if bgct==2:
        m1Play()
    if bgct==30:
        m3Play()
    if types[1]=='1':
        if 'g' in getlist2:
            bg.image='1gold ('+str(bgct)+').png'
        else:
            bg.image='1purple ('+str(bgct)+').png'
    else:
        if 'g' in getlist2:
            bg.image='10gold ('+str(bgct)+').png'
        else:
            bg.image='10purple ('+str(bgct)+').png'
def pzct():
    posx=140
    for i in range(10):
        if pz[i].x>=posx+369:
            pz[i].x-=100
        elif pz[i].x>=posx+256:
            pz[i].x-=80
        elif pz[i].x>=posx+162:
            pz[i].x-=60
        elif pz[i].x>=posx+94:
            pz[i].x-=40
        elif pz[i].x>=posx+47:
            pz[i].x-=20
        elif pz[i].x>=posx+26:
            pz[i].x-=10
        elif pz[i].x>=posx+15:
            pz[i].x-=5
        posx+=80
def get1():
    global getlist1,getlist2,types,jczy,xyzy,historytype
    getlist1=['0','0','0','0','0','0','0','0','0','0']
    getlist2=['p','p','p','p','p','p','p','p','p','p']
    getlist1[0]=get.an(historytype)
    if getlist1[0] in goldlist:
        getlist2[0]='g'
    read()
    if types[1]=='4':
        xyzy-=1
    else:
        jczy-=1
    write()
def get10():
    global getlist1,getlist2,types,jczy,xyzy,historytype
    getlist1=['0','0','0','0','0','0','0','0','0','0']
    getlist2=['p','p','p','p','p','p','p','p','p','p']
    for i in range(10):
        getlist1[i]=get.an(historytype)
        if getlist1[i] in goldlist:
            getlist2[i]='g'
        read()
        if types[1]=='4':
            xyzy-=1
        else:
            jczy-=1
        write()
def MainMusicPlay():#播放背景音乐
    fileZ = os.getcwd()+'/sounds/main.wav'
    pygame.mixer.init()
    track = pygame.mixer.music.load(fileZ)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play() # 获取每一首歌曲的时长，使程序存活的时长等于歌曲时长  
    clock.schedule_unique(MainMusicPlay,86)
def tapPlay():#播放m1
    fileTap = os.getcwd()
    tap = pygame.mixer.Sound(fileTap+'/sounds/tap.wav')
    tap.play(loops=0,maxtime=0,fade_ms=0)
def turnPlay():#播放m1
    fileTurn = os.getcwd()
    turn = pygame.mixer.Sound(fileTurn+'/sounds/turn.wav')
    turn.play(loops=0,maxtime=0,fade_ms=0)
def m1Play():#播放m1
    fileA = os.getcwd()
    aa = pygame.mixer.Sound(fileA+'/sounds/m1.wav')
    aa.play(loops=0,maxtime=0,fade_ms=0)
def m2Play():#播放m2
    fileB = os.getcwd()
    bb = pygame.mixer.Sound(fileB+'/sounds/m2.wav')
    bb.play(loops=0,maxtime=0,fade_ms=0)
def m3Play():##播放m3
    fileC = os.getcwd()
    cc = pygame.mixer.Sound(fileC+'/sounds/m3.wav')
    cc.play(loops=0,maxtime=0,fade_ms=0)
def draw():
    global ui,getlist1,getlist2,card,ys,jczy,xyzy,types,name,history,page,historytype,goldlist,bjnum,skip
    histxt=['角色活动祈愿-1','角色活动祈愿-2','武器活动祈愿','常驻祈愿']
    histxt2=['角色活动祈愿','角色活动祈愿','武器活动祈愿','常驻祈愿']
    mbpos=[173,215,258,298]
    bg.draw()
    if ui=='total':
        if types[1]=='2':
            for i in range(10):
                if getlist2[i]=='g':
                    pz[i].image='pzg.png'
                else:
                    pz[i].image='pzn.png'
                pz[i].draw()
                screen.draw.text(getlist1[i],center=[pz[i].x,248],fontname="1",fontsize=28,color=[200,200,110])
        else:
            ui='main'
            bg.image='bg'+types[0]+'.png'
    elif ui=='more':
        ups=''
        stars4=' '
        f=0
        for i in range(1,bjnum+1,1):
            if str(i) not in goldlist:
                f+=1
                if f%9==0:
                    if i<10:
                        stars4+='0'+str(i)+' '+name[i-1]+'\n'
                    else:
                        stars4+=str(i)+' '+name[i-1]+'\n'
                else:
                    if i<10:
                        stars4+='0'+str(i)+' '+name[i-1]+'   '
                    else:
                        stars4+=str(i)+' '+name[i-1]+'   '
        for i in range(len(goldlist)):
            ups+=goldlist[i-1]+' '+name[int(goldlist[i-1])-1]+'   '
        screen.draw.text(histxt[int(historytype)-1],center=[240, 82],fontname="1",fontsize=23,color=[88,84,81])#卡池类型
        screen.draw.text(ups,center=[466, 237],fontname="1",fontsize=18,color=[88,84,81])#卡池up
        screen.draw.text(stars4,center=[515, 427],fontname="1",fontsize=15,color=[88,84,81])#卡池4星up
    elif ui == 'history-1'or ui == 'history-2':
        if ui== 'history-2':
            whitemb.y=mbpos[int(historytype)-1]
            whitemb.draw()
        b = open(os.getcwd()+'/assets/user/lzx/history'+historytype+'num.txt','r')#打开userfiles1.txt
        a=b.read()
        b.close()
        f=0
        screen.draw.text(histxt[int(historytype)-1],center=[425, 123],fontname="1",fontsize=17,color=[96,83,74])#历史类型
        for i in range(5):
            if str(history[int(a)-i-(page-1)*5-1]) =='0' :
                screen.draw.text('无',center=[190, 273+f],fontname="1",fontsize=16,color=[143,142,137])#第一列
                screen.draw.text('无',center=[357, 273+f],fontname="1",fontsize=16,color=[143,142,137])#第二列
                screen.draw.text('无',center=[555, 273+f],fontname="1",fontsize=16,color=[143,142,137])#第三列
                screen.draw.text('无',center=[775, 273+f],fontname="1",fontsize=16,color=[143,142,137])#第四列
            else:
                screen.draw.text('角色',center=[190, 273+f],fontname="1",fontsize=16,color=[143,142,137])#第一列
                if str(history[int(a)-i-(page-1)*5-1]) in goldlist:
                    screen.draw.text(str(history[int(a)-i-(page-1)*5-1])+' '+name[int(history[int(a)-i-(page-1)*5-1])-1]+'（五星）',center=[357, 273+f],fontname="1",fontsize=16,color=[168,111,66])#第二列''''''
                else:
                    screen.draw.text(str(history[int(a)-i-(page-1)*5-1])+' '+name[int(history[int(a)-i-(page-1)*5-1])-1]+'（四星）',center=[357, 273+f],fontname="1",fontsize=16,color=[159,96,213])#第二列''''''
                screen.draw.text(histxt2[int(historytype)-1],center=[555, 273+f],fontname="1",fontsize=16,color=[143,142,137])#第三列
                screen.draw.text(str(historytime[int(a)-i-(page-1)*5-1]),center=[777, 273+f],fontname="1",fontsize=16,color=[143,142,137])#第四列
            f+=40            
        screen.draw.text(str(page),center=[512,482],fontname="1",fontsize=17,color=[88,84,81])#页码
    elif ui=='main':
        publicnotice.draw()
        YiLianButtom.draw()#祈愿1次
        ShiLianButtom.draw()#祈愿10次
        if skip:
            skipbt.image='skipbtt'
        else:
            skipbt.image='skipbtf'
        skipbt.draw()
        read()
        screen.draw.text(str(ys),center=[830, 26],fontname="1",fontsize=12,color="white")#原石
        screen.draw.text(str(0),center=[65, 519],fontname="1",fontsize=12,color="white")#星辉
        screen.draw.text(str(0),center=[130, 519],fontname="1",fontsize=12,color="white")#星尘
        screen.draw.text('跳过动画',center=[472, 505],fontname="1",fontsize=16,color="white")#开关
        if types[0]=='3':
            screen.draw.text(str(2)+' / 2',center=[81,486],fontname="1",fontsize=12,color=[168,111,66])#定轨命定值
        if types[0]=='4':
            screen.draw.text(str(xyzy),center=[924,26],fontname="1",fontsize=12,color="white")#相遇之缘
        else:
            screen.draw.text(str(jczy),center=[924,26],fontname="1",fontsize=12,color="white")#纠缠之缘
    elif ui=='stop':
        if types[1]=='1':
            screen.draw.text(str(card)+'/1',center=[500,100],fontname="1",fontsize=30,color="white")
        else:
            screen.draw.text(str(card)+'/10',center=[500,100],fontname="1",fontsize=30,color="white")
        if getlist2[card-1]=='g':
            screen.draw.text(getlist1[card-1],center=[500,240],fontname="1",fontsize=180,color="gold")
            screen.draw.text(name[int(getlist1[card-1])-1],center=[500,400],fontname="1",fontsize=100,color="gold")
        else:
            screen.draw.text(getlist1[card-1],center=[500,240],fontname="1",fontsize=180,color="white")
            screen.draw.text(name[int(getlist1[card-1])-1],center=[500,400],fontname="1",fontsize=100,color="white")
def on_mouse_up(pos,button):#鼠标抬起
    print(pos)
    global types,ui,card,goldlist,goldlists,bk,historytype,page,jczy,xyzy,skip
    b = open(os.getcwd()+'/assets/user/lzx/history'+historytype+'num.txt','r')#打开userfiles1.txt
    a=b.read()
    b.close()
    if ui=='main':
        if 315<pos[0]<395 and 15<pos[1]<50:#点击1卡池
            types[0]='1'
            goldlist=goldlists[int(types[0])-1]
            bg.image='bg'+types[0]+'.png'
            turnPlay()
        elif 415<pos[0]<505 and 15<pos[1]<50:#点击2卡池
            types[0]='2'  
            goldlist=goldlists[int(types[0])-1]
            turnPlay()
            bg.image='bg'+types[0]+'.png'
        elif 520<pos[0]<610and 15<pos[1]<50:#点击武器卡池
            types[0]='3'
            goldlist=goldlists[int(types[0])-1]
            turnPlay()
            bg.image='bg'+types[0]+'.png'
        elif 625<pos[0]<710 and 10<pos[1]<45:#点击常驻
            types[0]='4'
            goldlist=goldlists[int(types[0])-1]
            turnPlay()
            bg.image='bg'+types[0]+'.png'
        elif 970<pos[0]<995 and 270<pos[1]<305:#点击→
            if types[0]=='4':
                types[0]='1'
                goldlist=goldlists[int(types[0])-1]
                bg.image='bg'+types[0]+'.png'
            else:
                types[0]=str(int(types[0])+1)
                goldlist=goldlists[int(types[0])-1]
                bg.image='bg'+types[0]+'.png'
            turnPlay()
        elif 30<pos[0]<55 and 275<pos[1]<305:#点击←
            print('<-')
            if types[0]=='1':
                types[0]='4'
                goldlist=goldlists[int(types[0])-1]
                bg.image='bg'+types[0]+'.png'
            else:
                types[0]=str(int(types[0])-1)
                goldlist=goldlists[int(types[0])-1]
                bg.image='bg'+types[0]+'.png'
            turnPlay()
        elif 850<pos[0]<875 and 15<pos[1]<35:#点击+
            jczy+=30
            xyzy+=30
            write()
        elif 240<pos[0]<355 and 535<pos[1]<560 :#点击历史记录
            tapPlay()
            history_read()
            ui='history-1'
            page=1
            bg.image='hi2.jpg'
        elif 135<pos[0]<235 and 530<pos[1]<560:#点击详情
            tapPlay()
            ui='more'
            bg.image='more1.jpg'
        elif publicnotice.collidepoint(pos):#点击公告
            tapPlay()
            os.startfile(os.getcwd()+'/公告/start.pyw')
        elif YiLianButtom.collidepoint(pos):#点击1次
            tapPlay()
            types[1]='1'
            get1()
            time.sleep(0.01)
            if skip:
                ui='stop'
                card+=9
                bg.image='1purple (62).png'
                g=1020
                h=220
                for i in range(10):
                    pz[i].x=g
                    g+=80+h
                    h+=0
            else:
                ui='start'
            card=1
        elif ShiLianButtom.collidepoint(pos):#点击10次
            tapPlay()
            types[1]='2'
            get10()
            time.sleep(0.01)
            if skip:
                ui='total'
                bg.image='1purple (62).png'
                g=1020
                h=220
                for i in range(10):
                    pz[i].x=g
                    g+=80+h
                    h+=0
            else:
                ui='start'
            card=1
        elif skipbt.collidepoint(pos):
            if skip:
                skip=False
            else:
                skip=True
        historytype=types[0]
        print(goldlist)
    elif ui == 'more':
        if 940<pos[0]<975 and 65<pos[1]<105 :
                tapPlay()
                ui='main'
                bg.image='bg'+types[0]+'.png'
    elif ui == 'history-1':
            if int(a)%5==0:
                ans=int(int(a)/5)-1
            else:
                ans=int(int(a)/5)
            if 940<pos[0]<975 and 65<pos[1]<105 :
                tapPlay()
                ui='main'
                bg.image='bg'+types[0]+'.png'
            elif 350<pos[0]<895 and 105<pos[1]<145 :
                tapPlay()
                ui='history-2'
                bg.image='hi1.jpg'
            if 435<pos[0]<465 and 470<pos[1]<495 and page>=2:
                tapPlay()
                page-=1
            elif 555<pos[0]<600 and 470<pos[1]<495 and page<=ans:
                tapPlay()
                page+=1
    elif ui == 'history-2':
            if 340<pos[0]<905 and 150<pos[1]<310:
                page=1
                if 150<pos[1]<195:
                    historytype='1'
                elif 195<pos[1]<235:
                    historytype='2'
                elif 235<pos[1]<275:
                    historytype='3'
                elif 275<pos[1]<310:
                    historytype='4'
                history_read()
            tapPlay()
            ui='history-1'
            bg.image='hi2.jpg'
    elif ui=='total' and  pz[9].x==870:
        time.sleep(0.05)
        ui='main'
        bg.image='bg'+types[0]+'.png'
    elif ui=='stop':
        if types[1]=='1':
            card+=9
        if card>=10:
            ui='total'
            g=1020
            h=220
            for i in range(10):
                pz[i].x=g
                g+=80+h
                h+=0
        if bk:
            card+=1
            time.sleep(0.05)
def update():
    global ui,bgct
    if ui=='start':
        bgplay()
        if bgct>=62:
            bgct=1
            ui='stop'
        else:
            bgct+=1
    time.sleep(0.04)
    read()
    pzct()
MainMusicPlay()
pgzrun.go()