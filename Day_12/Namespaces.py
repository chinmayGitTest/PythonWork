#local and Global scopes
# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside the function : {enemies}")

# increase_enemies()
#print(f"enemies outside function : {enemies}")

#local scope (local scope exist within function)
#when you  create a new variable then there scope is only exisiting function only
# def drink_potion():
#     potion_strength =2
#     print(potion_strength)

# drink_potion()    
#print(potion_strnght)

#Global scope
# player_health= 10      #function define outside of the body
# def game():
#  def drink_potion():
#     potion_strength = 2
#     print(player_health)
#     drink_potion()

# print(player_health)

#There is no block scope

# game_level = 3
# enemies =["Skeleton","Zombi","Alien"]
# if game_level < 5:
#     new_enemey = enemies[0]

# print(new_enemey)

#Modifying global scope

# enemies =1

# def increase_enemies():
#     global enemies
#     enemies +=1
#     print(f"enemies inside the func ;{enemies}")

# increase_enemies()
# print(f"enemies outside the func ;{enemies}")

# #Global constants
# PI = 3.14
# def cal():
#     print(PI)

# def a_function(a_parameter):
#     a_variable = 15
#     return a_parameter
 
# a_function(10)
# print(a_variable)

i = 50
def foo():
    i = 100
    return i
 
foo()
print(i)