def l(msg):
    print(msg)


nationalTeams = ["england", "france", "germany", "portugal", "argentina", "brazil"]

englishClubs = ["liverpool", "man city", "man united", "spars", "everton"]

spanishClubs = ["barcelons", "real madrid", "athletico madrid", "malaga"]

langs = ["english", "french", "bengali", "arabic", "hindi"]

index = 5
team = nationalTeams[index]
#l(team)

names = ["tom smith", "bob dillion", "joe montana", "john doe"]

l(names[0].title())
l(names[1].title())
l(names[2].title())

name = names[0].title()
msg = "Good evening! My name is "+name.title()+"."
l(msg)

name = names[1].title()
msg = "Hi there! My name is "+name.title()+"."
l(msg)

name = names[2].title()
msg = "Howdy! My name is "+name.title()+"."
l(msg)

msg = "Someday, I would like to watch "+englishClubs[0].title() + " live."
l(msg)

msg = "I would like to watch "+nationalTeams[2].title()+" play against "+nationalTeams[1].title()+" in 2022 football world cup."
l(msg)

msg = "My native language is "+langs[2].title()+"."
l(msg)

msg = "I can speak "+langs[-1].title()+"."
l(msg)

l(langs)

#langs[0] = "nepali"'
lang = "nepali"
langs.append(lang)


lang = "japanese"
langs.append(lang)
l(langs)

# append makes it easy to build lists dynamically
animals = []
animals.append("lion")
animals.append("tiger")
animals.append("monkey")
animals.append("fox")
animals.append("wolf")
animals.append("deer")
animals.append("zebra")

l(animals)


animals.insert(6,"bear")
l(animals)

animals.insert(2, "alligator")
l(animals)


animals[0] = "king kong"
l(animals)




















