import random

#EuroMillions Number Picker
#Picks five numbers between 1 and 49
#Picks two numbers between 1 and 12

balls = []
for ball in range(49):
    balls.append(ball + 1)
    
stars = []
for star in range(12):
    stars.append(star + 1)

chosenBalls = []
for i in range(5):
    chosenBall = random.choice(balls)
    chosenBalls.append(chosenBall)
    balls.remove(chosenBall)

print("Your chosen EuroMillions balls are: ")
chosenBalls.sort()
for i in range(5):
    if i < 4:
        print(chosenBalls[i], end = " - ")
    else:
        print(chosenBalls[i])

chosenStars = []
for i in range(2):
    chosenStar = random.choice(stars)
    chosenStars.append(chosenStar)
    stars.remove(chosenStar)

chosenStars.sort()
print(chosenStars[0], end = " - ")
print(chosenStars[1])

#Lotto Number Picker
#Picks six numbers between 1 and 59

balls = []
for ball in range(59):
    balls.append(ball + 1)

chosenBalls = []
for i in range(6):
    chosenBall = random.choice(balls)
    chosenBalls.append(chosenBall)
    balls.remove(chosenBall)

print("Your chosen Lotto balls are: ")
chosenBalls.sort()
for i in range(6):
    if i < 5:
        print(chosenBalls[i], end = " - ")
    else:
        print(chosenBalls[i])