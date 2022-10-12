import random
from bke import MLAgent, EvaluationAgent, is_winner, opponent, RandomAgent, load, start

#makkelijk
class MyRandomAgent(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    return random.randint(1,500)

#moeilijk
class MyAgent(MLAgent):
  def evaluate(self, board):
    if is_winner(board, self.symbol):
      reward = 1
    elif is_winner(board, opponent[self.symbol]):
      reward = -1
    else:
      reward = 0
    return reward         

#train&plot
class MyAgent(MLAgent):
  def evaluate(self, board):
    if is_winner(board, self.symbol):
      reward = 1
    elif is_winner(board, opponent[self.symbol]):
      reward = -1
    else:
      reward = 0
    return reward

my_random_agent = MyRandomAgent()

my_agent = MyAgent(alpha=0.9, epsilon=0.3)
my_agent = load("MyAgent_3000")      
my_agent.learning = True

my_trainagent = MyAgent(alpha=1.0, epsilon=0.1)
random_agent = RandomAgent()
    
#start menu
print("Welkom bij boter, kaas en eieren!")

def games():
  print("Kies een van de volgende menu's: \n1. een speler \n2. twee spelers \n3. trainen en valideren")
  x=input("keuze:")
  if x=="1":
    print("een speler \n")
    print("Kies een niveau: \n1. makkelijk \n2. moeilijk")
    y=input("keuze:")
    if y=="1":
      print("makkelijk")
      
      start(player_o=my_random_agent)

      playagain()
      
    elif y=="2":
      print("moeilijk")

      start(player_o=my_agent)

      playagain()
    
  elif x=="2":
    print("twee spelers")
  
    start()

    playagain()
  elif x=="3":
    print("trainen en valideren /n")
   
    random.seed(1)
  
    train_and_plot(
        agent=my_trainagent,
        validation_agent=random_agent,
        iterations=50,
        trainings=500,
        validations=1000)

    playagain()

  else:
    print("Uw input is incorrect \n")




def playagain():
  print("Wilt u opnieuw beginnen?")
  y=input()
  if y=="ja" or y=="Ja" or y=="JA": 
    print("\n")
    games() 
  elif y=="nee" or y=="Nee" or y=="NEE":
    print("Tot ziens!")
    
games()