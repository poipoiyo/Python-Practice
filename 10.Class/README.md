# Class

Design data based on real world (or some concept)

For example :
```python
class Player():
  def __init__(self, name):
    self.name = name
    self.score = 0
  def who(self):
    return self.name
  def getScore(self):
    return self.score
  def setScore(self, score):
    self.score = score

class Game:
  def __init__(self, player):
    self.live = 10
    self.player = player
  def isGameOver(self):
    return self.live <= 0
```

## Homework
You are handling a billing system. 
Customer will send their orders to systems.
You should list their products together, and how much they should pay.

### Input :
- `produce.txt`: product list
- `rule.txt`: in some conditions, products will be on sales
- `record.txt`: logs from system

### Output :
Take robin's billing:
```
Robin: AABBA
Robin: BBAC
Robin: A
```

