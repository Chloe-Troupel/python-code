# -*- coding: utf-8 -*-
"""
@author: Chloe TROUPEL
"""

from tkinter import *
from tkinter import messagebox              #pop-ups
from random import *                        #to have a random number


class EnemisShips: 
    def __init__(self, name, posx, posy, ImgShip,shooter, life,speed, points, sens=1,tour=0):
        self.name=name    
        self.posx=posx                      #spatial coordinates X
        self.posy=posy                      #spatial coordinates Y
        self.Img=ImgShip                    #canvas
        self.shooter=shooter                #state to end the game  
        self.life=life 
        self.speed=speed
        self.points = points                #points given to the player if he killed the ship
        self.sens=sens
        self.tour=tour

class ProjectilePlayer: #class to handle the players's projectiles
    def __init__(self,name,speed,posx,posy,ImgProjectile):
        self.name=name
        self.speed=speed
        self.posx=posx
        self.posy=posy
        self.Img=ImgProjectile
        
class ProjectileEnnemis:
    def __init__(self,name,speed,posx,posy,ImgProjectile): #class to handle the ennemis's projectiles
        self.name=name
        self.speed=speed
        self.posx=posx
        self.posy=posy
        self.Img=ImgProjectile   
        
class Bloc: #class to handle blocs to protect the player and the life points
    def __init__(self,name,life,posx,posy,ImgBloc):
        self.name=name
        self.life=life
        self.posx=posx
        self.posy=posy
        self.ImgBloc=ImgBloc
        
        
def CHEATvie(a = 0): #the right shift allows to add life
    global Life
    Life += 1
    
def CHEATstop(a = 0):                       #the left shift allows to stop aliens and their shoots
    #WARNING : the game can't be finished when the game is freeze
    global FREEZE 
    if FREEZE == False:                     #freeze or not when shift is pushed
        FREEZE = True
    else:
        FREEZE = False
        
def beginning(): #initialization
    global isRunning, BNewGame, xPlayer, Iship, Player, Beginning, ShipBonus, listAlien, ListShoot, ListShootEnnemis, IAlienA, IAlienB, IAlienC, IBloc, ListBlocs #global variables 
    Beginning += 1 
    BNewGame.config(state="disabled")       #while a game is on, the button to play again is disabled
    isRunning = True                        #a timerest is on to keep from refresh too often
    xPlayer=350                             #abscissa of the ship at t0
    Iship = PhotoImage(file = 'img/vaisseaugimp.gif') #picture of the player
    Player = Can.create_image(xPlayer, 650, image = Iship) 
    listAlien = []                          #lists with objects which can change with time
    ListShoot = []
    ListShootEnnemis=[]
    ListBlocs=[]
    ShipBonus=[0,]
    IAlienA = PhotoImage(file = 'img/aliens3.gif') #import pictures of aliens
    IAlienB = PhotoImage(file = 'img/aliens2.gif')
    IAlienC = PhotoImage(file = 'img/aliens1.gif')
    IBloc=PhotoImage(file= 'img/Bloc1.gif')
    for x in range(20,501, 80):             #we create the 3 ranks of aliens, each rank has a different picture and attributes. The 2nd rank has more point of life and the last can shoot
        listAlien.append(EnemisShips(len(listAlien)+1,x,100,Can.create_image(x,100, anchor = NW, image = IAlienA),1, AlLife, AlSpeed, 25))
    for x in range(20,501, 80):
        listAlien.append(EnemisShips(len(listAlien)+1,x,200,Can.create_image(x,200, anchor = NW, image = IAlienB),0, AlLife+1, AlSpeed, 15))
    for x in range(20,501, 80):
        listAlien.append(EnemisShips(len(listAlien)+1,x,300,Can.create_image(x,300, anchor = NW, image = IAlienC),0, AlLife, AlSpeed, 10))
    messagebox.showinfo("Space Invader", "Level "+str(Level)+"\nYou have "+str(Life)+" lifes left." "\nGood luck !") #pop-up at the begginnig  
    for x in range(100,501,350):            #generation of blocs to protect
        ListBlocs.append(Bloc((len(ListBlocs)+1),10,x,500,Can.create_image(x,500, anchor = NW, image = IBloc)))
    if Beginning == 1:                      #we refresh if there isn't another instance already launched
        Update()
        
def dplace6(beg, end, pas): #move progressive during the interlude of the last level
    if beg != end:                          #function is called every 10ms while the ship is not on the targeted place
        Can.coords(Player,xPlayer,beg+pas)
        Fenetre.after(10,dplace6, beg+pas, end, pas)
    
def LEVEL6():
    global BNewGame, xPlayer, isRunning, Iship, Player,listAlien, ListShoot, ListShootEnnemis, IAlien #variables globales nescessaires tout au long du programme
    BNewGame.config(state="disabled")       #while a game is on, the button to play again is disabled
    isRunning = True                        #a timerest is on to keep from refresh too often
    xPlayer=350                             #abscissa of the ship at t0
    Iship = PhotoImage(file = 'img/vaisseaugimp.gif') #picture of the player
    Player = Can.create_image(xPlayer, 650, image = Iship) 
    listAlien = []                          #lists with objects which can change with time
    ListShoot = []
    ListShootEnnemis=[]
    dplace6(650, 500, -5)                   #ship move forward a little
    messagebox.showinfo("Player", "Is...\nit...\nthe end...?") #dialogue
    messagebox.showinfo("?", "HAHAHA")
    IAlien = PhotoImage(file= 'img/aliensBOSS.gif') #ennemi's ship appears
    listAlien.append(EnemisShips(len(listAlien)+1,320,100,Can.create_image(300,100, anchor = NW, image = IAlien),1, 20, 20, 500))
    messagebox.showinfo("LIMANE", "Are you pythonning ?")
    dplace6(500,650,10)                     #the ship go back to its place
    messagebox.showinfo("Player", "LIMANE, NOOOOOOOOO")
        
def Bonus()   : #to handle the bonus ennemis
    global listAlien, ListShoot, Score, ShipBonus, IBonus
    if ShipBonus!=[]:                       #test to see if the ennemis ship bonus has been destroyed
        if ShipBonus[0]==0:                 #test to see if the ennemis ship bonus hasn't been created
            if len(listAlien)<=14:          #if hasn't been created and there is less than 14 lifes we create it
                IBonus=PhotoImage(file= 'img/aliensBONUS.gif')
                ShipBonus.append(EnemisShips("bonus",540,10 ,  Can.create_image(700-160,10, anchor = NW, image = IBonus),1, AlLife, 2*AlSpeed, 150))               
                ShipBonus[0]=[1]            #we indicate if the ship has been created for this level to avoid that it apperas again
        elif len(ShipBonus)==2:             #if the alien's ship is on the field, we move it
            ShipBonus[1].posx-=ShipBonus[1].speed #we write down its position
            Can.move(ShipBonus[1].Img, -ShipBonus[1].speed ,0) # the bonus moves from right to left with a speed of 20px
            for i in ListShoot:             #we test the colision with the player's shooting
                if len(ShipBonus)>1:        #we test if the ship has been destroyed by a previous shoot
                    if i.posx<ShipBonus[1].posx + 170  and i.posx>ShipBonus[1].posx -10 and i.posy<80: #the bonus is touched
                        Score += ShipBonus[1].points
                        LScore.config(text = "score : " + str(Score)) #update of the score
                        Can.delete(Fenetre,i.Img) #we delete the shooting picture
                        Can.delete(Fenetre,ShipBonus[1].Img)  #we delete the bonus picture
                        ShipBonus=[]        #we delete the bonus
                        ListShoot.remove(i) #we delete the shooting from the list
                    else:                   #if the bonus touches the edge of the screen, the player failed, he doesn't win points and the bonus disappears
                        ShipBonus[1].posx-=0
                        if ShipBonus[1].posx<0:
                            Can.delete(Fenetre,ShipBonus[1].Img)
                            ShipBonus=[]
        
def LeftPlayer(a=0): #we move the player to the left
    global xPlayer
    global Player
    if xPlayer >10:                         #the player has not reach the left edge
        xPlayer-=20                         #we write down the value
        Can.coords(Player,xPlayer,650)      #we move the player(we could have used Can.move)
        
def RightPlayer(a=0): #we move the player to the right
    global xPlayer
    global Player
    if xPlayer <690:                        #the player has not reach the right edge
        xPlayer+=20
        Can.coords(Player,xPlayer,650)      
    
def ShootPlayer(a=0): #we shoot
    global ListShoot
    if len(ListShoot)<5:                    #no more than 4 shootings at the same time in order for the game not to be too simple
        ImgProjectile=Can.create_rectangle(xPlayer,660,xPlayer+10,650, fill="orange") #the projectile is an orange square
        ListShoot.append(ProjectilePlayer(len(ListShoot),150,xPlayer+42,650,ImgProjectile)) #we put it in the list which will be refreshed
 
def ShootAliens(): #Aliens shoot
    global ListShootEnnemis
    ListShooter=[]
    for i in listAlien:                     #we set aside aliens capable of shooting
        if i.shooter==1:
            ListShooter.append(i)
    for i in ListShooter:                   #every alien has a probability to shoot which rise every time an alien dies
        if Level == FinalLevel:             #the boss shoots faster and in green
            a=randint(1,2)
            if a==2*len(listAlien):
                ImgProjectile=Can.create_rectangle(i.posx+100,i.posy+100,i.posx+110,i.posy+110, fill="green")#we create the projectile and we put it in the refreshed list
                ListShootEnnemis.append(ProjectileEnnemis(len(ListShootEnnemis),50,i.posx+100,i.posy+100,ImgProjectile))   
        else:
            a=randint(1,2*len(listAlien)+1) #We take a number between 1 and the number of ships
            if a==2*len(listAlien):         #if it is the number of ships, we shoot
                ImgProjectile=Can.create_rectangle(i.posx,i.posy,i.posx+10,i.posy+10, fill="red") #we create the projectile and we put it in the refreshed list
                ListShootEnnemis.append(ProjectileEnnemis(len(ListShootEnnemis),20,i.posx+15,i.posy+15,ImgProjectile))   
    
def MoveShootEnnemis(): #movements of ennemi's shooting
    global ListShootEnnemis, Life, ListBlocs, IBloc2, IBloc3
    for i in ListShootEnnemis: 
        if i.posy>=500 and i.posy<=560 :    #zone where the projectile can touch a bloc
            for k in ListBlocs:             #we test the collision with each bloc
                if i.posx> k.posx and i.posx< k.posx +160:
                    k.life-=1               #if the bloc is touched it lose a life point
                    Can.delete(Fenetre,i.Img)#we modify its picture
                    if i in ListShootEnnemis:
                        ListShootEnnemis.remove(i)
                        if k.life<1:        #bloc is destroyed if it has no more life
                            Can.delete(Fenetre,k.ImgBloc)
                            ListBlocs.remove(k)
                        elif k.life<4:      #updated (almost destroyed)
                            Can.delete(Fenetre,k.ImgBloc)
                            k.ImgBloc = Can.create_image(k.posx,500, anchor = NW, image = IBloc3)
                        elif k.life<7:      #updated (broken)
                            Can.delete(Fenetre,k.ImgBloc)
                            k.ImgBloc = Can.create_image(k.posx,500, anchor = NW, image = IBloc2)               
        elif i.posy>=650 and i.posx> xPlayer and i.posx+10<=xPlayer+50: #collision with the player
            Life-=1                         #we lose a life
            Can.delete(Fenetre,i.Img)       #we delete the projectile
            ListShootEnnemis.remove(i)
            if Life<0:                      
                End(i)                      #end of the game
        elif i.posy> 680:                   #the projectile missed the player, we delete it when it reached the edges
            Can.delete(Fenetre,i.Img)
            ListShootEnnemis.remove(i)
        i.posy+=20                          #we move the projectile if nothing happened
        Can.move(i.Img,0,20)
    
def MoveShoot(): #movements of player's shooting
    global ListShoot, listAlien, Score
    for i in ListShoot:
        for j in listAlien:                 #test collision with aliens
            if Level == FinalLevel:
                if i.posy<j.posy+150 and i.posy>j.posy and i.posx<j.posx+250 and i.posx>j.posx:
                    j.life -= 1             #they lose a life if there is a collision
                    if i in ListShoot:      #we delete the projectile, we test if it hasn't been deleted yet to avoid a bug
                        ListShoot.remove(i)
                    Can.delete(Fenetre,i.Img)
                    if j.life < 1:          #if they die we delete them
                        Score += j.points
                        LScore.config(text = "score : " + str(Score))
                        Can.delete(Fenetre,j.Img)
                        listAlien.remove(j)
            elif i.posy<j.posy+50 and i.posy>j.posy and i.posx<j.posx+110 and i.posx>j.posx:
                j.life -= 1                 #they lose a life if there is a collision
                if i in ListShoot:          #we delete the projectile, we test if it hasn't been deleted yet to avoid a bug
                    ListShoot.remove(i)
                Can.delete(Fenetre,i.Img)
                if j.life < 1:              #if they die we delete them and we add their points to the player's score
                    Score += j.points
                    Can.delete(Fenetre,j.Img)
                    listAlien.remove(j)
                    for n in listAlien:     #the speed increase for each death of aliens
                        n.speed += 0.3
        if i.posy<=0:                       #the projectile leaves, we delete it
            ListShoot.remove(i)
        else:                               #if not, he moves forward
            i.posy-=20            
            Can.move(i.Img, 0, -20)
    
def Move():#movements of aliens
    global listAlien
    tueur=None                              #to handle collision with teh player
    for i in listAlien:             
        if i.sens==1:
            if (Level == FinalLevel and i.posx>550) or i.posx>650 : 
                for x in listAlien:         #alien reached the edge he go down and turn around
                    x.posy += 50
                    x.sens=-1
            else: 
                Can.coords(i.Img,i.posx+i.speed,i.posy)
                i.posx=i.posx+i.speed
        else:
            if i.posx>0 :                   #alien move to the left
                Can.coords(i.Img,i.posx-i.speed,i.posy)
                i.posx=i.posx-i.speed                
            else:
                for x in listAlien:         #at the edges of the screen the alien go down and turn around
                    x.posy += 50
                    x.sens=1
        if i.posy>630:                      #zone of collision possible with the player
            tueur = i
    if len(listAlien)<1 or tueur != None:   #if there are no more aliens and if the alien reached the players it is the end of the game
        End(tueur)
    else:
        Bonus()                             #bonus is always called while the player is still alive but it is not launched
        
def End(i):
    global listAlien, Level, Wallpaper, AlLife, AlSpeed, Life, Score
    highscore()                             #we write down the highscore
    if i == None and Level+1 == FinalLevel: #Level 6 is the final level
        Level += 1
        clean()
        LEVEL6()                            #We called this function which is almost the same of beginning()
    else:
        if i != None:                       #the alien has touched the player it is the defeat
            messagebox.showinfo("You lost","Sorry !\nYou lost with a score of " +str(Score)) #pop-up of defeat
            Life = 5                        #we on reset the game and the variables
            Level = 1
            Score = 0
            Wallpaper = PhotoImage(file = "img/fond1.gif") #we put back the first wallpaper
            Can.create_image(0, 0, anchor = NW, image = Wallpaper)
            LLevel.config(text = "Levels : " + str(Level))
            AlLife = 1
            AlSpeed = 3
            clean()
        elif len(listAlien)<=1:             #all aliens are dead (bonus doesn't count)
            messagebox.showinfo("You won !!","They are all dead !")
            Score += 50*Level               #We add to the score depending on the level
            Life += 1                       #We have an additional life for each levels
            Level += 1
            if Level == 2:                  #We adapt the wallpaper depending on the level 
                #To adjust difficulty the speed or the life of aliens inncrease
                Wallpaper = PhotoImage(file = "img/fond2.gif")
                AlSpeed += 1
            elif Level == 3:
                Wallpaper = PhotoImage(file = "img/fond3.gif")
                AlLife += 1
            elif Level == 4:
                Wallpaper = PhotoImage(file = "img/fond4.gif")
                AlSpeed += 1
            elif Level == 5:
                Wallpaper = PhotoImage(file = "img/fond5.gif")
                AlSpeed += 1
                AlLife += 1
            elif Level == 7: 
                Score += Life*100           #we add the lives left to the score
                AlLife += 1
                AlSpeed+= 2
                messagebox.showinfo("You won !!","Congratulations !\nYou won with a score of " + str(Score))
            elif Level > 7:                 #Player won, but can keep on playing
                AlSpeed += 2
                AlLife += 1
                messagebox.showinfo("You won !!","still in the race ?\nCHEATER") #We know the buttons shift and their usefulness
            Can.create_image(0, 0, anchor = NW, image = Wallpaper)
            clean()                         #cleanning...
        beginning()                         #... we start again !

def highscore(): #to keep the scores and display the best
    global Score
    fichier=open("highscore.txt","a+")      #open the file or create it if not created
    liste=[]
    for i in fichier:
        liste.append(i.strip())             #we add the scores in a list
    Score=int(Score)
    liste.append(Score)
    fichier.close()                         #close in reading
    fichier=open("highscore.txt","w") 
    for i in liste:
        fichier.write(str(i))               #writing of the new score
        fichier.write("\n")                 #to put scores in column
    fichier.close()                         #close in writing
    l2=[]
    for i in liste:
        l2.append(int(i))
    if len(l2)==0:
        a=0
    else :
        a=max(l2)
    LHighScore.config(text = "HighScore : "+str(a))
        
def clean(a = 0): #function to clean the canvas and used lists, it is called between levels and at the defeat
    global listAlien, BNewGame, isRunning, ListShoot, ListShootEnnemis
    for i in listAlien:
        Can.delete(Fenetre,i.Img)
    for i in ListShoot:
        Can.delete(Fenetre,i.Img)
    for i in ListShootEnnemis:
        Can.delete(Fenetre,i.Img)
    listAlien=[]
    ListShoot=[]
    ListShootEnnemis=[] 
    isRunning = False
    BNewGame.config(state="active")

def Update():
    MoveShoot()
    if FREEZE == False:
        Move()
        ShootAliens()
        MoveShootEnnemis()
    LScore.config(text = "score : " + str(Score))
    LLevel.config(text = "Level : " + str(Level))
    LLife.config(text="lifes : "+ str(Life))
    if isRunning:
        Fenetre.after(50,Update)



Fenetre = Tk()
isRunning=True
Fenetre.title("SPACE INVADER v1.0_CL")
IBloc3=PhotoImage(file= 'img/Bloc3.gif')
IBloc2=PhotoImage(file= 'img/Bloc2.gif')

Score = 0
Beginning = 0
Level = 1
Life = 5
AlLife = 1
AlSpeed = 3
FREEZE = False
FinalLevel = 6                              #the final level is the 6th but it is useful to change it for tests


Haut = Frame(Fenetre)
Haut.pack(side = TOP, padx = 5, pady = 5)

Wallpaper = PhotoImage(file = "img/fond1.gif")
Can = Canvas(Fenetre, width = 700, height = 700)
Can.pack(side = LEFT)
Can.create_image(0, 0, anchor = NW, image = Wallpaper)

Right = Frame(Fenetre)
Right.pack(side = RIGHT, padx = 10, pady = 10)

LScore = Label(Haut,text = "score : " + str(Score))
LScore.pack(side = LEFT, padx = 5)
LLevel = Label(Haut,text = "Level : " + str(Level))
LLevel.pack(side = LEFT, padx = 200)
LLife = Label(Haut,text = "lifes : " + str(Life))
LLife.pack(side = LEFT, padx = 5)


BNewGame = Button(Right, text = "New Game", command = beginning, activebackground="blue")
BNewGame.pack(pady = 30)
LHighScore=Label(Haut,text = "Highscore : 0" + str(Score))
LHighScore.pack(padx = 5)  
highscore()
BQuit = Button(Right, text = "Exit", command = Fenetre.destroy, activebackground="red")
BQuit.pack(pady = 30)


Fenetre.bind("<Left>", LeftPlayer)
Fenetre.bind("<Right>", RightPlayer)
Fenetre.bind("<space>",ShootPlayer)
Fenetre.bind("<Up>",ShootPlayer)
Fenetre.bind("<Shift_L>",CHEATstop)
Fenetre.bind("<Shift_R>",CHEATvie)
Fenetre.bind("<Escape>",clean)




Fenetre.mainloop()
