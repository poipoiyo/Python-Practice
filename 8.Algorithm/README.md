# Algorithm

[Reference](https://zh.wikipedia.org/zh-tw/%E7%AE%97%E6%B3%95)
```
演算法（英語：algorithm），在數學（算學）和電腦科學之中，指一個被定義好的、電腦可施行其指示的有限步驟或次序，常用於計算、資料處理和自動推理。
```

## Binary search
For example, guess number in range 1-100, it is not effective to guess randomly.
We should guess 50, 25, 37, ..., to get final solution.

Binary search is telling that, if there is a sorted list, we should always search the middle to find our target.

## Sort
There are some method to sort a list.
For example, bubble sort, always choose the biggest one.
```
[5, 18, 25, 13, 19, 7] -> []
[5, 18, 13, 19, 7] -> [25]
[5, 18, 13, 7] -> [25, 19]
[5, 13, 7] -> [25, 19, 18]
[5, 7] -> [25, 19, 18, 13]
[5] -> [25, 19, 18, 13, 7]
[] -> [25, 19, 18, 13, 7, 5]
```
(`sort` function is using q-sort)

## Homework
You are a professor and you want to rank your students by their average.
There are three lessons, but not students may not take all lessons.
A student, who takes more class, should spend more time studying.
You decide to give their highest scores more weight if he/she takes more class.
(Average should be integer, but you should notice the rank of 80.2 is higher than 80.0)

For example, 

John takes three class and gets [96, 51, 72] points. 
John's average is (96*3+51+72)/5 = 82, because he takes three lessons.
It will be higher than his original grades (96+51+72)/3 = 73. 

Jade takes two class and gets [80, X, 85] points.
Jade's average is (80+85*2)/3 = 83, because he takes three lessons.

Tom takes only one class and gets [X, 68, X] points.
Tom's average is 68.

### Input :
- `scores.txt`: score for all student's.

### Output :
- `ranking.txt` to list their ranking, name, average
```
1. [Jade, 83]
2. [Jhon, 82]
3. [Tom, 68]
```

