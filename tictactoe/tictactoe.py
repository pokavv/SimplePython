import random
import sys
import time
    
def choosePlayer():
    print('사용하실 문자를 고르세요.(영문자 X 또는 O 입력)') #'X : 선공', 'O : 후공' 
    while True:
        print('입력 : ', end='')
        chosen = input().upper()
        if chosen != 'O' and chosen !='X' :
            print('[오류] 잘못 입력하셨습니다. 영문자 O 또는 X를 입력해주세요.')
            print('------------------------------------------------------------------------')
            continue
        elif chosen == 'O':
            print('O를 고르셨습니다. 컴퓨터가 먼저 공격합니다.')
            return 'O','X'
        elif chosen == 'X':
            print('X를 고르셨습니다. 당신이 컴퓨터보다 먼저 공격합니다.')
            return 'X','O'        
############################################################################
          
def drawingBoard(screen):
    print()
    print()
    print('───────────────────────')
    print('   '+screen[6]+'   '+'│'+'   '+screen[7]+'   '+'│'+'   '+screen[8])
    print('───────────────────────')
    print('   '+screen[3]+'   '+'│'+'   '+screen[4]+'   '+'│'+'   '+screen[5])
    print('───────────────────────')
    print('   '+screen[0]+'   '+'│'+'   '+screen[1]+'   '+'│'+'   '+screen[2])
    print('───────────────────────')
    print()
    print()
 
############################################################################
    
def putPlayerStone(screen,mark):
    print('Your Turn. Specify your location')
    while True:
        print('>> 위치 지정 : ',end='')
        position = input()
        if position not in ['1', '2', '3', '4', '5' ,'6' ,'7' ,'8', '9'] :
            print('[오류]잘못된 값이 입력되었습니다. 1부터 9까지 입력가능합니다.')
            continue
        if screen[int(position)-1] != '':
            print('이미 돌이 놓여있습니다. 다른 곳에 놓아주세요.')
            continue
        else :
            break
    
    screen[int(position)-1] = mark
    print('당신은 '+position+'번 위치에 돌을 놓았습니다!')
    return position,screen
  
############################################################################
def putAIstone(screen,player,AI):
    print('컴퓨터의 차례입니다!')    
    AI_willPut_here=[] #컴퓨터가 놓을 위치    
    #플레이어가 돌을 놓은 위치를 확인
    Put_player = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0,9):
        if player == screen[i]:
            Put_player[i] = True       
          
    ###################################################
    #      컴퓨터의  승리 가능여부 확인    
    ###################################################
    #컴퓨터가 놓아서 승리할 수 있는 위치가 있는지 확인
    Put_AI = [False, False, False, False, False, False, False, False, False]
    for i in range(0,9):
        if AI == screen[i]:
            Put_AI[i] = True
    
   #컴퓨터의 돌이 가로로 2개 이상 놓였는지 확인
    hldx = 8
    while hldx >= 2:
        #한 쪽에 쏠려 놓인 경우
        if  Put_AI[hldx-1]==True:#가운데
            if Put_AI[hldx-1-1] == True: #왼쪽
                AI_willPut_here.append(hldx-1+1)
            elif Put_player[hldx-1+1] == True: #오른쪽
                AI_willPut_here.append(hldx-1-1)
        ##양쪽에 놓인 경우
        elif Put_AI[hldx-1-1] == True and Put_AI[hldx-1+1] == True:
            AI_willPut_here.append(hldx-1)
        hldx -= 3
    
    #컴퓨터의 돌이 세로로 2개 이상 놓였는지 확인
    vldx = 4
    while vldx <= 6:
        # 한쪽에 쏠려 놓인경우.
        if Put_AI[vldx-1] == True: #가운데 돌이 놓인경우
            if Put_AI[vldx-1+3] == True: #위쪽에 돌이 놓인 경우
                AI_willPut_here.append(vldx-1-3)
            elif Put_AI[vldx-1-3] == True: #아래쪽에 돌이 놓인 경우
                AI_willPut_here.append(vldx-1+3)
        #양쪽에 놓인 경우
        elif Put_AI[vldx-1+3] == True and Put_AI[vldx-1-3] == True:
            AI_willPut_here.append(vldx-1)
        vldx += 1
        
    #컴퓨터의 돌이 대각선으로 2개 이상 놓였는지 확인
    if Put_AI[5-1] == True: #5번에 돌이 놓인경우
        if Put_AI[7-1] == True:
            AI_willPut_here.append(3-1)
        elif Put_AI[3-1] == True:
            AI_willPut_here.append(7-1)
        elif Put_AI[9-1] == True:
            AI_willPut_here.append(1-1)
        elif Put_AI[1-1] == True:
            AI_willPut_here.append(9-1)
    if Put_AI[7-1] == True and Put_AI[3-1] == True:
        AI_willPut_here.append(5-1)
    if Put_AI[9-1] == True and Put_AI[1-1] == True:
        AI_willPut_here.append(5-1)

    #컴퓨터가 돌을 놓을 자리 선택
    for i in range(0,len(AI_willPut_here)):
        if screen[AI_willPut_here[i]] == '' :
            screen[AI_willPut_here[i]] = AI
            print('컴퓨터가 '+str(AI_willPut_here[i]+1)+'번 위치에 돌을 놓았습니다!')
            return screen
        
    ####################################################
    # 플레이어의 승리 막기                                #   
    ###################################################
    #플레이어의 돌이 가로로 2개 이상 놓였는지 확인
    hldx = 8
    while hldx >= 2:
        if Put_player[hldx-1] == True: #가운데 돌이 놓인경우
            if Put_player[hldx-1-1] == True: #왼쪽에 돌이 놓인 경우
                AI_willPut_here.append(hldx-1+1)
            elif Put_player[hldx-1+1] == True: #오른쪽에 돌이 놓인 경우
                AI_willPut_here.append(hldx-1-1)
        ##양쪽에 놓인 경우
        elif Put_player[hldx-1-1] == True and Put_player[hldx-1+1] == True:
            AI_willPut_here.append(hldx-1)
        hldx -= 3
    
    #플레이어의 돌이 세로로 2개 이상 놓였는지 확인
    vldx = 4
    while vldx <= 6:
        if Put_player[vldx-1] == True: #가운데 돌이 놓인경우
            if Put_player[vldx-1+3] == True: #위쪽에 돌이 놓인 경우
                AI_willPut_here.append(vldx-1-3)
            elif Put_player[vldx-1-3] == True: #아래쪽에 돌이 놓인 경우
                AI_willPut_here.append(vldx-1+3)
        #양쪽에 놓인 경우
        elif Put_player[vldx-1+3] == True and Put_player[vldx-1-3] == True:
            AI_willPut_here.append(vldx-1)
        vldx += 1
        
    #플레이어의 돌이 대각선으로 2개 이상 놓였는지 확인
    if Put_player[5-1] == True: #5번에 돌이 놓인경우
        if Put_player[7-1] == True:
            AI_willPut_here.append(3-1)
        elif Put_player[3-1] == True:
            AI_willPut_here.append(7-1)
        elif Put_player[9-1] == True:
            AI_willPut_here.append(1-1)
        elif Put_player[1-1] == True:
            AI_willPut_here.append(9-1)
    if Put_player[7-1] == True and Put_player[3-1] == True:
        AI_willPut_here.append(5-1)
    if Put_player[9-1] == True and Put_player[1-1] == True:
        AI_willPut_here.append(5-1)
 
   
    #돌을 놓을 자리 선택
    for i in range(0,len(AI_willPut_here)):
        if screen[AI_willPut_here[i]] == '' :
            screen[AI_willPut_here[i]] = AI
            print('컴퓨터가 '+str(AI_willPut_here[i]+1)+'번 위치에 돌을 놓았습니다!')
            return screen
    
    #놓을 자리를 못찾은 경우 랜덤하게 지정
    #if len(AI_willPut_here)==0:
    for i in range(0,9):
         if screen[i]=='':
            AI_willPut_here.append(i)
    available = []
    for i in range(0,len(AI_willPut_here)):
        if screen[AI_willPut_here[i]] == '' :
            available.append(AI_willPut_here[i])
    available = random.choice(available)
    screen[int(available)] = AI
    print('컴퓨터가 '+str(available+1)+'번 위치에 돌을 놓았습니다!')
    return screen
 
############################################################################
 
def checkWinner(screen,player,AI):
    ###################################################
    #   플레리어 승리 확인                         
    ###################################################
    #플레이어가 돌을 놓은 위치를 확인
    playerPut = [False, False, False, False, False, False, False, False, False]
    for i in range(0,9):
        if player == screen[i]:
            playerPut[i] = True
    #세로 확인
    vldx = 7
    while vldx<=9:
        if playerPut[vldx-1]==True and playerPut[vldx-1-3]==True and playerPut[vldx-1-6]==True :
            playerWin(screen)
            return True
        
        vldx+=1
    #가로 확인
    hldx = 7
    while hldx>=1:
        if playerPut[hldx-1]==True and playerPut[hldx-1+1]==True and playerPut[hldx-1+2]==True :
            playerWin(screen)
            return True
        
        hldx-=3
    #대각선 확인
    if playerPut[7-1]==True and playerPut[5-1]==True and playerPut[3-1]==True :
        playerWin(screen)
        return True
    
    elif playerPut[9-1]==True and playerPut[5-1]==True and playerPut[1-1]==True :
        playerWin(screen)
        return True
      
    #########################################
    #  컴퓨터의  승리 확인                     #
    #########################################
    #컴퓨터가 돌을 놓은 위치를 확인
    computerPut = [False, False, False, False, False, False, False, False, False]
    for i in range(0,9):
        if AI == screen[i]:
            computerPut[i] = True
    #세로 확인
    vldx = 7
    while vldx<=9:
        if computerPut[vldx-1]==True and computerPut[vldx-1-3]==True and computerPut[vldx-1-6]==True :
            comWin(screen)
            return True
        
        vldx+=1
    #가로 확인
    hldx = 7
    while hldx>=1:
        if computerPut[hldx-1]==True and computerPut[hldx-1+1]==True and computerPut[hldx-1+2]==True :
            comWin(screen)
            return True
        
        hldx-=3
    #대각선 확인
    if computerPut[7-1]==True and computerPut[5-1]==True and computerPut[3-1]==True :
        comWin(screen)
        return True
    
    elif computerPut[9-1]==True and computerPut[5-1]==True and computerPut[1-1]==True :
        comWin(screen)
        return True
    ###################################################
    #  무승부 확인                                      #    
    ###################################################
    for i in range(0,9):
        if screen[i]=='':
            break
        elif i==8:
            drawingBoard(screen)
            print()
            print('************************************************')
            print('                                 무승부입니다!                       ')
            print('************************************************')
            print()
            return True
          
def playerWin(gameScreen):
        drawingBoard(gameScreen) 
        print('************************************************') 
        print('                             플레이어가 승리했습니다!!                          ')
        print('************************************************') 
  
def comWin(gameScreen):
        drawingBoard(gameScreen)
        print() 
        print('************************************************')
        print('                                컴퓨터가 승리했습니다!!                              ')
        print('************************************************')
        print() 
        
##############################################################################
def replayGuide():
    print('다시 플레이 하시겠습니까? (1.네   /  2.아니요)')
    print(' >> 입력 : ',end='')
    temp = input()
    while True:
          if temp == '1':
            print()
            print('New Game!')
            print()
            break
          elif temp == '2':
            print()
            print('Good Bye!')
            print()
            sys.exit(0)
          else :
            print('You are Wrong! press 1 or 2')
            continue
 
    return True
 #################################################################### 
  
while True:
    gameScreen = ['', '', '', '', '' ,'' ,'' ,'', ''] # 순서대로 789456123
    player, AI = choosePlayer()
    drawingBoard(gameScreen)
    
    if player=='X': #선공
        while True:
            putPlayerStone(gameScreen, player)
            temp = checkWinner(gameScreen,player,AI)
            if temp==True:
                if replayGuide()==True:
                    break
            drawingBoard(gameScreen)
            time.sleep(1)
            
            putAIstone(gameScreen,player,AI)
            temp = checkWinner(gameScreen,player,AI)
            if temp==True:
                if replayGuide()==True:
                    break
            drawingBoard(gameScreen)
            time.sleep(1)
            
            
    elif player=='O': #후공
        while True:
            putAIstone(gameScreen,player,AI)
            temp = checkWinner(gameScreen,player,AI)
            if temp==True:
                if replayGuide()==True:
                    break
            drawingBoard(gameScreen)
            time.sleep(1)
            
            putPlayerStone(gameScreen, player)
            temp = checkWinner(gameScreen,player,AI)
            if temp==True:
                if replayGuide()==True:
                    break
            drawingBoard(gameScreen)
            time.sleep(1)