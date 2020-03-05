# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 07:57:32 2018

@author: chloe.troupel
purpose: Hangman game
"""

import random
file="Dico.txt"

#Function which extracts every words of Dico.txt and put it in a list
#Input: file.txt
#Outputs: list of words

def ListWords(file):
    f = open(file,"r")
    listWords=f.readlines()
    
    for i in range(len(listWords)):
        listWords[i]=listWords[i].rstrip('\n')
    f.close() 
    return listWords
    
#Function which chose a random word in Dico.txt
#Input: file.txt
#Outputs: a random word

def ChoixRandom (file):
    num=random.randrange(0,len(ListWords(file)))
    word=ListWords(file)[num]
    return word
    
#Function which display the letters found and the first letter of the word otherwise display a _
#Input: a list of character and the word to find
#Output: the number of character found and the word with the characters found
    
def Affich(listChar,word):
   chgt=0
   wordi=word[0]
   
   for i in range(1,len(word)):
        if word[i] in listChar:
            chgt+=1
            wordi+=str(word[i])
        else:
            wordi+="_"
   return wordi,chgt

#Function which chose a letter to test and verify that the letter has not been already played
#Input: a list of letters
#Output: a letter

def Choixlettre(listChar):
    l=input("Which letter you want to test ? ")
    l=l.lower()
    
    while l in listChar:
        l=input("You have already chosen this letter. Which other letter you want to test ? ")
    return l
    
#Function which create a file with name of the player and his score
#Input: score and the name of the player
#Output: a list with the file's content    
    
def ComptScore(score, name):
    f = open("FichierScore.txt", "r")
    LScore = f.readlines()
    
    for i in range(len(LScore)):
        if int(LScore[i][0])<=score:
            LScore=LScore[0:i]+[str(score)+' '+str(name)+'\n']+LScore[i:len(LScore)]
            return LScore
    LScore=LScore[:]+[str(score)+' '+str(name)+'\n']
    f.close
    return LScore
    
#Function which modify the file of scores
#Input: score and the name of the player 
        
def fComptScore(score,name):
    LScore = ComptScore(score,name)
    f = open("FichierScore.txt", "w")
    for i in LScore:
        f.write(i)
    f.close   
    
#Function which allow to play
#Input: file.txt
#Output: number of errors if she won and if she lost return -1

def Game(file):
   word = ChoixRandom(file)
   Llettres = []
   Lchgt = []
   wordi,chgt = Affich(Llettres,word)
   Lchgt.append(chgt)
   print (wordi)
   
   i=0
   while i<8:   
        Llettres.append(Choixlettre(Llettres))
        wordi,chgt = Affich(Llettres,word)
        Lchgt.append(chgt)
        print (wordi)
        print("you have ",7-i,"charater left")
        if Lchgt[-1]==Lchgt[-2]:
            i+=1
        if wordi == word:
            return i
   return 10
   
   
def Replay():
    name = input("What is your name ? ")
    score = Game(file)
    if score != 10:
        print ("You won ! Congratulation !")
        fComptScore(score, name)
        print("You did",score,"errors")
        replay = input("Do you want to replay ? ")
        replay.lower()
        if replay == "yes":
            Replay()
    else:
        print ("You lost. Try again !")
        fComptScore(score, name)
        replay = input("Do you want to replay ? ")
        replay.lower()
        if replay == "yes":
            Replay()
        
#Body of the program
        
Replay()
