import random as r
#Pierre Feuille Ciseaux

shifumi = ["Pierre", "Feuille", "Ciseaux"]
name = ''


def round():
  player_choice = input("Choisissez un signe: ")
  bot = r.choice(shifumi)
  return check(player_choice, bot)


def check(player_choice, bot):
  #Cette fonction va vérifier quel joueur a gagné le point et si il y a égalité
  if player_choice == "Pierre" and bot == "Ciseaux" or player_choice == "Ciseaux" and bot == "Feuille" or player_choice == "Feuille" and bot == "Pierre":
    #On va voir si le joueur prend le point sur le bot et si c'est le cas on va incrémenter ses points de 1
    print(name + " a gagné")
    #On return 2 pour indiqer à qui il fau ajouter les points 
    return 2
  elif player_choice == "Ciseaux" and bot == "Pierre" or player_choice == "Feuille" and bot == "Ciseaux" or player_choice == "Pierre" and bot == "Feuille":
    #A l'inverse, si le bot gagne la manche contre le joueur,on incrémente ses points de 1
    print("Le bot a gagné la manche")
    #On return 1 pour indiqer à qui il fau ajouter les points 
    return 1
  elif player_choice == "Ciseaux" and bot == "Ciseaux" or player_choice == "Feuille" and bot == "Feuille" or player_choice == "Pierre" and bot == "Pierre":
    print("Egalité :/")
  else:
    print("Signe invalide")


def game():
  #Cette fonction va lancer une game en BO5
  #Je l'ai mise en format fonction pour
  bot_pts = 0
  player_pts = 0
  global name
  name = input("Entrez votre nom de dieu du shifumi: ")
  while bot_pts < 3 and player_pts < 3:
    temp = round()
    if temp == 1:
      bot_pts = bot_pts + 1
    elif temp == 2:
      player_pts = player_pts + 1
    print("Le bot a "+ str(bot_pts) + " pts")
    print(name+ " a " +str(player_pts) + " pts")
  if bot_pts == 3:
    print("Le bot a gagné le jeu")
  else:
    print(name + " a gagné le jeu")


game()