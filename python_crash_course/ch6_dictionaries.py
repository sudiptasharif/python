##alien_0 = {"color":"green", "point":5}
##print(alien_0)
##
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

alien = {}
alien["x"] = 0
alien["y"] = 25
alien["speed"] = "medium"
print("Original x-position: "+str(alien["x"]))

if alien["speed"] == "slow":
    x_inc = 1
elif alien["speed"] == "medium":
    x_inc = 2
else:
    x_inc = 3

alien["x"] = alien["x"] + x_inc
print("New x-position: "+str(alien["x"]))

