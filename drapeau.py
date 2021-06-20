#importation du module turtle qui permet de dessiner
# dessin notre drapeau national 
import turtle    
t=turtle
#le curseur vaetre invisible avec ;une epaisseur (1),une vitesse normale et en noir
t.hideturtle()
t.color("black")
t.width(1)
t.speed("normal")
#dessin de la 1iere partie du rectangle en vert
t.fillcolor("green")
t.begin_fill()
t.forward(200)
t.left(90)
t.up()
t.forward(150)
t.down()
t.left(90)
t.forward(200)
t.left(90)
t.forward(150)
t.end_fill()
#changement de coordonnee du curseur pour pouvoir dessiner la 2ieme partie en jaune
t.setpos(200,0)
turtle.setheading(0)
#dessin de la 2ieme partie en jaune
t.fillcolor("yellow")
t.begin_fill()
t.forward(200)
t.left(90)
t.up()
t.forward(150)
t.down()
t.left(90)
t.forward(200)
t.left(90)
t.up()
t.forward(150)
t.down()
#changement de coordonnee du curseur pour pouvoir dessiner la 3ieme partie en rouge
t.setpos(200,0)
turtle.setheading(0)
t.end_fill()
t.forward(200)
t.fillcolor("red")
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(150)
t.left(90)
t.forward(200)
t.left(90)
t.up()
t.forward(150)
t.left(90)
t.down()
t.end_fill()
#retour du curseur aux coordonnees du milieu pour le dessin de 4ieme parte qui est l'etoile
t.back(90)
t.goto(0,0)
t.width(2)
t.up()
t.goto(270,75)
t.down()
#dessin de l'etoile en vert
AF=25
a=180-180/5
t.fillcolor("green")
t.begin_fill()
for i in range(5): 
     t.forward(AF)
     t.right(a-360/5)
     t.forward(AF)
     t.left(a)
t.end_fill()
done()
#au final on a le drapeau de notre nation














 