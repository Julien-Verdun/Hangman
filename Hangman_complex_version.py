# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 14:00:47 2017

@author: Julienv
"""
# TD4 : Verdun Julien et Uzel Antoine
# Version améliorée
from tkinter import *
from math import sqrt,pi
from random import randint
from tkinter.messagebox import *

class ZoneAffichage(Canvas):
    def __init__(self,parent, w, h, c, n):
        Canvas.__init__(self, width = w, height = h, bg = c)
        self.__nombrecoups = n #nombre de coups restant à jouer
    def afficher(self):
        """Affiche les éléments du jeu du pendu"""
        self.delete(ALL)
        nomImage = 'pendu{}.gif'.format(8-self.__nombrecoups)
        self.photo = PhotoImage(file=nomImage)
        self.create_image(0,0, anchor=NW, image=self.photo)
        self.config(height=self.photo.height(),width=self.photo.width())
    def getNombreCoupsPossible(self):
        """Renvoie le nombre de coups restant"""
        return self.__nombrecoups
    def setNombreCoupsPossible(self,n):
        """Modifie le nombre de coups restants"""
        self.__nombrecoups = n
        
class Joueur():
    def __init__(self,nom,scores):
        self.__nom = nom
        self.__scores = scores
    def get_nom(self):
        """ Renvoie le nom du joueur"""
        return self.__nom
    def set_nom(self,nom):
        """ Modifie le nom du joueur (attribut self.__nom) par nom"""
        self.__nom = nom
    def get_score(self):
        """ Renvoie le score du joueur."""
        return self.__scores
    def set_score(self,score):
        """ Modifie le score (attribut self.__score) du joueur"""
        self.__scores = score
    def affiche_joueurs(self):
        """ Renvoie le nom et le score du joueur sous la forme d'une chaine de caractère"""
        texte = str(self.get_nom()) + ' '*5 + str(self.get_score()) + '\n'
        return texte
    
class FenPrincipale(Tk,Joueur):
    def __init__(self):
        Tk.__init__(self)
        f2 = Frame(self)
        f2.pack(side = TOP,padx = 5,pady = 5)
        self.__instructions = Label(self)
        self.__instructions.pack(side = LEFT)
        self.__instructions.config(text = 
        'Bienvenue cher utilisateur.'+
        '\n\nVoici les règles du jeu du pendu : '+
        '\nTon objectif est de découvrir le mot caché'+
        '\nen bas de l écran avant que le bonhomme ne '+
        '\nsoit pendu. Tu peux si tu le souhaites abandonner'+
        '\nla partie en cliquant sur le bouton je donne'+
        '\nma langue au chat. Tu peux t inscrire si tu es'+
        '\nun nouveau joueur en cliquant sur le bouton ajout'+
        '\njouer. Si tu étais djà inscrit tu peux réutiliser'+
        '\nton profil en cliquant sur le bouton choix joueur.'+
        '\nTu peux à tout moment consulter ton score et'+
        '\ncelui des autres joueurs en cliquant sur le bouton' +
        '\nJoueurs et scores. Chaque partie gagnée te rapporte '+
        '\n5 points plus le nombre de coups qu il te restait à jouer.'+
        '\n\n Bonne chance et amuse toi bien ! ') 
        self.__zoneAffichage = ZoneAffichage(self,480,320,'white',7)
        self.title('Jeu du Pendu')
        self.__zoneAffichage.pack(padx=5, pady=5)
        f1 = Frame(self)
        f1.pack(side=TOP, padx=5, pady=5)
        self.__boutonNew = Button(f2, text ='Nouvelle partie', width=15, command = self.nouvellePartie).grid(row = 0, column = 0)     
        self.__boutonQuitter  =  Button(f2,  text  ='Quitter',  command  = self.destroy).grid(row = 0, column = 1)
        self.__lmot = Label(self)
        self.__mot = ''
        self.__motaff = ''
        self.__lmot.pack(side=TOP)
        self.__lmot.config(text='Bienvenue, vous pouvez commencer à jouer en cliquant sur Nouvelle Partie ')
        self.__boutons = []
        self.__boutonabandon = Button(f2,text = 'Je donne ma langue au chat',width = 30,command = self.abandon).grid(row = 0,column = 2)   
        for i in range(26):
            bouton = MonBoutton(self,f1,chr(ord('A')+i))
            bouton.grid(row=(i//7)+2,column = i-7*(i//7)+2)
            self.__boutons.append(bouton)
            self.__boutons[i].config(command= self.__boutons[i].cliquer, state = DISABLED)
        self.__liste_joueurs = []
        self.__boutonjoueurs = Button(f2,text = 'Joueurs et scores',width = 30,command = self.affiche_joueurs_scores).grid(row = 0,column = 4)
        self.__boutonajoutjoueur = Button(f2,text = 'Ajout joueur',width = 30,command = self.ajout_joueur).grid(row = 0,column = 5)
        self.__boutonchoixjoueur = Button(f2, text = 'Choix joueur',width = 30, command = self.choix_joueur).grid(row = 0,column = 6)
        self.__joueurselectionne = 0
        self.__joueur = Label(self)
        self.__joueur.pack(side = TOP)
    def set_score(self,score):
        """ Modifie l'attribut contenant le score du joueur actuel et lui donne la valeur score."""
        self.__liste_joueurs[self.__joueurselectionne].set_score(score)
        #self.__score = score
    def get_score(self):
        """ Renvoie le score du joueur actuel si il y en a un, sinon renvoie None."""
        if self.__joueurselectionne <= len(self.__liste_joueurs)-1:
            return self.__liste_joueurs[self.__joueurselectionne].get_score()
        return None
    def set_joueurselectionne(self,nom):
        """ Modifie l'attribut contenant le nom du joueur actuel et lui donne la valeur nom."""
        for i in range(len(self.__liste_joueurs)) :
            if self.__liste_joueurs[i].get_nom() == nom:
                self.__joueurselectionne = i
                return
    def get_joueurselectionne(self):
        """ Renvoie le nom du joueur actuel."""
        return self.__joueurselectionne
    def ajout(self,fen,nom):
        """
        Ajoute le nom obtenu par la méthode ajout_joueur
        à la liste des joueurs        
        """
        nom = nom.get()
        fen.destroy()
        self.__liste_joueurs.append(Joueur(nom,0))
    def ajout_joueur(self):
        """
        Permet à un nouveau joueur de s'inscrire dans la base de données du jeu
        du pendu. Il débute avec un score nul bien entendu.
        """
        mafenetre = Tk()
        mafenetre.title('Ajout d un joueur')
        label = Label(mafenetre, text = 'Nom : ')
        label.pack(side = LEFT, padx = 5, pady = 5)
        nom = StringVar()
        texte = Entry(mafenetre, bg ='bisque', fg='maroon')# textvariable= nom,
        texte.focus_set()
        texte.pack(side = LEFT, padx = 5, pady = 5) 
        bouton = Button(mafenetre, text ='Valider', command = lambda: self.ajout(mafenetre,texte)).pack(side = LEFT, padx = 5, pady = 5)
    def affiche_joueurs_scores(self):
        """
        Permet d'afficher les joueurs ainsi que leur score.
        """
        texte = 'Noms:     Scores:\n'
        for elt in self.__liste_joueurs :
            texte += elt.affiche_joueurs()
        fenetre = Tk()
        fenetre.title('Joueurs et scores')
        bouton = Button(fenetre,text = 'Quitter',command = fenetre.destroy)
        bouton.pack(side = LEFT,padx = 5,pady = 5)
        lab=Label(fenetre, text=texte)
        lab.pack(side="left")
    def modif_joueur(self,joueur):
        """Modifie l'attribut contenant le nom du joueur actuel et affiche le nom du joueur actuel sur l'écran de jeu."""
        self.set_joueurselectionne(joueur.get_nom())
        self.__joueur.config(text = 'Vous jouez actuellement avec : {}'.format(joueur.get_nom()))
    def choix_joueur(self):
        """ Affiche une fenêtre contenant les noms de chaques joueurs inscrits sous forme d'un bouton."""
        fenetre = Tk()
        fenetre.title('Choix du joueur')
        l = len(self.__liste_joueurs)
        for n in range(len(self.__liste_joueurs)) :
            elt = self.__liste_joueurs[n]
            Button(fenetre, text = '{}'.format(elt.get_nom()), command = lambda elt=elt : self.modif_joueur(elt)).grid(row = self.__liste_joueurs.index(elt),column = 0)
        Button(fenetre, text = 'Valider choix',command = fenetre.destroy).grid(row = l,column = 0)
    def abandon(self):
        """Affiche la reponse en cas d'abandon"""
        self.__lmot.config(text='Le mot était - {} '.format(self.__mot))
        self.finPartie()
    def finPartie(self):
        """Termine la partie en bloquant les lettres du clavier"""
        for elt in self.__boutons:
            elt.config(state=DISABLED)
    def nouvellePartie(self):
        """Demarre une nouvelle partie : reinitialise le nombre
        de coups possible, l ecran d affichage, genere un nouveau mot, etc..."""
        self.__zoneAffichage.delete(ALL)
        for elt in self.__boutons :
            elt.config(state = NORMAL)
        mot = self.nouveauMot()
        self.__zoneAffichage.setNombreCoupsPossible(7)
        self.__zoneAffichage.afficher()
        self.setmot(mot)
        self.setmotaff('*'*len(mot))
        self.__lmot.config(text='Mot : {}'.format(self.__motaff))
    def setmot(self,mot):
        """Modifie le mot a deviner par mot"""
        self.__mot = mot
    def setmotaff(self,mot):
        """Modifie le mot affiche par mot"""
        self.__motaff = mot
    def traitement(self,lettre):
        """Gere les actions lors du clique sur une lettre du clavier"""
        tourgagnant = 0
        if self.__zoneAffichage.getNombreCoupsPossible() <= 1 : # si plus de tentative possible : c'est perdu
            self.__lmot.config(text =' Vous avez perdu, le mot était : {}'.format(self.__mot))
            self.finPartie() 
        else : # si encore des tentatives
            for i in range(len(self.__mot)):
                if self.__mot[i] == lettre: #si la lettre selectionnee est presente dans le mot a deviner
                    # on modifie les * du mot affiche par la lettre
                    tourgagnant = 1
                    if i == len(self.__mot)-1:
                        self.setmotaff(self.__motaff[:i] + lettre)
                    elif i == 0:
                        self.setmotaff(lettre + self.__motaff[1:])
                    else :
                        self.setmotaff(self.__motaff[:i] + lettre + self.__motaff[i+1:])
                    self.__lmot.config(text='{}'.format(self.__motaff))
        if tourgagnant == 0 : # si la lettre n'était pas présente dans le mot
            self.__zoneAffichage.setNombreCoupsPossible(self.__zoneAffichage.getNombreCoupsPossible()-1)
            self.__zoneAffichage.afficher()
        if "*" not in self.__motaff: # si plus d'inconnues dans le mot, c'est gagne.
            self.__lmot.config(text='{} - Bravo, vous avez gagné'.format(self.__mot))
            if len(self.__liste_joueurs) > 0:
                self.set_score(5+self.get_score()+self.__zoneAffichage.getNombreCoupsPossible())
            self.finPartie()
    def chargeMots(self):
        """Renvoie la liste des mots après avoir convertit le texte qui les contenait """
        fichier = open('mots.txt','r')
        texte = fichier.read()
        fichier.close()
        liste_mots = texte.strip().split() #Transforme la chaine de caractère en une liste de mot.
        return liste_mots
    def nouveauMot(self):
        """Renvoie un mot prit au hasard dans la liste de mot précédente """
        liste_mots = self.chargeMots()
        return liste_mots[randint(0,len(liste_mots))]
   
   
class MonBoutton(Button):
    def __init__(self,fen,f,tex):
        Button.__init__(self,master=f,text=tex)
        self.__t = tex
        self.fen = fen
        self.config(command = self.cliquer)
    def cliquer(self):
        """Lance la procedure de traitement a chaque clique sur une lettre """
        self.config(state = DISABLED)
        self.fen.traitement(self.__t)


fen = FenPrincipale()
fen.mainloop()
