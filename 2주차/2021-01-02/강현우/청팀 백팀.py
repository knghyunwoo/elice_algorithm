b1,b2,b3,b4 = map(int, input().split())
w1,w2,w3,w4 = map(int, input().split())

blue = b1 + b2 + b3 + b4
white = w1 + w2 + w3 + w4

print(blue if blue>=white else white)