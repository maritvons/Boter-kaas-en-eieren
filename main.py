import random
from bke import MLAgent, EvaluationAgent, is_winner, opponent, RandomAgent, train_and_plot, load, start 

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


#start menu
print("1. een speler (slim) \n2. een speler (dom) \n3. twee spelers \n4. tegenstander trainen \n5. validatie grafiek")

x=input("keuze:")
if x=="1":
  print("slimme speler")
  start(player_o=my_agent)
  
elif x=="2":
  print("domme speler")
  r=2
elif x=="3":
  print("twee spelers")
  r = 3
elif x=="4":
  print("tegenstander trainen")
  r = 4
elif x=="5":
  print("validatie grafiek")
  r = 5
else:
  print("incorrecte input")

