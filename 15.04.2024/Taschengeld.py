import matplotlib.pyplot as plt

a0 = 1
b0 = 0.1
a = []
b = []

for i in range(0,12):
    a.append(a0)
    a0 += 2
    b.append(b0)
    b0 = 2 * b0

x_werte = range(1, len(a)+1)

# Diagramm erstellen
plt.plot(x_werte, a, marker='o', label='a')
plt.plot(x_werte, b, marker='s', label='b')  # hinzugefügt

# Achsenbeschriftungen
plt.xlabel('Geld')
plt.ylabel('Monat')

# Titel
plt.title('Hausaufgabe IMP')

# Diagramm anzeigen
plt.grid(True)
plt.legend()  # hinzugefügt für die Legende
plt.show()