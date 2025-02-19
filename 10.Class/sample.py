import math
class Bill:
  def __init__(self, name):
    self.name = name
    self.buy = ""
    self.cost = 0

  def addBill(self, buy, cost):
    self.buy += buy
    self.buy = ''.join(sorted(self.buy))
    self.cost += cost
    
  def display(self):
    line = self.name + ": " + self.buy + ", $" + str(self.cost)
    print(line)

PEN = 'A'
PURSE = 'B'
KEYCHAIN = 'C'
FORK = 'D'
TOOTHBRUSH = 'E'
CANDY = 'F'

products = {
 PEN: 10, PURSE:350, KEYCHAIN:100, FORK:150, TOOTHBRUSH:80, CANDY:50  
}

lines = [
  "Robin: BB",
  "Taylor: CCAC",
  "Gray: AC",
  "Robin: AADA",
  "Jefferson: DBA",
  "Taylor: C",
  "Robin: DEFC",
  "Jefferson: DA"
]

Bills = dict()

# Sequence to apply the rule
def discount(buy: str, cost: int) -> list:
  _cost = cost
  # Rule 1
  if cost >= 500:
    _cost = min(_cost, cost*0.85)

  # Rule 2
  if buy.count(PURSE) > 0:
    b_times = buy.count(PURSE)
    a_times = buy.count(PEN)
    if b_times > a_times:
      # Free "more" product A
      buy += PEN * (b_times - a_times)
      _cost = min(_cost, cost - products[PEN]*a_times)
    else:
      # Free "some" product A
      _cost = min(_cost, cost - products[PEN]*b_times)

  # Rule 3
  if buy.count(FORK) > 0 and buy.count(CANDY) > 0 and buy.count(TOOTHBRUSH) > 0:
    discountE = min(buy.count(KEYCHAIN), buy.count(FORK))
    discountE = min(discountE, buy.count(TOOTHBRUSH))
    discountCost = products[TOOTHBRUSH] - 70
    _cost = min(_cost, cost - discountE*discountCost)
  
  # Rule 4
  if buy.count(KEYCHAIN) >= 2:
    _cost = min(_cost, cost*0.95)

  return [buy, math.ceil(_cost)]

# Bills = {"Robin": Bill(Robin)}  

def calculate(s: str):
  name = s.split(':')[0]
  buy = s.split(': ')[1]

  if name in Bills:
    b = Bills[name]
  else:
    b = Bill(name)

  cost = 0
  for product, value in products.items():
    cost += buy.count(product)*value

  [buy, cost] = discount(buy, cost)
  b.addBill(buy, cost)
  Bills[name] = b 


#######################
for line in lines:
  calculate(line)

for key, value in Bills.items():
  value.display()


