from random import choice

class joueur (object) :
  """Cette classe permet de creer un joueur qui a un nom, un signe pas encore défini et un nombre de point"""
  def __init__(self,id,nom,signe,point):
    self.id = id
    self.nom = nom
    self.point = point
    self.signe = signe
    
  def ajout_point(self):
    self.point = self.point + 1
    
  def pose_signe_random (self, signes) :
    """Choisis un signe parmi la liste deja existante"""
    self.signe = choice(signes)
    
  def pose_signe (self, signes) :
    """Choisis un signe à partir du paramètre"""
    self.signe = signes
    
  def retour_signe(self):
    return self.signe

  def afficher_pts(self):
    print(self.nom,"a",self.point,"points")
    
  def afficher_joueur(self):
    print("Le joueur",self.id," s'appelle",self.nom,"il a",self.point,"points")
    
  def montrer_signe(self):
    print(self.nom,"joue le signe",self.signe)

  def retourne_pts(self):
    return self.point 

class verif (object) :
  def __init__(self,signe):
    self.signe = signe

  def afficher_signe(self):
    print(self.signe)
    
  def check (self,signe2):
    if self.signe == "Pierre" and signe2 == "Ciseaux" :
      """joueur_1.ajout_point()"""
      return True
    elif self.signe == "Pierre" and signe2 == "Papier" :
      return False
    elif self.signe == "Papier" and signe2 == "Pierre" :
      return True
    elif self.signe == "Papier" and signe2 == "Ciseaux" :
      return False
    elif self.signe == "Ciseaux" and signe2 == "Papier" :
      return True 
    elif self.signe == "Ciseaux" and signe2 == "Pierre" :
      return False
    else:
      return "je ne comprend pas"
      
  def gestion_erreur(self):
    signe1 = self.signe
    if signe1 == "Pierre" or signe1 == "Papier" or signe1 == "Ciseaux" :
      return True
    else :
      print("Veuillez entrer un signe valide")
      signe1 = None
      return False

#main program
signes = ["Pierre", "Papier", "Ciseaux"]

joueur_1 = joueur("1","Pablo","None",0)
joueur_2 = joueur("2","René","None",0)

joueur_1.afficher_joueur()
joueur_2.afficher_joueur()
print("\n")

joueur_1.afficher_pts()
joueur_2.afficher_pts()

while joueur_1.retourne_pts() <= 3 or joueur_2.retourne_pts() <= 3:
  signe_j1 = input("Choisissez un signe: ")
  joueur_1.pose_signe(signe_j1)
  signe1 = verif(str(joueur_1.retour_signe()))
  joueur_1.montrer_signe()
  
  if signe1.gestion_erreur() == True :
    joueur_2.pose_signe_random(signes)
    signe_2 = joueur_2.retour_signe()
    signe2 = verif(signe_2)
    
    joueur_2.montrer_signe()
    signe2.gestion_erreur()
    
    if signe1.check(signe_2) == True :
      joueur_1.ajout_point()
    elif signe1.check(signe_2) == False :
      joueur_2.ajout_point()
    
    joueur_1.afficher_pts()
    joueur_2.afficher_pts()
    print("\n")

  if joueur_1.retourne_pts() == 3:
    print("Bravo, joueur 1 gagne")
    break
  elif joueur_2.retourne_pts() == 3:
    print("Bravo, joueur 2 gagne")
    break