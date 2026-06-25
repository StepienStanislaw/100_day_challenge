Nauczylem sie zeby uzywac 

haslo = []
haslo.append(random.choice(letters))

Zamiast 

haslo = []
haslo += (random.choice(letters))

Bo append dodaje tylko JEDEN element listy, natomiast += bierze i rozbija na mniejsze elemenety i dodaje kazdy osobno

Do zapamietania rowniez leci funkcja .shuffle() noi to miesza elementy listy 