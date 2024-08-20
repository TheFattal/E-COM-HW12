import random

oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

# a:
oscar_winners.add("emma watson")
print("oscar_winners set is now:\n", oscar_winners)

# b:
oscar_winners.clear()
print("Oscar winners set is now:\n", oscar_winners)

# c:
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
oscar_winners_copy = oscar_winners.copy()
print("Oscar winners set is now:\n", oscar_winners)

# d:
oscar_winners.remove("Meryl Streep")
print("Oscar winners set is now:\n", oscar_winners)

# e:
# Method 1:
common_elements = titanic_actors & dark_knight_actors
print("Actors both in Titanic and Dark Knight are:\n", common_elements)
# Method 2:
common_elements = titanic_actors.intersection(dark_knight_actors)
print("Actors both in Titanic and Dark Knight are:\n", common_elements)

# f:
common_actors = iron_man_actors & avengers_actors
if common_actors:
    print("Yes! there are common actors to iron man and avengers!")
else:
    print("NO! there are no common actors to the 2 movies....")

# g:
if len(actor_list & oscar_winners) == len(actor_list):
    print("YES, all the actors in Actor_list won the oscar!")
else:
    print("NO! Not al the actors won the oscar... :< ")

# h:
if len(actor_list & avengers_actors) == len(avengers_actors):
    print("YES, all the actors in Avengers are in actor list!")
else:
    print("NO! Not al the actors are in the list... :< ")

# i:
random_actor_index: int = random.randint(0, len(movie_cast) - 1)
movie_cast_list: list = list(movie_cast)
random_actor_string = movie_cast_list[random_actor_index]
movie_cast_list.pop(random_actor_index)
movie_cast_after_pop = set(movie_cast_list)
print("The random actor this time is:\n", random_actor_string)
print("The new set movie_cast after removing is:\n", movie_cast_after_pop)

# j:
movie_cast.remove("Will Smith")
print("The new set movie_cast after removing Will Smith is:\n", movie_cast)

# k:
print("Titanic actors who didn't win the oscar prize are:\n", titanic_actors - oscar_winners)

# l:
print("Actors who preform in Titanic and Dark knight, but not both, are:")
print(titanic_actors | dark_knight_actors - (titanic_actors & dark_knight_actors))

# m:
oscar_winners.update({"Daniel Day-Lewis", "Cate Blanchett"})
print("Oscar winners after update are:\n", oscar_winners)

# n:
print("Actors both played in Titanic and dark knight are:", titanic_actors | dark_knight_actors)

# o:
dark_knight_rises_actors = {"Christian Bale", "Michael Caine", "Gary Oldman", "Tom Hardy", "Joseph Gordon-Levitt"}
if dark_knight_actors <= dark_knight_rises_actors:
    print("TRUE! The first actors were in the second movie too!")
else:
    print("FALSE! not all the players stayed for the second movie...")

# p:
if legendary_actors <= oscar_winners:
    print("TRUE! The legends got the oscar prize!")
else:
    print("FALSE! not all the legends won the oscar  :<")

# q:
print("The actors played in Avengers but not Iron man are:\n", avengers_actors - iron_man_actors)

# r:
print("Actors that played exclusively in dark night or Avengers are:\n", avengers_actors ^ dark_knight_actors)

# s:
print("Dark night and Iron man actors are:\n", dark_knight_actors | iron_man_actors)

# t:
frozen_legends = frozenset(legendary_actors)
