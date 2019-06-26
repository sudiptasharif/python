##animals = []
##animals.append("lion")
##animals.append("tiger")
##animals.append("monkey")
##animals.append("bear")
##animals.append("deer")
##
##for animal in animals:
##    print(animal)
##
##magicians = ["alice", "david", "carolina"]
##
##for magician in magicians:
##    print(magician.title() + ", that was a great trick")
##print("I can't wait to see your next trick, "+magician.title()+".\n")
##    
##print("Thank you, everyone. That was a great magic show!")
##
##
##engClubs = ["liverpool", "man city", "man united", "arsenal"]
##engClubs.append("spurs")
##engClubs.append("everton")
##engClubs.append("wolves")
##
##print("Total length of engClubs = ",len(engClubs))
##
##msg = "=="*10
##
##for club in engClubs:
##    msg = club.title() + " is an english premier league club." 
##    print(msg)
##
##league = "English Premier League"
##msg = "I love the "+league+"."
##print(msg)
##
##league = "La Liga"
##msg = "I love the "+league+"."
##print(msg)
##
##for i in range(10):
##    print(i)
##
##for i in range(1,5):
##    print(i)


##nums = list(range(50))
##print(len(nums))
##
##nums = list(range(1000, 2000, 100))
##print(len(nums))
##
##for num in nums:
##    print(num)

##squares = []
##for value in range(1,11):
##    squares.append(value**2)
##print(squares);
##
##
##nums = [12, 45, 23, 8, 4, 33, 55, 98, 32]
##maxNum = max(nums)
##minNum = min(nums)
##total = sum(nums)
##print("Nums",nums)
##print("Max Num = ",maxNum)
##print("Min Num = ", minNum)
##print("Total = ",total)
##
##
##names = ["bob", "tom", "kelly", "peter", "david"]
##maxName = max(names)
##minName = min(names)
##print(maxName)
##print(minName)
##
##'''The following gives an error'''
###sumName = sum(names)

'''SLICING LISTS'''
##players = ["charles", "martina", "michael", "florence", "eli"]
##print(players)
## 
##slicedPlayers = players[0:3]
##print(slicedPlayers)
##print()
##colors = ["red", "green", "blue", "orange", "pink", "olive", "brown", "yellow"]
##print(colors)
##print()
##print(len(colors))
##
##fromColors = colors[1:6]
##print(fromColors)
##
##fromColors = colors[:4]
##print(fromColors)
##
##fromColors = colors[:]
##print(fromColors)
##
##fromColors = colors[-3:]
##print(fromColors)

engClubs = ["manchester city", "liverpool", "chelsea", "tottenham hotspur", "arsenal"]
engClubs.append("Manchester United")
engClubs.append("Wolverhampton Wandereres")
engClubs.append("Everton")
engClubs.append("Leicester City")
engClubs.append("West Ham United")
#print(engClubs)

top = 4
print("Here are the top "+str(top)+" EPL club(s)")
i = 0;
for club in engClubs[:top]:
    print(str(i+1)+".",club.title())
    i = i+1

'''COPYING LISTS'''

myMovies = ["iron man", "super man", "spider man"]
friendMovies = myMovies[:]
friendMovies.append("bat man")
friendMovies.append("cat women")

print("My Movies:",myMovies)
print("My Friend's Movies:",friendMovies)


newPapers = ["the guardian", "bbc", "the independent", "the sun", "times"]

favLang = ["python", "java", "c#"]
tomFavLang = favLang[:]

tomFavLang.append("c")
tomFavLang.append("c++")
tomFavLang.append("delphi")

msg = "favorite programming languages:"
print("My "+msg, favLang)
print("Tom's "+msg, tomFavLang)
