import pygame
import imgkit
import pyperclip
import tkinter as tk
from pynput.mouse import Button,Controller
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime,timezone,timedelta
tztboxactive=False
pygame.init()
activatecopybox=False
copyhoverhex=False
am_or_pm=''
copyhover=False
finaltime=''
colorstr=''
mouse_logger=Controller()
win=pygame.display.set_mode((900,500),flags=pygame.NOFRAME)
pygame.display.set_caption('solow viewer')
page=requests.get(f'https://colors.sashr.repl.co/colorsearch')
soup=BeautifulSoup(page.content,'html.parser')
with open('system files\\colors.json', 'w') as f:
    f.write(str(soup))
window=0
finalthing3=''
finalthing2=''
textinputclr=''
boxinput3text=''
boxcolor=54,57,63
boxinput3_active=False
boxinput1_active=False
boxinput2_active=False
disclr=255,255,255
textinputtext=""
boxinput1text=''
boxinput2text=''
soup=''
textbarwidth=200
textinputclractive=False
textinputactive=False
file_length=0
blinkline=1
came_from_enter=False
filedict=''
click_on_start=False
boxgraphamount=1
measure_by='chars'
tztboxtext=''
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if tztboxactive:
                if event.key==pygame.K_BACKSPACE:
                    tztboxtext=tztboxtext[0:-1]
                elif not event.key==pygame.K_RETURN:
                    tztboxtext+=event.unicode
            if boxinput1_active:
                if event.key==pygame.K_BACKSPACE:
                    boxinput1text= boxinput1text[0:-1]
                if event.key==pygame.K_1 or event.key==pygame.K_2 or event.key==pygame.K_3 or event.key==pygame.K_4 or event.key==pygame.K_5 or event.key==pygame.K_6 or event.key==pygame.K_7 or event.key==pygame.K_8 or event.key==pygame.K_9 or event.key==pygame.K_0:
                    boxinput1text+=event.unicode
                if event.key==pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    try:
                        int(pyperclip.paste())
                        boxinput1text+=pyperclip.paste()
                    except:
                        print('error')
            if textinputclractive:
                if event.key==pygame.K_BACKSPACE:
                        textinputclr= textinputclr[0:-1]
                if event.unicode=='_':
                    textinputclr+='_'
                if event.unicode=="\\":
                    textinputclr+='\\'
                if event.unicode==" ":
                    textinputclr+=" "
                if event.key==pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    textinputclr+=pyperclip.paste()
                if event.key==pygame.K_RETURN:
                    window=2
                    came_from_enter=True
                elif event.key==pygame.K_a or event.key==pygame.K_b or event.key==pygame.K_c or event.key==pygame.K_d or event.key==pygame.K_e or event.key==pygame.K_f or event.key==pygame.K_g or event.key==pygame.K_h or event.key==pygame.K_i or event.key==pygame.K_j or event.key==pygame.K_k or event.key==pygame.K_l or event.key==pygame.K_m or event.key==pygame.K_n or event.key==pygame.K_n or event.key==pygame.K_o or event.key==pygame.K_p or event.key==pygame.K_q or event.key==pygame.K_r or event.key==pygame.K_s or event.key==pygame.K_t or event.key==pygame.K_u or event.key==pygame.K_v or event.key==pygame.K_w or event.key==pygame.K_x or event.key==pygame.K_y or event.key==pygame.K_z or event.key==pygame.K_1 or event.key==pygame.K_2 or event.key==pygame.K_3 or event.key==pygame.K_4 or event.key==pygame.K_5 or event.key==pygame.K_6 or event.key==pygame.K_7 or event.key==pygame.K_7 or event.key==pygame.K_8 or event.key==pygame.K_9 or event.key==pygame.K_0:
                    textinputclr+= event.unicode
                    
            if boxinput2_active:
                if event.key==pygame.K_BACKSPACE:
                    boxinput2text= boxinput2text[0:-1]
                if event.key==pygame.K_1 or event.key==pygame.K_2 or event.key==pygame.K_3 or event.key==pygame.K_4 or event.key==pygame.K_5 or event.key==pygame.K_6 or event.key==pygame.K_7 or event.key==pygame.K_8 or event.key==pygame.K_9 or event.key==pygame.K_0:
                    boxinput2text+=event.unicode
                if event.key==pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    try:
                        int(pyperclip.paste())
                        boxinput2text+=pyperclip.paste()
                    except:
                        print('error')
            if boxinput3_active:
                if event.key==pygame.K_BACKSPACE:
                    boxinput3text= boxinput3text[0:-1]
                if event.key==pygame.K_1 or event.key==pygame.K_2 or event.key==pygame.K_3 or event.key==pygame.K_4 or event.key==pygame.K_5 or event.key==pygame.K_6 or event.key==pygame.K_7 or event.key==pygame.K_8 or event.key==pygame.K_9 or event.key==pygame.K_0:
                    boxinput3text+=event.unicode
                if event.key==pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    try:
                        int(pyperclip.paste())
                        boxinput2text+=pyperclip.paste()
                    except:
                        print('error')
            if window==1:
                if textinputactive:
                    if event.key==pygame.K_BACKSPACE:
                        textinputtext= textinputtext[0:-1]
                    if event.unicode=='_':
                        textinputtext+='_'
                    if event.unicode=="\\":
                        textinputtext+='\\'
                    if event.unicode==" ":
                        textinputtext+=" "
                    if event.key==pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        textinputtext+=pyperclip.paste()
                    if event.key==pygame.K_RETURN:
                        window=2
                        came_from_enter=True
                    elif event.key==pygame.K_a or event.key==pygame.K_b or event.key==pygame.K_c or event.key==pygame.K_d or event.key==pygame.K_e or event.key==pygame.K_f or event.key==pygame.K_g or event.key==pygame.K_h or event.key==pygame.K_i or event.key==pygame.K_j or event.key==pygame.K_k or event.key==pygame.K_l or event.key==pygame.K_m or event.key==pygame.K_n or event.key==pygame.K_n or event.key==pygame.K_o or event.key==pygame.K_p or event.key==pygame.K_q or event.key==pygame.K_r or event.key==pygame.K_s or event.key==pygame.K_t or event.key==pygame.K_u or event.key==pygame.K_v or event.key==pygame.K_w or event.key==pygame.K_x or event.key==pygame.K_y or event.key==pygame.K_z or event.key==pygame.K_1 or event.key==pygame.K_2 or event.key==pygame.K_3 or event.key==pygame.K_4 or event.key==pygame.K_5 or event.key==pygame.K_6 or event.key==pygame.K_7 or event.key==pygame.K_7 or event.key==pygame.K_8 or event.key==pygame.K_9 or event.key==pygame.K_0:
                        textinputtext+= event.unicode
    if textinputactive:
        if blinkline==1:
            textinputtext+='|'
    if tztboxactive:
        tztboxtext+='|'
    if boxinput2_active:
        boxinput2text+='|'
    if boxinput3_active:
        boxinput3text+='|'
    if boxinput1_active:
        boxinput1text+='|'
    if textinputclractive:
        textinputclr+='|'
    var=pygame.mouse.get_pos()
    mouse=pygame.Rect(var[0],var[1],15,15)
    pygame.draw.rect(win,(0,255,0),mouse)
    win.fill((54,57,63))
    titlebar=pygame.Rect(0,0,900,22)
    pygame.draw.rect(win,(32,34,37),titlebar)
    closebtn=pygame.Rect(880,2,21,20)
    pygame.draw.rect(win,(0,255,0),closebtn)
    exiter=pygame.image.load("images\\close.png")
    win.blit(exiter,(880,2))
    if mouse.colliderect(closebtn):
        click= pygame.mouse.get_pressed(3)[0]
        if click:
            run=False
    minibtn=pygame.Rect(855,2,21,20)
    pygame.draw.rect(win,(0,255,0),minibtn)
    minimizer=pygame.image.load("images\\minimize.png")
    win.blit(minimizer,(855,2))
    if mouse.colliderect(minibtn):
        click= pygame.mouse.get_pressed(3)[0]
        if click:
            pygame.display.iconify()
    if window==0:
        now=datetime.now()
        current_time_hour=now.strftime("%H")
        current_time_rest=now.strftime("%M:%S")
        if int(current_time_hour)>12:
            am_or_pm='pm'
            current_time_hour=int(current_time_hour)-12
            finaltime=f'{current_time_hour}:{current_time_rest}{am_or_pm}'
        else:
            am_or_pm='am'
            finaltime=f'{current_time_hour}:{current_time_rest}{am_or_pm}'
        myfont=pygame.font.SysFont('verdana',20)
        timerect=pygame.Rect(500,100,400,100)
        pygame.draw.rect(win,(32,34,37),timerect)
        if am_or_pm=='pm':
            myrendering=myfont.render('Good Afternoon',False,(255,255,255))
            win.blit(myrendering,(500,125))
        else:
            myrendering=myfont.render('Good Morning',False,(255,255,255))
            win.blit(myrendering,(500,125))
        myrendering=myfont.render(f'{finaltime}',False,(255,255,255))
        win.blit(myrendering,(500,150))
        coding_progressbtn=pygame.Rect(50,100,100,100)
        pygame.draw.rect(win,(0,0,0),coding_progressbtn)
        coding_progressimg1=pygame.image.load("images\\coding_progress.png")
        coding_progressimg=pygame.transform.scale(coding_progressimg1,(100,100))
        win.blit(coding_progressimg,(50,100))
        if mouse.colliderect(coding_progressbtn):
            coding_progress_hover=pygame.image.load('images\\coding_progress_hover.png')
            coding_progress_hover2=pygame.transform.scale(coding_progress_hover,(100,100))
            win.blit(coding_progress_hover2,(50,100))
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                window=1
        clockbtn=pygame.Rect(50,250,90,100)
        pygame.draw.rect(win,(0,255,0),clockbtn)
        clockbtnimg=pygame.image.load('images\\clockbtn.png')
        tinyclockbtnimg=pygame.transform.scale(clockbtnimg,(90,100))
        win.blit(tinyclockbtnimg,(50,250))
        if mouse.colliderect(clockbtn):
            clockbtnimghover=pygame.image.load('images\\clockbtnhover.png')
            tinyclockbtnhover=pygame.transform.scale(clockbtnimghover,(90,100))
            win.blit(tinyclockbtnhover,(50,250))
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                window=7
        make_a_graphbtn=pygame.Rect(200,100,100,100)
        pygame.draw.rect(win,(0,255,0),make_a_graphbtn)
        make_a_graphimg=pygame.image.load('images\\make_a_graph.png')
        make_a_graphmini=pygame.transform.scale(make_a_graphimg,(100,100))
        win.blit(make_a_graphmini,(200,100))
        if mouse.colliderect(make_a_graphbtn):
            make_a_graphimghover=pygame.image.load('images\\make_a_graph_hover.png')
            make_a_graphminihover=pygame.transform.scale(make_a_graphimghover,(100,100))
            win.blit(make_a_graphminihover,(200,100))
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                window=3
        colorbtn=pygame.Rect(320,100,100,100)
        pygame.draw.rect(win,(0,255,0),colorbtn)
        colorimg=pygame.image.load('images\\colorbtn.png')
        colorimg2=pygame.transform.scale(colorimg,(100,100))
        win.blit(colorimg2,(320,100))
        if mouse.colliderect(colorbtn):
            colorimghvr=pygame.image.load('images\\colorbtnhover.png')
            colorimghvr2=pygame.transform.scale(colorimghvr,(100,100))
            win.blit(colorimghvr2,(320,100))
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                window=6
    elif window==1:
        donebtn=pygame.Rect(840,460,50,25)
        pygame.draw.rect(win,(0,255,0),donebtn)
        doneimg=pygame.image.load('images\\donebtn.png')
        minidoneimg=pygame.transform.scale(doneimg,(50,30))
        win.blit(minidoneimg,(840,460))
        if mouse.colliderect(donebtn):
            doneimghover=pygame.image.load('images\\donebtnhover.png')
            minidoneimghover=pygame.transform.scale(doneimghover,(50,30))
            win.blit(minidoneimghover,(840,460))
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                came_from_enter=True
                window=2
        sidebar=pygame.Rect(0,0,150,500)
        pygame.draw.rect(win,(32,34,37),sidebar)
        backbox=pygame.Rect(2,80,30,30)
        pygame.draw.rect(win,(54,57,63),backbox)
        back=pygame.image.load('images\\back.png')
        back2=pygame.transform.scale(back,(30,30))
        win.blit(back2,(2,80))
        if mouse.colliderect(backbox):
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                window=0
        titlefont=pygame.font.SysFont('verdana',30)
        theheading=titlefont.render('please pick a file', False,(255,255,255))
        win.blit(theheading,(220,50))
        browsebtn=pygame.Rect(238,103,62,37)
        pygame.draw.rect(win,(255,0,0),browsebtn)
        browseimg=pygame.image.load('images\\browsebtn.png')
        win.blit(browseimg,(238,103))
        if mouse.colliderect(browsebtn):
            browseimghover=pygame.image.load('images\\browsebtnhover.png')
            win.blit(browseimghover,(238,103))
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                windo=tk.Tk()
                windo.withdraw()
                filedict=filedialog.askopenfilename()
                click_on_start=True
                window=2
        pygame.font.init()
        myfont=pygame.font.SysFont("verdana", 40)
        hahafont=pygame.font.SysFont('verdana', 25)
        heading=hahafont.render('Coding', False,disclr)
        win.blit(heading,(35,80))
        line=myfont.render('______', False, (255,255,255))
        win.blit(line,(0,90))
        back1=pygame.image.load('images\\back.png')
        back12=pygame.transform.scale(back,(30,30))
        win.blit(back12,(2,80))
        textbar=pygame.Rect(300,105, textbarwidth, 35)
        pygame.draw.rect(win,(255,255,255),textbar)
        textinputfont=pygame.font.SysFont("verdana", 32)
        textinputrendering=textinputfont.render(textinputtext,False,(0,0,0))
        win.blit(textinputrendering,(300,100))
        textbarwidth=max(500,textinputrendering.get_width())
        if mouse.colliderect(textbar):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                textinputactive=True
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                textinputactive=False
        textinputtext=textinputtext.strip('|')
    elif window==2:
        if came_from_enter:
            filedict=textinputtext.strip('|')
            came_from_enter=False
        if click_on_start:
            mouse_logger.click(Button.left, 1)
            click_on_start=False
        dictdisplayer=pygame.font.SysFont('verdana', 15)
        sidebar=pygame.Rect(0,0,150,500)
        pygame.draw.rect(win,(32,34,37),sidebar)
        backbox=pygame.Rect(2,80,30,30)
        pygame.draw.rect(win,(54,57,63),backbox)
        back=pygame.image.load('images\\back.png')
        back2=pygame.transform.scale(back,(30,30))
        win.blit(back2,(2,80))
        if mouse.colliderect(backbox):
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                window=0
        hahafont=pygame.font.SysFont('verdana', 25)
        heading=hahafont.render('Coding', False,disclr)
        win.blit(heading,(35,80))
        line=myfont.render('______', False, (255,255,255))
        win.blit(line,(0,90))
        rendering=dictdisplayer.render(f'file information of file {filedict}',False,(255,255,255))
        win.blit(rendering,(160,30))
        try:
            with open(f'{filedict}','r') as f:
                content=f.readlines()
                file_length_lines=len(content)
                infodisplayer=pygame.font.SysFont('calibri', 20)
                renderinginfo1=infodisplayer.render(f'lines:{file_length_lines}',False,(255,255,255))
                win.blit(renderinginfo1,(10,200))
            with open(f'{filedict}','r') as f:
                content2=f.read()
                charsamount=len(content2)
                renderinginfo2=infodisplayer.render(f'chars:{charsamount}',False,(255,255,255))
                win.blit(renderinginfo2,(10,250))
            if measure_by=='chars':
                btnselectorlines=pygame.Rect(525,100,375,10)
                charsselect=pygame.image.load('images\\selectorchars.png')
                thisfont=pygame.font.SysFont('verdana',20)
                linesthing=thisfont.render('lines',False,(255,255,255))
                win.blit(linesthing,(700,70))
                charsthing=thisfont.render('chars',False,(255,255,255))
                win.blit(charsthing,(300,70))
                charsselect2=pygame.transform.scale(charsselect,(750,5))
                win.blit(charsselect2,(150,100))
                charsdivider=0-charsamount//5
                graphrect=pygame.Rect(250,500,100,charsdivider)
                pygame.draw.rect(win,(255,202,40),graphrect)
                measure=pygame.image.load('images\\graphmeasurement.png')
                win.blit(measure,(200,108))
                if mouse.colliderect(btnselectorlines):
                    linehover=pygame.image.load('images\\selectorlineshover.png')
                    linehover2=pygame.transform.scale(linehover,(750,5))
                    win.blit(linehover2,(150,100))
                    click=pygame.mouse.get_pressed(3)[0]
                    if click:
                        measure_by='lines'
            elif measure_by=='lines':
                btnselectorchars=pygame.Rect(150,100,375,10)
                linesselect=pygame.image.load('images\\selectorlines.png')
                linesselect2=pygame.transform.scale(linesselect,(750,5))
                win.blit(linesselect2,(150,100))
                thisfont=pygame.font.SysFont('verdana',20)
                linesthing=thisfont.render('lines',False,(255,255,255))
                win.blit(linesthing,(700,70))
                charsthing=thisfont.render('chars',False,(255,255,255))
                win.blit(charsthing,(300,70))
                linedivider=0-file_length_lines//5
                graphrect=pygame.Rect(250,500,100,linedivider)
                pygame.draw.rect(win,(255,202,40),graphrect)
                measure=pygame.image.load('images\\graphmeasurement.png')
                win.blit(measure,(200,108))
                if mouse.colliderect(btnselectorchars):
                    charshover=pygame.image.load('images\\selectorcharshover.png')
                    charshover2=pygame.transform.scale(charshover,(750,5))
                    win.blit(charshover2,(150,100))
                    click=pygame.mouse.get_pressed(3)[0]
                    if click:
                        measure_by='chars'
        except FileNotFoundError:
            print('error')
    elif window==3:
        myfont=pygame.font.SysFont("verdana", 40)
        sidebar=pygame.Rect(0,0,150,500)
        pygame.draw.rect(win,(32,34,37),sidebar)
        backbox=pygame.Rect(2,80,30,30)
        pygame.draw.rect(win,(54,57,63),backbox)
        back=pygame.image.load('images\\back.png')
        back2=pygame.transform.scale(back,(30,30))
        win.blit(back2,(2,80))
        if mouse.colliderect(backbox):
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                window=0
        lolfont=pygame.font.SysFont('verdana', 25)
        heading=lolfont.render('Graph', False,disclr)
        win.blit(heading,(35,80))
        line=myfont.render('______', False, (255,255,255))
        win.blit(line,(0,90))
        smolfont=pygame.font.SysFont('verdana', 20)
        smoltext1=smolfont.render('bar 1:' ,False, (255,255,255))
        win.blit(smoltext1,(780,48))
        boxinput1=pygame.Rect(850,50,50,20)
        pygame.draw.rect(win,(255,255,255),boxinput1)
        boxinputtext11=smolfont.render(f'{boxinput1text}',False,(0,0,0))
        win.blit(boxinputtext11,(850,47))
        if mouse.colliderect(boxinput1):
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                boxinput1_active=True
        else:
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                boxinput1_active=False
        boxinput1text=boxinput1text.strip('|')
        addgraph=pygame.Rect(848,80,51,30)
        pygame.draw.rect(win,(255,0,0),addgraph)
        addbtn=pygame.image.load('images\\addbtn.png')
        miniaddbtn=pygame.transform.scale(addbtn,(51,30))
        win.blit(miniaddbtn,(848,80))
        if mouse.colliderect(addgraph):
            addbtnhover=pygame.image.load('images\\addbtnhover.png')
            miniaddbtnhover=pygame.transform.scale(addbtnhover,(51,30))
            win.blit(miniaddbtnhover,(848,80))
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                window=4
        if boxinput1text=='':
            finalthing1='0'
        else:
            finalthing1=boxinput1text
        equation=0-int(finalthing1)//5
        inputdisplayer1=pygame.Rect(600,450,100,equation)
        pygame.draw.rect(win,(196, 90, 90),inputdisplayer1)
    elif window==4:
        myfont=pygame.font.SysFont("verdana", 40)
        sidebar=pygame.Rect(0,0,150,500)
        pygame.draw.rect(win,(32,34,37),sidebar)
        backbox=pygame.Rect(2,80,30,30)
        pygame.draw.rect(win,(54,57,63),backbox)
        back=pygame.image.load('images\\back.png')
        back2=pygame.transform.scale(back,(30,30))
        win.blit(back2,(2,80))
        if mouse.colliderect(backbox):
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                window=0
        lolfont=pygame.font.SysFont('verdana', 25)
        heading=lolfont.render('Graph', False,disclr)
        win.blit(heading,(35,80))
        line=myfont.render('______', False, (255,255,255))
        win.blit(line,(0,90))
        smolfont=pygame.font.SysFont('verdana', 20)
        smoltext1=smolfont.render('bar 1:' ,False, (255,255,255))
        win.blit(smoltext1,(780,48))
        boxinput1=pygame.Rect(850,50,50,20)
        pygame.draw.rect(win,(255,255,255),boxinput1)
        smolfont=pygame.font.SysFont('verdana', 20)
        smoltext1=smolfont.render('bar 2:' ,False, (255,255,255))
        win.blit(smoltext1,(780,78))
        boxinput1=pygame.Rect(850,50,50,20)
        pygame.draw.rect(win,(255,255,255),boxinput1)
        boxinput2=pygame.Rect(850,80,50,20)
        pygame.draw.rect(win,(255,255,255),boxinput2)
        boxinputtext11=smolfont.render(f'{boxinput1text}',False,(0,0,0))
        win.blit(boxinputtext11,(850,47))
        if mouse.colliderect(boxinput1):
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                boxinput1_active=True
        else:
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                boxinput1_active=False
                boxinput1text=boxinput1text.strip('|')
        boxinputtext21=smolfont.render(f'{boxinput2text}',False,(0,0,0))
        win.blit(boxinputtext21,(850,77))
        if mouse.colliderect(boxinput2):
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                boxinput2_active=True
        else:
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                boxinput2_active=False
                boxinput2text=boxinput2text.strip('|')
        addgraph=pygame.Rect(848,110,51,30)
        pygame.draw.rect(win,(255,0,0),addgraph)
        addbtn=pygame.image.load('images\\addbtn.png')
        miniaddbtn=pygame.transform.scale(addbtn,(51,30))
        win.blit(miniaddbtn,(848,110))
        if mouse.colliderect(addgraph):
            addbtnhover=pygame.image.load('images\\addbtnhover.png')
            miniaddbtnhover=pygame.transform.scale(addbtnhover,(51,30))
            win.blit(miniaddbtnhover,(848,110))
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                window=5
        if boxinput1_active:
            boxinput1text=boxinput1text.strip('|')
        if boxinput2_active:
            boxinput2text=boxinput2text.strip('|')
        if boxinput1text=='':
            finalthing1='0'
        else:
            finalthing1=boxinput1text
        equation=0-int(finalthing1)//5
        inputdisplayer1=pygame.Rect(600,450,100,equation)
        pygame.draw.rect(win,(196, 90, 90),inputdisplayer1)
        if boxinput2text=='':
            finalthing2='0'
        else:
            finalthing2=boxinput2text
        equation=0-int(finalthing2)//5
        inputdisplayer2=pygame.Rect(450,450,100,equation)
        pygame.draw.rect(win,(255, 212, 20),inputdisplayer2)
        if boxinput1text=='':
            finalthing1='0'
        else:
            finalthing1=boxinput1text
        equation=0-int(finalthing1)//5
        inputdisplayer1=pygame.Rect(600,450,100,equation)
        pygame.draw.rect(win,(196, 90, 90),inputdisplayer1)
    elif window==5:
        myfont=pygame.font.SysFont("verdana", 40)
        sidebar=pygame.Rect(0,0,150,500)
        pygame.draw.rect(win,(32,34,37),sidebar)
        backbox=pygame.Rect(2,80,30,30)
        pygame.draw.rect(win,(54,57,63),backbox)
        back=pygame.image.load('images\\back.png')
        back2=pygame.transform.scale(back,(30,30))
        win.blit(back2,(2,80))
        if mouse.colliderect(backbox):
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                window=0
        lolfont=pygame.font.SysFont('verdana', 25)
        heading=lolfont.render('Graph', False,disclr)
        win.blit(heading,(35,80))
        line=myfont.render('______', False, (255,255,255))
        win.blit(line,(0,90))
        smolfont=pygame.font.SysFont('verdana', 20)
        smoltext1=smolfont.render('bar 1:' ,False, (255,255,255))
        win.blit(smoltext1,(780,48))
        boxinput1=pygame.Rect(850,50,50,20)
        pygame.draw.rect(win,(255,255,255),boxinput1)
        smolfont=pygame.font.SysFont('verdana', 20)
        smoltext1=smolfont.render('bar 2:' ,False, (255,255,255))
        win.blit(smoltext1,(780,78))
        smolfont=pygame.font.SysFont('verdana', 20)
        smoltext1=smolfont.render('bar 3:' ,False, (255,255,255))
        win.blit(smoltext1,(780,108))
        boxinput1=pygame.Rect(850,50,50,20)
        pygame.draw.rect(win,(255,255,255),boxinput1)
        boxinput3=pygame.Rect(850,110,50,20)
        pygame.draw.rect(win,(255,255,255),boxinput3)
        boxinput2=pygame.Rect(850,80,50,20)
        pygame.draw.rect(win,(255,255,255),boxinput2)
        boxinputtext11=smolfont.render(f'{boxinput1text}',False,(0,0,0))
        boxinputtext31=smolfont.render(f'{boxinput3text}',False, (0,0,0))
        boxinput3text=boxinput3text.strip('|')
        win.blit(boxinputtext31,(850,107))
        win.blit(boxinputtext11,(850,47))
        if mouse.colliderect(boxinput3):
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                boxinput3_active=True
        else:
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                boxinput3_active=False
        if mouse.colliderect(boxinput1):
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                boxinput1_active=True
        else:
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                boxinput1_active=False
                boxinput1text=boxinput1text.strip('|')
        boxinputtext21=smolfont.render(f'{boxinput2text}',False,(0,0,0))
        win.blit(boxinputtext21,(850,77))
        if mouse.colliderect(boxinput2):
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                boxinput2_active=True
        else:
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                boxinput2_active=False
                boxinput2text=boxinput2text.strip('|')
        if boxinput1_active:
            boxinput1text=boxinput1text.strip('|')
        if boxinput2_active:
            boxinput2text=boxinput2text.strip('|')
        if boxinput3text=='':
            finalthing3='0'
        else:
            finalthing3=boxinput3text
        equation=0-int(finalthing3)//5
        inputdisplayer3=pygame.Rect(300,450,100,equation)
        pygame.draw.rect(win,(255,255,255),inputdisplayer3)
        if boxinput2text=='':
            finalthing2='0'
        else:
            finalthing2=boxinput2text
        equation=0-int(finalthing2)//5
        inputdisplayer2=pygame.Rect(450,450,100,equation)
        pygame.draw.rect(win,(255, 212, 20),inputdisplayer2)
        if boxinput1text=='':
            finalthing1='0'
        else:
            finalthing1=boxinput1text
        equation=0-int(finalthing1)//5
        inputdisplayer1=pygame.Rect(600,450,100,equation)
        pygame.draw.rect(win,(196, 90, 90),inputdisplayer1)
    elif window==6:
        copyrectrgb=pygame.Rect(470,190,60,30)
        pygame.draw.rect(win,(0,255,0),copyrectrgb)
        copyrecthex=pygame.Rect(470,220,60,30)
        pygame.draw.rect(win,(0,255,0),copyrecthex)
        thisbox=pygame.Rect(150,20,750,480)
        pygame.draw.rect(win,(boxcolor),thisbox)
        sidebar=pygame.Rect(0,0,150,500)
        pygame.draw.rect(win,(32,34,37),sidebar )
        backbox=pygame.Rect(2,80,30,30)
        pygame.draw.rect(win,(54,57,63),backbox)
        back=pygame.image.load('images\\back.png')
        back2=pygame.transform.scale(back,(30,30))
        win.blit(back2,(2,80))
        if mouse.colliderect(backbox):
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                window=0
        lolfont=pygame.font.SysFont('verdana', 25)
        heading=lolfont.render('Colors', False,disclr)
        win.blit(heading,(35,80))
        myfont=pygame.font.SysFont("verdana", 40)
        line=myfont.render('______', False, (255,255,255))
        win.blit(line,(0,90))
        textbox=pygame.Rect(200,100,300,30)
        pygame.draw.rect(win,(255,255,255),textbox)
        if mouse.colliderect(textbox):
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                textinputclractive=True
        else:
            if mouse.colliderect(copyrectrgb):
                click=pygame.mouse.get_pressed(3)[0]
                if activatecopybox:
                    copyhover=True
                elif click:
                    textinputclractive=False
            if mouse.colliderect(copyrecthex):
                if activatecopybox:
                    copyhoverhex=True
            else:
                click=pygame.mouse.get_pressed(3)[0]
                if click:
                    textinputclractive=False
        thefont=pygame.font.SysFont('verdana', 30)
        rendering=thefont.render(f'{textinputclr}',False,(0,0,0))
        win.blit(rendering,(200,95))
        if textinputclractive:
            textinputclr=textinputclr.strip('|')
            try:
                with open('system files//colors.json','r') as f:
                    jsonthing=json.load(f)
                    colorstr=jsonthing[f'{textinputclr}']
                    colorstr2=colorstr.split(',')
                    boxcolor=int(colorstr2[0]),int(colorstr2[1]),int(colorstr2[2])
                    infobox=pygame.image.load('images\\infobox.png')
                    win.blit(infobox,(152,130))
                    rgbccrendering=lolfont.render(f'rgb color code: {colorstr}',False,(0,0,0))
                    win.blit(rgbccrendering,(160,190))
                    hexclrcode='#%02x%02x%02x' % (int(colorstr2[0]), int(colorstr2[1]), int(colorstr2[2]))
                    hexccrendering=lolfont.render(f'hex color code: {hexclrcode}',False,(0,0,0))
                    win.blit(hexccrendering,(160,220))
                    copyrectrgbimg=pygame.image.load('images\\copybtn.png')
                    copyrectbtnimg2=pygame.transform.scale(copyrectrgbimg,(60,30))
                    win.blit(copyrectbtnimg2,(470,190))
                    copyrectheximg=pygame.image.load('images\\copybtn.png')
                    copyrectbtnimg21=pygame.transform.scale(copyrectheximg,(60,30))
                    win.blit(copyrectbtnimg21,(470,220))
                    if copyhover:
                        copyrectrgbimghvr=pygame.image.load('images\\copybtnhover.png')
                        copyrectbtnimghvr2=pygame.transform.scale(copyrectrgbimghvr,(60,30))
                        win.blit(copyrectbtnimghvr2,(470,220))
                        click=pygame.mouse.get_pressed(3)[0]
                        if click:
                            pyperclip.copy(colorstr)
                        copyhover=False
                    if copyhoverhex:
                        copyrectheximghvr=pygame.image.load('images\\copybtnhover.png')
                        copyrectbtnimghvr21=pygame.transform.scale(copyrectheximghvr,(60,30))
                        win.blit(copyrectbtnimghvr21,(470,220))
                        click=pygame.mouse.get_pressed(3)[0]
                        if click:
                            pyperclip.copy(hexclrcode)
                        copyhoverhex=False
                    activatecopybox=True
            except:
                boxcolor=54,57,63
                activatecopybox=False
        else:
            textinputclr=textinputclr.strip('|')
    elif window==7:
        sidebar=pygame.Rect(0,0,150,500)
        pygame.draw.rect(win,(32,34,37),sidebar)
        backbox=pygame.Rect(2,80,30,30)
        pygame.draw.rect(win,(54,57,63),backbox)
        back=pygame.image.load('images\\back.png')
        back2=pygame.transform.scale(back,(30,30))
        win.blit(back2,(2,80))
        if mouse.colliderect(backbox):
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                window=0
        lolfont=pygame.font.SysFont('verdana', 25)
        heading=lolfont.render('Clock', False,disclr)
        win.blit(heading,(35,80))
        myfont=pygame.font.SysFont("verdana", 40)
        line=myfont.render('______', False, (255,255,255))
        win.blit(line,(0,90))
        tztbox=pygame.Rect(200,100,300,25)
        pygame.draw.rect(win,(255,255,255),tztbox)
        displaytzt=lolfont.render(f'{tztboxtext}',False,(0,0,0))
        win.blit(displaytzt,(205,98))
        if mouse.colliderect(tztbox):
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                tztboxactive=True
        else:
            click=pygame.mouse.get_pressed(3)[0]
            if click:
                tztboxactive=False
        tztboxtext=tztboxtext.strip('|')
        try:
            offset=tztboxtext
            if offset.startswith('+'):
                direction=1
            else:
                direction=-1
            off_hours, off_minutes = map(int, offset[1:].split(':'))
            tz= timezone(timedelta(hours=off_hours, minutes=off_minutes)*direction)
            infobox=pygame.image.load('images\\infobox.png')
            win.blit(infobox,(152,130))
            time24hr=datetime.now(tz).strftime('%H:%M:%S').split(':')
            am_or_pm_tz=''
            time12hr=''
            if int(time24hr[0])>12:
               am_or_pm_tz='pm'
            else:
                am_or_pm_tz='am'
            if am_or_pm_tz=='pm':
                time12hr=f'{int(time24hr[0])-12}:{time24hr[1]}:{time24hr[2]} {am_or_pm_tz}'
            else:
                time12hr=f'{time24hr[0]}:{time24hr[1]}:{time24hr[2]} {am_or_pm_tz}'
            timedisplayer=lolfont.render(time12hr,False,(0,0,0))
            win.blit(timedisplayer,(165,190))
        except:
                try:
                    with open('system files\\timezones.json','r') as f:
                        jsonfile=json.load(f)
                        offset=jsonfile[f'{tztboxtext}']
                        if offset.startswith('+'):
                            direction=1
                        else:
                            direction=-1
                        off_hours, off_minutes = map(int, offset[1:].split(':'))
                        tz= timezone(timedelta(hours=off_hours, minutes=off_minutes)*direction)
                        infobox=pygame.image.load('images\\infobox.png')
                        win.blit(infobox,(152,130))
                        time24hr=datetime.now(tz).strftime('%H:%M:%S').split(':')
                        am_or_pm_tz=''
                        if int(time24hr[0])>12:
                            am_or_pm_tz='pm'
                        else:
                            am_or_pm_tz='am'
                        if am_or_pm_tz=='pm':
                            time12hr=f'{int(time24hr[0])-12}:{time24hr[1]}:{time24hr[2]} {am_or_pm_tz}'
                        else:
                            time12hr=f'{time24hr[0]}:{time24hr[1]}:{time24hr[2]} {am_or_pm_tz}'
                        utcrender=lolfont.render(f'UTC offset: {offset}',False,(0,0,0))
                        win.blit(utcrender,(165,190))
                        timerender=lolfont.render(time12hr,False,(0,0,0))
                        win.blit(timerender,(165,220))
                except:
                    pass
    solowlogo=pygame.image.load('images\\solow_logo.png')
    solowlogo2=pygame.transform.scale(solowlogo,(60,22))
    win.blit(solowlogo2,(0,0))
    pygame.display.flip()
pygame.quit()