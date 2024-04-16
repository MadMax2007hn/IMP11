import matplotlib.pyplot as plt

# Die gegebene Folge von Werten
folge = [5000, 5062.5, 5151.09375, 5266.99335938, 5411.83567676, 5587.72033625]

# Die Nummern der Folgenglieder für die x-Achse
x_werte = range(len(folge))

# Diagramm erstellen
plt.plot(x_werte, folge, marker='o')

# Achsenbeschriftungen
plt.xlabel('Jahre')
plt.ylabel('Betrag in Euro')

# Titel
plt.title('Hausaufgabe IMP')

# Diagramm anzeigen
plt.grid(True)
plt.show()