# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:20:23 2017
Julien Verdun
"""

    
from tkinter import *
from math import sqrt,pi
from random import randint
from tkinter.messagebox import *

# Implémentation des classes shape, Rectangle, square et circle tirée des TD précédents.
# Version simple du jeu.


class Shape :
    """
    This class allows to built a shape, defined by its center (coordinate xc and yx)
    and its color.
    """
    def __init__(self,xc,yc,c):
        self.__centre = (xc,yc)
        self.__color = c
    def get_centre(self):
        """
        Return the coordinates of the centre of the shape.
        """
        return self.__centre
    def get_color(self):
        """
        Return the color of the shape.
        """
        return self.__color

class Circle(Shape) :
    """
    This class inherits of the class shape and allows to built a circle of diameter d.
    """
    def __init__(self,xc,yc,c,d):
        Shape.__init__(self,xc,yc,c)
        self.__diameter = d
    def get_diameter(self):
        """
        Return the diameter of the circle.
        """
        return self.__diameter
    def perimeter(self):
        """
        Return the perimeter of the circle.
        """
        return pi * self.__diameter
    def area(self):
        """
        Return the area of the circle.
        """
        return pi*(self.__diameter/2)**2
    def affiche(self,zoneaffiche):
        """
        Display the circle on the window zoneaffiche.
        """
        (xc,yc) = self.get_centre()
        d = self.__diameter
        c = self.get_color()
        zoneaffiche.create_oval(xc-d/2,yc-d/2,xc+d/2,yc+d/2,outline= c,fill=c)


class Square(Shape) :
    """
    This class inherits of the class shape and allows to built a square of side l.
    """
    def __init__(self,xc,yc,c,l):
        Shape.__init__(self,xc,yc,c)
        self.__width = l
    def get_width(self):
        """
        Return the width of the square.
        """
        return self.__width
    def perimeter(self):
        """
        Return the perimeter of the square.
        """
        return 4*self.__width
    def area(self):
        """
        Return the area of the square.
        """
        return self.__width**2
    def affiche(self,zoneaffiche):
        """
        Display the square on the window zoneaffiche.
        """
        (xc,yc) = self.get_centre()
        l = self.__width
        c = self.get_color()
        zoneaffiche.create_rectangle(xc-l/2,yc-l/2,xc+l/2,yc+l/2,outline= c,fill=c)

    
        
class Rectangle(Shape):
    """
    This class inherits of the class shape and allows to built a Rectangle of width l and height h.
    """
    def __init__(self,xc,yc,c,l,h):
        Shape.__init__(self,xc,yc,c)
        self.__width = l
        self.__height = h
    def get_width(self):
        """
        Return the width of the Rectangle.
        """
        return self.__width
    def get_height(self):
        """
        Return the height of the Rectangle.
        """
        return self.__height
    def perimeter(self):
        """
        Return the perimeter of the Rectangle.
        """
        return 2*(self.__width+self.__height)
    def area(self):
        """
        Return the area of the Rectangle.
        """
        return self.__width*self.__height
    def affiche(self,zoneaffiche):
        """
        Display the Rectangle on the window zoneaffiche.
        """
        (xc,yc) = self.get_centre()
        l = self.__width
        L = self.__height
        c = self.get_color()
        zoneaffiche.create_rectangle(xc-L/2,yc-l/2,xc+L/2,yc+l/2,outline= c,fill=c)

    
class Dessin:
    """
    This class allows to manage many different shapes (circles, Rectangles and squares).
    """
    def __init__(self): 
        self.__list_of_shapes = []#list of the shapes
    def ajouter_shapes(self,shape_a_ajouter):
        """
        Add a shape to the liste of shapes.
        """
        self.__list_of_shapes.append(shape_a_ajouter)
    def afficher_shapes(self,zoneaffiche):
        """
        Display all the shapes in the list of shapes on the window zoneaffichage.
        """
        for elt in self.__list_of_shapes :
            elt.affiche(zoneaffiche)
    def delete_shapes(self):
        """
        Delete the shapes in the list of shapes.
        """
        self.__list_of_shapes = []
            
            
            
        

class ZoneAffichage(Canvas):
    """
    This class inherits of the class Canvas and creates the window where all the elements are displayed.
    """
    def __init__(self,parent, w, h, c, n):
        Canvas.__init__(self, width = w, height = h, bg = c)
        self.__numbermoves = n #number of available moves
        self.__dessin = Dessin()
    def afficher(self):
        """
        Dispayed the different texts and shapes of the window.
        """
        # List of the shape that represents the hangman.
        self.__dessin.delete_shapes()
        self.__dessin.ajouter_shapes(Rectangle(125,255,'black',10,75))
        self.__dessin.ajouter_shapes(Rectangle(125,140,'black',220,10))
        self.__dessin.ajouter_shapes(Rectangle(215,35,'black',10,170))
        # Depending on the number of moves available, creates the members of the hangman.
        if self.__numbermoves <= 7:
            self.__dessin.ajouter_shapes(Rectangle(297.5,60,'black',50,5))
        if self.__numbermoves <= 6 :
            self.__dessin.ajouter_shapes(Circle(297.5,80,'black',40))
        if self.__numbermoves <= 5:
            self.__dessin.ajouter_shapes(Rectangle(297.5,107.5,'black',25,10))
        if self.__numbermoves <= 4:
            self.__dessin.ajouter_shapes(Rectangle(297.5,147.5,'black',55,30))
        if self.__numbermoves <= 3:
            self.__dessin.ajouter_shapes(Rectangle(286.5,187.5,'black',25,8))
        if self.__numbermoves <= 2:
            self.__dessin.ajouter_shapes(Rectangle(308.5,187.5,'black',25,8))
        if self.__numbermoves <= 1:
            self.__dessin.ajouter_shapes(Rectangle(267.5,122.5,'black',5,30))
        if self.__numbermoves <= 0:
            self.__dessin.ajouter_shapes(Rectangle(327.5,122.5,'black',5,30))
        # Displays the shapes.
        self.__dessin.afficher_shapes(self)
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
        
    
class FenPrincipale(Tk):
    """
    This class inherits of the class Tk, implements the logic of the game and modifys the elements of the window.
    """
    def __init__(self):
        Tk.__init__(self)

        f2 = Frame(self)
        f2.pack(side = TOP,padx = 5,pady = 5)

        self.__zoneAffichage = ZoneAffichage(self,480,320,'white',8)
        self.title('Jeu du Pendu')
        self.__zoneAffichage.pack(padx=5, pady=5)

        f1 = Frame(self)
        f1.pack(side=TOP, padx=5, pady=5)

        # Add the different buttons
        self.__boutonNew = Button(f2, text ='New Game', width=15, command = self.newGame).grid(row = 0, column = 0)
        self.__boutonQuitter  =  Button(f2,  text  ='Exit',  command  = self.destroy).grid(row = 0, column = 1)
        self.__lWord = Label(self)
        self.__Word = ''
        self.__Wordaff = ''
        self.__lWord.pack(side=TOP)
        self.__lWord.config(text='Welcome, you can play by clicking on the button New Game')
        # Add the buttons to choose the letters.
        self.__boutons = []
        for i in range(26):
            bouton = MonBoutton(self,f1,chr(ord('A')+i))
            bouton.grid(row=(i//7)+2,column = i-7*(i//7)+2)
            self.__boutons.append(bouton)
            self.__boutons[i].config(command= self.__boutons[i].cliquer, state = DISABLED)

    def finGame(self):
        """
        Freeze the letters.
        """
        for elt in self.__boutons:
            elt.config(state=DISABLED)

    def newGame(self):
        """
        Begin a new game, reinitiate the number of moves, the window, generate a new word and so on.
        """
        self.__zoneAffichage.delete(ALL)
        #Letters available.
        for elt in self.__boutons :
            elt.config(state = NORMAL)
        # Generate a new word
        Word = self.newWord()
        self.__zoneAffichage.setnumbermovesavailable(8)
        self.__zoneAffichage.afficher()
        self.setWord(Word)
        self.setWordaff('*'*len(Word))
        self.__lWord.config(text='Word : {}'.format(self.__Wordaff))

    def setWord(self,Word):
        """
        Change the value of the variable word by Word.
        """
        self.__Word = Word

    def setWordaff(self,Word):
        """
        Change the value of the variable word displayed by Word.
        """
        self.__Wordaff = Word

    def traitement(self,lettre):
        """
        Manage the variables and window when a letter is clicked.
        """
        tourgagnant = 0
        # if no more moves available : that's a defeat, we display the right word and block the keys.
        if self.__zoneAffichage.getnumbermovesavailable() <= 0 :
            self.__lWord.config(text =' You lose, the word was : {}'.format(self.__Word))
            self.finGame()
        # if moves avaible, we find the letter pressed
        else :
            for i in range(len(self.__Word)):
                if self.__Word[i] == lettre: #if the letter pressed is a letter of the word
                    # we change the * in the displayed word by the letters
                    tourgagnant = 1
                    if i == len(self.__Word)-1:
                        self.setWordaff(self.__Wordaff[:i] + lettre)
                    elif i == 0:
                        self.setWordaff(lettre + self.__Wordaff[1:])
                    else :
                        self.setWordaff(self.__Wordaff[:i] + lettre + self.__Wordaff[i+1:])
                    self.__lWord.config(text='{}'.format(self.__Wordaff))
        # if the letter was not in the word
        if tourgagnant == 0 :
            # if there is no more moves available, that's a defeat
            if self.__zoneAffichage.getnumbermovesavailable() == 1:
                self.__lWord.config(text =' You lose, the word was : {}'.format(self.__Word))
                self.finGame()
            self.__zoneAffichage.setnumbermovesavailable(self.__zoneAffichage.getnumbermovesavailable()-1)
            self.__zoneAffichage.afficher()
        # if no more letters to find in the word : that's a win.
        if "*" not in self.__Wordaff:
            self.__lWord.config(text='{} - Congratulation, you won !'.format(self.__Word))
            self.finGame()

    def chargeWords(self):
        """
        Return the liste of words after transforming the text
        """
        fichier = open('words.txt','r')
        texte = fichier.read()
        fichier.close()
        # Transform the string into a list
        liste_Words = texte.strip().split()
        return liste_Words

    def newWord(self):
        """
        Return a word taking randomly in the list of words.
        """
        liste_Words = self.chargeWords()
        return liste_Words[randint(0,len(liste_Words))]
   
   
   
class MonBoutton(Button):
    """
    This class inherits of the class Button and manages the interactions
    of the players with the buttons.
    """
    def __init__(self,fen,f,tex):
        Button.__init__(self,master=f,text=tex)
        self.__t = tex
        self.fen = fen
        self.config(command = self.cliquer)
    def cliquer(self):
        """
        Whenever a touch is pressed, the game logic is launched.
        """
        self.config(state = DISABLED)
        self.fen.traitement(self.__t)


# Run the game
if __name__ == "__main__":
    fen = FenPrincipale()
    fen.mainloop()

