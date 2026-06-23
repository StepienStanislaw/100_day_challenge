import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
wybor = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

gra = ['kamien', 'papier', 'nozyce']
wyborGry = int(random.random() * len(gra))

print("Ty wybrałeś:", gra[wybor])
print("Komputer wybrał:", gra[wyborGry])


if wybor == wyborGry:
    print("remis")
elif wyborGry == 0 and wybor == 2:
    print('przegrales')
elif wyborGry == 2 and wybor == 1:
    print('przegrales')
elif wyborGry == 1 and wybor == 0:
    print('przegrales')
else:
    print("przegrales")
