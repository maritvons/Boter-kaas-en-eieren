import random
from bke import MLAgent, EvaluationAgent, is_winner, opponent, RandomAgent, train_and_plot, load, validate, plot_validation, start 

#start menu
print("Welkom bij boter, kaas en eieren!")

while True:
  print("Kies een van de volgende menu's: \n1. een speler \n2. twee spelers \n3. trainen en valideren")
  x=input("keuze:")
  if x=="1":
    print("een speler \n")
    print("Kies een niveau: \n1. makkelijk \n2. moeilijk")
    y=input("keuze:")
    if y=="1":
      print("makkelijk")
  
      class MyRandomAgent(EvaluationAgent):
        def evaluate(self, board, my_symbol, opponent_symbol):
          return random.randint(1,500)
    
      my_random_agent = MyRandomAgent()
      start(player_o=my_random_agent)
  
      print("Wilt u opnieuw beginnen?")
      x=input()
      if x=="ja" or x=="Ja" or x=="JA":
        print("\n")
        continue 
      if x=="nee" or x=="Nee" or x=="NEE":
        break
        print("Tot ziens!")
      
    elif y=="2":
      print("moeilijk")
      
      class MyAgent(MLAgent):
        def evaluate(self, board):
          if is_winner(board, self.symbol):
            reward = 1
          elif is_winner(board, opponent[self.symbol]):
            reward = -1
          else:
            reward = 0
          return reward
         
      my_agent = MyAgent()
      my_agent = load("MyAgent_3000")
       
      my_agent.learning = False
      start(player_o=my_agent)
  
      print("Wilt u opnieuw beginnen?")
      x=input()
      if x=="ja" or x=="Ja" or x=="JA":
        continue 
        print("\n")
      if x=="nee" or x=="Nee" or x=="NEE":
        break
        print("Tot ziens!")
    
  elif x=="2":
    print("twee spelers")
  
    start()

    print("Wilt u opnieuw beginnen?")
    x=input()
    if x=="ja" or x=="Ja" or x=="JA":
      continue 
      print("\n")
    if x=="nee" or x=="Nee" or x=="NEE":
      break
      print("Tot ziens!")
    
  elif x=="3":
    print("trainen en valideren")
  
    class MyAgent(MLAgent):
      def evaluate(self, board):
          if is_winner(board, self.symbol):
              reward = 1
          elif is_winner(board, opponent[self.symbol]):
              reward = -1
          else:
              reward = 0
          return reward
   
    random.seed(1)
   
    my_agent = MyAgent()
    random_agent = RandomAgent()
     
    train_and_plot(
        agent=my_agent,
        validation_agent=random_agent,
        iterations=50,
        trainings=100,
        validations=1000)

  else:
    print("Uw input is incorrect \n")

