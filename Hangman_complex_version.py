# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 14:00:47 2017
Julien Vedun
Improved version of the hangman game.
"""

from tkinter import *
from math import sqrt,pi
from random import randint
from tkinter.messagebox import *


class ZoneAffichage(Canvas):
    """
        This class inherits of the class Canvas and creates the window where all the elements are displayed.
        """
    def __init__(self,parent, w, h, c, n):
        Canvas.__init__(self, width = w, height = h, bg = c)
        self.__numbermoves = n #number of available moves.
    def afficher(self):
        """
        Dispayed the different texts and shapes of the window.
        """
        # Images that represents the hangman.
        self.delete(ALL)
        # Depending on the number of moves available, displays the image of the hangman.
        nameImage = 'hangman{}.gif'.format(8-self.__numbermoves)
        self.photo = PhotoImage(file=nameImage)
        self.create_image(0,0, anchor=NW, image=self.photo)
        self.config(height=self.photo.height(),width=self.photo.width())
    def getnumbermovesavailable(self):
        """
        Return the number of moves available.
        """
        return self.__numbermoves
    def setnumbermovesavailable(self,n):
        """
        Set the number of moves available and give it the value n.
        """
        self.__numbermoves = n
        
class Player:
    """
    This class allows to create the profil of a player named "name" and with the score "scores".
    """
    def __init__(self,name,scores):
        self.__name = name
        self.__scores = scores
    def get_name(self):
        """
        Return the name of the player.
        """
        return self.__name
    def set_name(self,name):
        """
        CHange the name of the player with the given name "name".
        """
        self.__name = name
    def get_score(self):
        """
        Return the player's score.
        """
        return self.__scores
    def set_score(self,score):
        """
        Change the score of the player with the given score "score".
        """
        self.__scores = score
    def affiche_players(self):
        """
        Return a string including the name and the score of the player.s
        """
        texte = str(self.get_name()) + ' '*5 + str(self.get_score()) + '\n'
        return texte
    
class FenPrincipale(Tk,Player):
    """
    This class inherits of the class Tk and Player,
    implements the logic of the game and modifies the elements of the window.
    """
    def __init__(self):
        Tk.__init__(self)

        f2 = Frame(self)
        f2.pack(side = TOP,padx = 5,pady = 5)

        # Create a text area for the rules of the games and a few explanations.
        self.__instructions = Label(self)
        self.__instructions.pack(side = LEFT)
        self.__instructions.config(text = 
        'Welcome dear user.'+
        '\n\nHere are the rules of the hangman game : '+
        '\nYour goal is to find out the hidden word'+
        '\nin the bottom of the window, before the man '+
        '\nis completely hanged. You can, if you want, give up'+
        '\nthe game by clicking on the button "Give up".'+
        '\nIf you are new around here, you can sign up'+
        '\nby clicking the button "Add a new player".'+
        '\nIf you are already registered, you can use again'+
        '\nyour profil by clicking on the button "Choose a player".'+
        '\nYou can whenever you wnt check your score and'+
        '\nthe scores of the other players by clicking on the button' +
        '\n"Players and scores". Each winning game gives you '+
        '\n5 points plus the number of moves left behind.'+
        '\n\n Good luck and have fun ! ')

        self.__zoneAffichage = ZoneAffichage(self,480,320,'white',7)
        self.title('Hangman game')
        self.__zoneAffichage.pack(padx=5, pady=5)

        f1 = Frame(self)
        f1.pack(side=TOP, padx=5, pady=5)

        # Add the different buttons
        self.__boutonNew = Button(f2, text ='New game', width=15, command = self.nouvellePartie).grid(row = 0, column = 0)
        self.__boutonQuitter  =  Button(f2,  text  ='Exit',  command  = self.destroy).grid(row = 0, column = 1)
        self.__lmot = Label(self)
        self.__mot = ''
        self.__motaff = ''
        self.__lmot.pack(side=TOP)
        self.__lmot.config(text='Welcome, you can play by clicking on the button New Game')
        self.__boutons = []
        self.__boutonabandon = Button(f2,text = 'Give up',width = 30,command = self.abandon).grid(row = 0,column = 2)
        # Add the buttons to choose the letters
        for i in range(26):
            bouton = MonBoutton(self,f1,chr(ord('A')+i))
            bouton.grid(row=(i//7)+2,column = i-7*(i//7)+2)
            self.__boutons.append(bouton)
            self.__boutons[i].config(command= self.__boutons[i].cliquer, state = DISABLED)
        self.__liste_players = []
        self.__boutonplayers = Button(f2,text = 'Players and scores',width = 30,command = self.affiche_players_scores).grid(row = 0,column = 4)
        self.__boutonajoutplayer = Button(f2,text = 'Add a new player',width = 30,command = self.ajout_player).grid(row = 0,column = 5)
        self.__boutonchoixplayer = Button(f2, text = 'Choose a player',width = 30, command = self.choix_player).grid(row = 0,column = 6)
        self.__playerselectionne = 0
        self.__player = Label(self)
        self.__player.pack(side = TOP)
    def set_score(self,score):
        """
        Modify the score value of the current player with the given score.
        """
        self.__liste_players[self.__playerselectionne].set_score(score)
    def get_score(self):
        """
        Return the score of the current player and None if it doesn't exist.
        """
        if self.__playerselectionne <= len(self.__liste_players)-1:
            return self.__liste_players[self.__playerselectionne].get_score()
        return None
    def set_playerselectionne(self,name):
        """
        Search in the list of player the player with the given name and register the index in the list
        in a variable.
        """
        for i in range(len(self.__liste_players)) :
            if self.__liste_players[i].get_name() == name:
                self.__playerselectionne = i
                return
    def get_playerselectionne(self):
        """
        Return the index of the current player in the list of players.
        """
        return self.__playerselectionne
    def ajout(self,fen,name):
        """
        Add the name of the wrote by the player and close the window.
        """
        name = name.get()
        fen.destroy()
        self.__liste_players.append(Player(name,0))
    def ajout_player(self):
        """
        Allow a new player to sign up in the database.
        He become the game with a null score.
        """
        mafenetre = Tk()
        mafenetre.title('Add a player')
        label = Label(mafenetre, text = 'name : ')
        label.pack(side = LEFT, padx = 5, pady = 5)
        name = StringVar()
        texte = Entry(mafenetre, bg ='bisque', fg='maroon')# textvariable= name,
        texte.focus_set()
        texte.pack(side = LEFT, padx = 5, pady = 5) 
        bouton = Button(mafenetre, text ='OK', command = lambda: self.ajout(mafenetre,texte)).pack(side = LEFT, padx = 5, pady = 5)
    def affiche_players_scores(self):
        """
        Display the latest players and their score.
        """
        texte = 'Names:     Scores:\n'
        for elt in self.__liste_players :
            texte += elt.affiche_players()
        fenetre = Tk()
        fenetre.title('Players et scores')
        bouton = Button(fenetre,text = 'Exit',command = fenetre.destroy)
        bouton.pack(side = LEFT,padx = 5,pady = 5)
        lab=Label(fenetre, text=texte)
        lab.pack(side="left")
    def modif_player(self,player):
        """
        Modify the variable including the current player name and
        display his name on the window.
        """
        self.set_playerselectionne(player.get_name())
        self.__player.config(text = 'You are playing with : {}'.format(player.get_name()))
    def choix_player(self):
        """
        Display a window with a button for each signed up player
        and allow a player to chooose an existing profil.
        """
        fenetre = Tk()
        fenetre.title('Choose a player')
        l = len(self.__liste_players)
        for n in range(len(self.__liste_players)) :
            elt = self.__liste_players[n]
            Button(fenetre, text = '{}'.format(elt.get_name()), command = lambda elt=elt : self.modif_player(elt)).grid(row = self.__liste_players.index(elt),column = 0)
        Button(fenetre, text = 'Validate choice',command = fenetre.destroy).grid(row = l,column = 0)
    def abandon(self):
        """
        Display the word in case of given up.
        :return:
        """
        self.__lmot.config(text='The word was - {} '.format(self.__mot))
        self.finPartie()
    def finPartie(self):
        """
        End the game.
        """
        for elt in self.__boutons:
            elt.config(state=DISABLED)
    def nouvellePartie(self):
        """
        Start a new game : reboote the number of available moves,
        the window and generate a new word
        """
        self.__zoneAffichage.delete(ALL)
        for elt in self.__boutons :
            elt.config(state = NORMAL)
        mot = self.nouveauMot()
        self.__zoneAffichage.setnumbermovesavailable(7)
        self.__zoneAffichage.afficher()
        self.setmot(mot)
        self.setmotaff('*'*len(mot))
        self.__lmot.config(text='Word : {}'.format(self.__motaff))
    def setmot(self,word):
        """Modify the word to guess by word."""
        self.__mot = word
    def setmotaff(self,word):
        """Modify the displayed word by word."""
        self.__motaff = word
    def traitement(self,lettre):
        """
        Implement the game logic when the player press a button.
        """
        tourgagnant = 0
        if self.__zoneAffichage.getnumbermovesavailable() <= 1 : # if no more available moves : that's a defeat
            self.__lmot.config(text =' You lost, the word was : {}'.format(self.__mot))
            self.finPartie() 
        else : # if one or more moves available
            for i in range(len(self.__mot)):
                if self.__mot[i] == lettre: #if the choosen letter was on the hidden word
                    # the * of the displayed word are replaced by the letters
                    tourgagnant = 1
                    if i == len(self.__mot)-1:
                        self.setmotaff(self.__motaff[:i] + lettre)
                    elif i == 0:
                        self.setmotaff(lettre + self.__motaff[1:])
                    else :
                        self.setmotaff(self.__motaff[:i] + lettre + self.__motaff[i+1:])
                    self.__lmot.config(text='{}'.format(self.__motaff))
        if tourgagnant == 0 : # if the lettter wasn't in the hidden word
            self.__zoneAffichage.setnumbermovesavailable(self.__zoneAffichage.getnumbermovesavailable()-1)
            self.__zoneAffichage.afficher()
        if "*" not in self.__motaff: # if no more hidden letters on the word to guess, that's a win
            self.__lmot.config(text='{} - Congratulations, you have won'.format(self.__mot))
            if len(self.__liste_players) > 0:
                self.set_score(5+self.get_score()+self.__zoneAffichage.getnumbermovesavailable())
            self.finPartie()
    def chargewords(self):
        """
        Return the list of <ords after having process them.
        """
        fichier = open('words.txt','r')
        texte = fichier.read()
        fichier.close()
        liste_words = texte.strip().split() #Change the string into a list of words.
        return liste_words
    def nouveauMot(self):
        """
        Return a random word of the list.
        """
        liste_words = self.chargewords()
        return liste_words[randint(0,len(liste_words))]
   
   
class MonBoutton(Button):
    """
    This class inherits of the class Button and allows to create a button
    with text inside and to implement actions when the button is pressed.
    """
    def __init__(self,fen,f,tex):
        Button.__init__(self,master=f,text=tex)
        self.__t = tex
        self.fen = fen
        self.config(command = self.cliquer)
    def cliquer(self):
        """
        Run the game logic whenever the button is pressed.
        """
        self.config(state = DISABLED)
        self.fen.traitement(self.__t)




# Run the game
if __name__ == "__main__":
    fen = FenPrincipale()
    fen.mainloop()