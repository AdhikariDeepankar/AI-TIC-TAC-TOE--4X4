# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 21:36:48 2020

@author: deepa
"""
import sys
diff = 50
#make a board 
matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#we will give 1 to player 1 and 2 to player 2
input_array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #stores the input of the players for all the 16 boxes

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Start of MINIMAX code xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def winCheck(matrix):
    #1st row check
    
    a=matrix[0][0]
    b=matrix[0][1]
    c=matrix[0][2]
    d=matrix[0][3]
    if a==1 and b==1 and c==1 and d==1:
        return 1
    elif a==2 and b==2 and c==2 and d==2:
        return 2
    
        
    #2nd row check
    
    a=matrix[1][0]
    b=matrix[1][1]
    c=matrix[1][2]
    d=matrix[1][3]
    if a==1 and b==1 and c==1 and d==1:
        return 1
    elif a==2 and b==2 and c==2 and d==2:
        return 2
       
        
    #3rd row check
    
    a=matrix[2][0]
    b=matrix[2][1]
    c=matrix[2][2]
    d=matrix[2][3]
    if a==1 and b==1 and c==1 and d==1:
        return 1
    elif a==2 and b==2 and c==2 and d==2:
        return 2
    
        
    #4th row check
    a=matrix[3][0]
    b=matrix[3][1]
    c=matrix[3][2]
    d=matrix[3][3]
    if a==1 and b==1 and c==1 and d==1:
        return 1
    elif a==2 and b==2 and c==2 and d==2:
        return 2
       
        
    #1st column check
    a=matrix[0][0]
    b=matrix[1][0]
    c=matrix[2][0]
    d=matrix[3][0]
    if a==1 and b==1 and c==1 and d==1:
        
        return 1
    elif a==2 and b==2 and c==2 and d==2:
        return 2
        
        
    #2nd column check
    a=matrix[0][1]
    b=matrix[1][1]
    c=matrix[2][1]
    d=matrix[3][1]
    if a==1 and b==1 and c==1 and d==1:
        
        return 1
    elif a==2 and b==2 and c==2 and d==2:
        return 2
       
        
    #3rd column check
    a=matrix[0][2]
    b=matrix[1][2]
    c=matrix[2][2]
    d=matrix[3][2]
    if a==1 and b==1 and c==1 and d==1:
        return 1
    elif a==2 and b==2 and c==2 and d==2:
        return 2
        
        
    #4th column check
    a=matrix[0][3]
    b=matrix[1][3]
    c=matrix[2][3]
    d=matrix[3][3]
    if a==1 and b==1 and c==1 and d==1:
        return 1
    elif a==2 and b==2 and c==2 and d==2:
        return 2
        
        
    #major diagonal check
    a=matrix[0][0]
    b=matrix[1][1]
    c=matrix[2][2]
    d=matrix[3][3]
    if a==1 and b==1 and c==1 and d==1:
        return 1
    elif a==2 and b==2 and c==2 and d==2:
        return 2
        
        
    #minor diagonal check
    a=matrix[0][3]
    b=matrix[1][2]
    c=matrix[2][1]
    d=matrix[3][0]
    if a==1 and b==1 and c==1 and d==1:
        return 1
    elif a==2 and b==2 and c==2 and d==2:
        return 2
    else:
        return 0
#end of check function
        
def result(matrix):
    if winCheck(matrix)==1:
        print('Player 1 wins')
    elif winCheck(matrix) ==2:
        print('Player 2 wins')
    sys.exit()

def terminal_state(matrix):
    if winCheck(matrix)==1:
        return 1
    elif winCheck(matrix) ==2:
        return 1
    else:
        spaces = available_spaces(matrix)
        if len(spaces) == 0:
            return 1
                

def printBoard(matrix):
    for j in range(0,4):
        for k in range(0,4):
            print(matrix[j][k], end =" ")
        print()
 
def available_spaces(matrix):
    listofEmptyPlaces= []
    i=0
    for j in range(0,4):
        for k in range(0,4):
            if matrix[j][k]==0:
                listofEmptyPlaces.append(i)
            i=i+1
    return listofEmptyPlaces

#max is player1
#min is player2
    
   

def utility(matrix):
    value=0
    #checked rows
    for j in range(0,4):
        num1 = 0
        num2 = 0
        for k in range(0,4):
            if matrix[j][k] == 1:
                num1=num1+1
            elif matrix[j][k] == 2:
                num2=num2+1
        if num1>=num2:  #may remove equality sign later
            value = value+ (10**(num1-num2))
        else:
            value = value- (10**(num2-num1))
    
    #checked columns        
    for j in range(0,4):
        num1 = 0
        num2 = 0
        for k in range(0,4):
            if matrix[k][j] == 1:
                num1=num1+1
            elif matrix[k][j] == 2:
                num2=num2+1
        if num1>=num2:
            value = value+ (10**(num1-num2))
        else:
            value = value- (10**(num2-num1))
            
    #checking for major axis
    num1=0
    num2=0
    for j in range(0,4):
        if matrix[j][j] == 1:
            num1=num1+1
        elif matrix[j][j] == 2:
            num2=num2+1
    if num1>=num2:
        value = value+ (10**(num1-num2))
    else:
        value = value- (10**(num2-num1))
            
    #checking for minor axis
    num1=0
    num2=0
    for j in range(0,4):
        if matrix[j][3-j] == 1:
            num1=num1+1
        elif matrix[j][3-j] == 2:
            num2=num2+1
    if num1>=num2:
        value = value+ (10**(num1-num2))
    else:
        value = value- (10**(num2-num1))
        
    return value
        
    
def available_states(matrix,num):
    availableChoice = available_spaces(matrix)
    neighbourStates= []
    for i in availableChoice:
        temp = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for j in range(0,4):
            for k in range(0,4):
                temp[j][k]=matrix[j][k]
        temp[int(i/4)][i%4]=num
        neighbourStates.append(temp)
    return neighbourStates
    
    
def max_value(matrix,level):
    if terminal_state(matrix)==1 or level==0 or level==-1:
        return utility(matrix)
    v=-100000
    availableStates = available_states(matrix,1)
    for allStates in availableStates:
        v = max(v,min_value(allStates,level-1))
    return v
    
def min_value(matrix,level):
    if terminal_state(matrix)==1 or level==0 or level==-1:
        return utility(matrix)
    v=100000
    availableStates = available_states(matrix,2)
    for allStates in availableStates:   
        v = min(v,max_value(allStates,level-1))
    return v
    
def decision_max(matrix,level):
    availableStates = available_states(matrix,1)
    resultState = availableStates[0]
    resultValue = utility(resultState)
    for allStates in availableStates:
        value=min_value(allStates,level)
        if value > resultValue:
            resultValue = value
            resultState = allStates
        
    return resultState

def decision_min(matrix,level):
    availableStates = available_states(matrix,2)
    resultState = availableStates[0]
    resultValue = utility(resultState)
    for allStates in availableStates:
        value=max_value(allStates,level)
        if value<resultValue:
            resultValue = value
            resultState = allStates
        
    return resultState

#-------------------------------------- End of minimax ----------------------------------
        
#difficulty playable in good time: i=1-2 level 5
def game_botVbot(matrix): 
    level=4
    i=0
    while 1:
        if i>=2:    #after 2 turns i increase the depth of tree
            level=5
        if i==3:    #comment to reduce difficulty
            level=20
        if i>=4:    #comment to reduce difficulty
            level=40
        #player 1 turn
        availableChoice = available_spaces(matrix)
        if len(availableChoice) == 0:
            print("game draw")
            sys.exit()
        
        if i==0:
            print("player1 plays")
            value = randint(0, 10)
            matrix[int(value/4)][value%4]=1
            printBoard(matrix)
        else:            
            print("player1 plays")
            matrix = decision_max(matrix,level)
            printBoard(matrix)
            if winCheck(matrix) != 0:
                result(matrix)
        
        #player 2 turn
        availableChoice = available_spaces(matrix)
        if len(availableChoice) == 0:
            print("game draw")
            sys.exit()
        
        print("player2 plays")
        matrix = decision_min(matrix,level)
        printBoard(matrix)
        if winCheck(matrix) != 0:
            result(matrix)
            
        i=i+1
            
from random import randint
def game_botVhuman(matrix): 
    level=4
    i=0
    while 1:
        if i>=2:    #after 2 turns i increase the depth of tree
            level=5
        
        if i==3:    #comment to reduce difficulty
            level=20
            
        if i>=4:    #comment to reduce difficulty
            level=40
        #player 1 turn
        
        availableChoice = available_spaces(matrix)
        if len(availableChoice) == 0:
            print("game draw")
            sys.exit()
        if i==0:
            print("player1 plays")
            value = randint(0, 10)
            matrix[int(value/4)][value%4]=1
            printBoard(matrix)
        else:            
            print("player1 plays")
            matrix = decision_max(matrix,level)
            printBoard(matrix)
            if winCheck(matrix) != 0:
                result(matrix)
        
        #player 2 turn
        availableChoice = available_spaces(matrix)
        if len(availableChoice) == 0:
            print("game draw")
            sys.exit()
        
        a=int(input("Play our turn player2 (select 0-15) :"))
        matrix[int(a/4)][a%4]=2
        printBoard(matrix)
        if winCheck(matrix) != 0:
            result(matrix)
         
        i=i+1

  

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx alpha Beta Pruning Code xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  
def prune_max_value(matrix,alpha,beta,level):
    if terminal_state(matrix)==1 or level==0 or level==-1:
        return utility(matrix)
    v=-100000
    availableStates = available_states(matrix,1)
    for allStates in availableStates:
        v = max(v,prune_min_value(allStates,alpha,beta,level-1))
        if v>=beta:
            return v
        alpha=max(alpha,v)
    return v
    
def prune_min_value(matrix,alpha,beta,level):
    if terminal_state(matrix)==1 or level==0 or level==-1:
        return utility(matrix)
    v=100000
    availableStates = available_states(matrix,2)
    for allStates in availableStates:   
        v = min(v,prune_max_value(allStates,alpha,beta,level-1))
        if v<=alpha:
            return v
        beta=min(beta,v)
    return v

def prune_decision_max(matrix,level):
    availableStates = available_states(matrix,1)
    resultState = availableStates[0]
    resultValue = utility(resultState)
    for allStates in availableStates:
        value=prune_min_value(allStates,-100000,100000,level)
        if value > resultValue:
            resultValue = value
            resultState = allStates
        
    return resultState

def prune_decision_min(matrix,level):
    availableStates = available_states(matrix,2)
    resultState = availableStates[0]
    resultValue = utility(resultState)
    for allStates in availableStates:
        value=prune_max_value(allStates,-100000,100000,level)
        if value<resultValue:
            resultValue = value
            resultState = allStates
        
    return resultState

#------------------------- End of Alpha beta Pruning code ---------------------------------
    
#difficulty playable in good time: i=1-2 level 5
def prune_game_botVbot(matrix): 
    level=4
    i=0
    while 1:
        if i>=2:    #after 2 turns i increase the depth of tree
            level=5
        if i==3:    #comment to reduce difficulty
            level=20
        if i>=4:    #comment to reduce difficulty
            level=40
        #player 1 turn
        availableChoice = available_spaces(matrix)
        if len(availableChoice) == 0:
            print("game draw")
            sys.exit()
        
        if i==0:
            print("player1 plays")
            value = randint(0, 10)
            matrix[int(value/4)][value%4]=1
            printBoard(matrix)
        else:            
            print("player1 plays")
            matrix = prune_decision_max(matrix,level)
            printBoard(matrix)
            if winCheck(matrix) != 0:
                result(matrix)
        
        #player 2 turn
        availableChoice = available_spaces(matrix)
        if len(availableChoice) == 0:
            print("game draw")
            sys.exit()
        
        print("player2 plays")
        matrix = prune_decision_min(matrix,level)
        printBoard(matrix)
        if winCheck(matrix) != 0:
            result(matrix)
            
        i=i+1
            
        
def prune_game_botVhuman(matrix): 
    level=4
    i=0
    while 1:
        if i>=2:    #after 2 turns i increase the depth of tree
            level=5
        
        if i==3:    #comment to reduce difficulty
            level=10
            
        if i>=4:    #comment to reduce difficulty
            level=40
        #player 1 turn
        
        availableChoice = available_spaces(matrix)
        if len(availableChoice) == 0:
            print("game draw")
            sys.exit()
        if i==0:
            print("player1 plays")
            value = randint(0, 10)
            matrix[int(value/4)][value%4]=1
            printBoard(matrix)
        else:            
            print("player1 plays")
            matrix = prune_decision_max(matrix,level)
            printBoard(matrix)
            if winCheck(matrix) != 0:
                result(matrix)
        
        #player 2 turn
        availableChoice = available_spaces(matrix)
        if len(availableChoice) == 0:
            print("game draw")
            sys.exit()
        
        a=int(input("Play our turn player2 (select 0-15) :"))
        matrix[int(a/4)][a%4]=2
        printBoard(matrix)
        if winCheck(matrix) != 0:
            result(matrix)
         
        i=i+1
        

#xxxxxxxxxxxxxxxxxxxxxxxxxx Use Heuristics and time limited decision making xxxxxxxxxxxxxxxxxxxxxxx

def heuristic_decision_max(matrix,d):
    availableStates = available_states(matrix,1)
    resultState = availableStates[0]
    resultValue = utility(resultState)
    for allStates in availableStates:
        value=min_value(allStates,d)
        if value > resultValue:
            resultValue = value
            resultState = allStates
        
    return resultState

def heuristic_decision_min(matrix,d):
    availableStates = available_states(matrix,2)
    resultState = availableStates[0]
    resultValue = utility(resultState)
    for allStates in availableStates:
        value=max_value(allStates,d)
        if value<resultValue:
            resultValue = value
            resultState = allStates
        
    return resultState

    
#difficulty playable in good time: i=1-2 level 5
def heuristic_game_botVbot(matrix): 
    level=4
    i=0
    while 1:
        if i>=2:    #after 2 turns i increase the depth of tree
            level=1
        if i==3:    #comment to reduce difficulty
            level=5
        if i>=4:    #comment to reduce difficulty
            level=40
        #player 1 turn
        availableChoice = available_spaces(matrix)
        if len(availableChoice) == 0:
            print("game draw")
            sys.exit()
        
        if i==0:
            print("player1 plays")
            value = randint(0, 10)
            matrix[int(value/4)][value%4]=1
            printBoard(matrix)
        else:            
            print("player1 plays")
            matrix = heuristic_decision_max(matrix,level)
            printBoard(matrix)
            if winCheck(matrix) != 0:
                result(matrix)
        
        #player 2 turn
        availableChoice = available_spaces(matrix)
        if len(availableChoice) == 0:
            print("game draw")
            sys.exit()
        
        print("player2 plays")
        matrix = heuristic_decision_min(matrix,level)
        printBoard(matrix)
        if winCheck(matrix) != 0:
            result(matrix)
            
        i=i+1
            
        
def heuristic_game_botVhuman(matrix): 
    level=4
    i=0
    while 1:
        if i>=2:    #after 2 turns i increase the depth of tree
            level=1
        
        if i==3:    #comment to reduce difficulty
            level=10
            
        if i>=4:    #comment to reduce difficulty
            level=40
        #player 1 turn
        
        availableChoice = available_spaces(matrix)
        if len(availableChoice) == 0:
            print("game draw")
            sys.exit()
        if i==0:
            print("player1 plays")
            value = randint(0, 10)
            matrix[int(value/4)][value%4]=1
            printBoard(matrix)
        else:            
            print("player1 plays")
            matrix = heuristic_decision_max(matrix,level)
            printBoard(matrix)
            if winCheck(matrix) != 0:
                result(matrix)
        
        #player 2 turn
        availableChoice = available_spaces(matrix)
        if len(availableChoice) == 0:
            print("game draw")
            sys.exit()
        
        a=int(input("Play our turn player2 (select 0-15) :"))
        matrix[int(a/4)][a%4]=2
        printBoard(matrix)
        if winCheck(matrix) != 0:
            result(matrix)
         
        i=i+1
        

#xxxxxxxxxxxxxxxxxxxxxxxxxx Use Heuristics and time limited decision making xxxxxxxxxxxxxxxxxxxxxxx
heuristic_game_botVhuman(matrix)