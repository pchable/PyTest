import fibo
import Matrices
import Edges
# import PlotGraph
# import Mandel
import BasicFunctions
import Canvas

print("Bienvenue dans ce test de fonctions Python!")

BasicFunctions.loop(5, 10)

BasicFunctions.firstfunction("Ceci est mon texte")
BasicFunctions.essai_dictionnaire()
fibo.fib(10)
# PlotGraph.essai_courbe()
# PlotGraph.essai_sinus()
Matrices.multiplication_matrices()


# PlotPy.draw_all()

# Mandel.ShowMandel()


edge = Edges.Edge("A", "B")
other = Edges.Edge("B", "C")
last = Edges.Edge("C", "D")
edge.print()
other.print()
connected = edge.connect(other)
connected = connected.connect(last)
connected.print()

Canvas.draw_canvas()
