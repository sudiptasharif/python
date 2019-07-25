def show_magicians(magicians):
    """Prints name of each magician passed into the function as a list"""
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """Adds the phrase 'the great' to each magician's names and returns that list"""
    for i in range(len(magicians)):
        magicians[i] = "the great " + magicians[i]

    return magicians


magicians = ["bob", "ron", "harry", "katie", "nevile"]
great_magicians = make_great(magicians[:])

show_magicians(magicians)
show_magicians(great_magicians)
