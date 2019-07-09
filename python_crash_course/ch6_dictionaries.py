##alien_0 = {"color":"green", "point":5}
##print(alien_0)
####
##alien_0["x_position"] = 0;
##alien_0["y_position"] = 25;
##
##print(alien_0)

##person = {
##    "name" : "sudipta sharif",
##    "age" : 25,
##    "nationality" : "bangladeshi",
##    "religion" : "islam",
##    "university" : "purdue fort wayne",
##    "college" : "g.d. birla",
##    "school" : "st. anthony's school"
##    }
##
##print(person)
##
##person["profession"] = "software developer"
##person["car"] = "toyota camry"
##person["fav footbal club"] = "liverpool"
##
##print(person["fav footbal club"])


##alien = {"color":"green"}
##print("The alien is now "+alien["color"]+".")
##
##alien["color"] = "yellow"
##print("The alien is now "+alien["color"]+".")

##alien = {}
##alien["x"] = 0
##alien["y"] = 25
##alien["speed"] = "medium"
##print("Original x-position: "+str(alien["x"]))
##
##if alien["speed"] == "slow":
##    x_inc = 1
##elif alien["speed"] == "medium":
##    x_inc = 2
##else:
##    x_inc = 3
##
##alien["x"] = alien["x"] + x_inc
##print("New x-position: "+str(alien["x"]))

##student = {}
##student["fname"] = "sudipta"
##student["lname"] = "sharif"
##student["sex"] = "male"
##student["major"] = "computer science"
##
##print(student)
##
##print(student["fname"].title())
##print(student["major"].title())
##
##student["degree"] = "bachelor of science"
##print(student["degree"].title())
##
##
##student["fname"] = "megan"
##student["lname"] = "smith"
##student["sex"] = "female"
##student["major"] = "theology"
##
##print(student)
##
##del student["sex"]
##print(student)

##fav_langs = {
##    "jen": "python",
##    "sarah": "c",
##    "edward": "ruby",
##    "phil": "python"
##    }
##print(fav_langs);
##
##print("Sarah's favorite language is "+
##      fav_langs["sarah"].title() +
##      ".")

##user_0 = {
##    "username": "efermi",
##    "first": "enrico",
##    "last": "fermi"
##    }
##print(user_0)
##
##for key,value in user_0.items():
##    print("\nKey: "+key)
##    print("Value: "+value)
##
##fav_langs = {
##    "jen": "python",
##    "sarah": "c",
##    "edward": "ruby",
##    "phil": "python"
##    }
##
##for name, lang in fav_langs.items():
##    print(name.title() + "'s favorite language is "+lang.title()+".")

##fav_langs = {
##    "jen": "python",
##    "sarah": "c",
##    "edward": "ruby",
##    "phil": "python"
##    }
##
##for key in fav_langs.keys():
##    print(key.title()+" fav lan is: "+fav_langs[key].title())

##fav_langs = {
##    "jen": "python",
##    "sarah": "c",
##    "edward": "ruby",
##    "phil": "python"
##    }
##
##for name in fav_langs:
##    print(name)


##words = {
##    "red": "color red",
##    "sit": "verb to sit down",
##    "stand": "verb to support someone on two legs",
##    "throw":"verb to move something",
##    "london":"name of place",
##    "drive":"operate a car"
##    }
##
##for word in words:
##    print(word + " meaning = "+words[word])

##cities = {
##    "mymensingh":"bangladesh",
##    "delhi":"india",
##    "punjab":"pakisthan",
##    "fort wayne":"usa",
##    "london":"uk",
##    "sydney":"australia",
##    "toronto":"canada",
##    "chicago":"usa",
##    "ohio":"usa",
##    "florida":"usa",
##    "sylet":"bangladesh",
##    "khulna":"bangladesh"
##    }
##
##for country in cities.values():
##    print(country)
##
##print("****"*20)
##print("The following unique countries have been mentioned")
##for country in set(cities.values()):
##    print(country)

##alien_0 = {"color":"green", "points":5}
##alien_1 = {"color":"yellow", "points":10}
##alien_2 = {"color":"red", "points":15}
##
##aliens = [alien_0, alien_1, alien_2]
##
##for alien in aliens:
##    print(alien)

##bangladesh = {
##    "capital": "dhaka",
##    "continent": "asia",
##    "language": "bengali"
##    }
##
##india = {
##    "capital": "new delhi",
##    "continent": "asia",
##    "language": "hindi"
##    }
##
##china = {
##    "capital": "beijing",
##    "continent": "asia",
##    "language": "mandarin"
##    }
##
##australia = {
##    "capital":"sydney",
##    "continent": "australia",
##    "language": "english"
##    }
##
##england = {
##    "capital": "london",
##    "continent": "europe",
##    "language": "english"
##    }
##
##wales = {
##    "capital": "cardiff",
##    "continent": "europe",
##    "language": "welsh"
##    }
##
##france = {
##    "capital": "paris",
##    "continent": "europe",
##    "language": "french"
##    }
##
##countries = [bangladesh, india, china, australia, england, wales, france]
##
##for country in countries[:2]:
##    for key, value in country.items():
##        print(key, value)

#make an empty list for storing aliens
##aliens = []
##
### make 30 green aliens
##for alien_number in range(30):
##    alien = {"color":"green", "points":5, "speed":"slow"}
##    aliens.append(alien)
##
####for alien in aliens[:5]:
####    print(alien)
####print("...")
####
####print("Total number of aliens: "+str(len(aliens)))
####
##
##for alien in aliens[:3]:
##    if alien["color"] == "green":
##        alien["color"] = "yellow"
##        alien["points"] = 10
##        alien["speed"] = "medium"
##    elif alien["color"] == "yellow":
##        alien["color"] = "red"
##        alien["points"] = 15
##        alien["speed"] = "fast"
##
##for alien in aliens[:5]:
##    print(alien)

##pizza = {
##    "crust":"thick",
##    "toppings":["mushrooms", "extra cheese", "chicken", "beef"]
##    }
##
##print(pizza)
##
##mission_impossible = {
##    "type":"action",
##    "actors":["tom cruise", "jon voight", "jean reno", "ving rhames", "henry czemy"],
##    "actress":["emmanuelle beart", "vanessa redgrave", "ingebora dapkunaite"],
##    "sequel": "mission impossible 2"
##    }
##
##for actor in mission_impossible["actors"]:
##    print(actor.title())

fav_langs = {
    "sudipta":["java", "delphi", "javascript", "python"],
    "ridwan":["c", "c++"],
    "silvia":["javascript", "html"],
    "bob":["r", "matlab"],
    "megan":["ruby", "c", "php"],
    "kelly":["shell"],
    "mom":[]
    }

for name, langs in fav_langs.items():
    numLangs = len(langs)
    if(numLangs > 0):
        if(numLangs > 1):
            print(name.title() + "'s favorite languages are:")
        else:
            print(name.title() + "'s favorite language is:")
        for lang in langs:
            print("\t"+lang.title())
    else:
        print(name.title() + " does not have any favorite language.")
        















