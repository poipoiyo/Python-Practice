
strInput = "Give me level 5 snake with 4 corners."
#5       5       5    
# 4     4 4     4 4   
#  3   3   3   3   3  
#   2 2     2 2     2 
#    1       1       1

level = int(strInput.split(" ")[3])
corner = int(strInput.split(" ")[-2])


len = level + corner*(level-1)
matrix = [[" " for _ in range(len)] for _ in range(level)]	

# concept :
# 利用方向向量決定目前要填入哪個位置以及要填入哪個值
# 只要撞到邊界就讓它反彈 (乘上-1)
ix = 1
iy = 1
x = 0
y = 0
lvCount = 0

while(corner >= 0):
  lvCount += iy
  if y < 0 or y > level:
    break
  matrix[y][x] = str(lvCount)

  if (y+iy) == level or (y+iy) < 0:
    iy *= -1
    corner -= 1

  x += ix
  y += iy

# print result
for row in matrix:																
  print(''.join(row))	
