blue = sum(map(int, input().split()))
white = sum(map(int, input().split()))

print(blue if blue>=white else white)