# PYFORT

## Contributors : Jalil Bellahcen and Maël Prouteau (both responsible for the code, Jalil keeps the Readme.txt updated)

### A new kind of experience with this fort Boyard simulator, build your team and face many trials to take the win
### KEEP ALL THE DOCUMENTS TOGETHER THEY'RE ALL IMPORTANT (I SWEAR)

## Created in Python (libraries used : json,random)
#### To run the game, just run main.py

## Structure :
### This whole game is just a function, also made of functions :
#### 1. Introduction and creation of the team
#### While you do not have 3 keys
#### 2. The user chooses a player of the team
#### 3. The user can choose a category of game, and a random one from this category will be chosen
#### 4. In case of a win, the chosen player will get one key
#### 5. After obtaining 3 keys, the final challenge is enabled
#### 6. If the final challenge is completed, it's a win, and the team will be registered in a file


## Functions : (The ones that are useful outside this program)
### Math module :
####    -factorial(n : integer)--->integer : The function that returns the factorial of an integer n
####    -is_prime(n : integer)--->Boolean : #Check whether a number n is prime or not
####    -nearest_prime(n : integer)-->integer: a function that returns the nearest prime number to a number n
### Logical module :
####    -empty_grid() : Creates a matrix of " "
### Père Fouras' riddles module :
####    -load_ridles(file : string) : Load the content of file and put it in a list








## Logbook :
#### 2/12 : starting the project
#### 3/12 : Creating the first modules, maths module is done by Jalil
#### 6/12 : finished logic module by Jalil and chance module by Maël
#### 08/12 : starting the riddles module by Jalil
#### 10/12 : riddles module truly finished by Maël
#### 19/12 : finished final challenge module by Maël
#### 20/12 : documenting and optimising every module (everyone documented its own modules)
#### 20/12 : main.py done by Maël
#### 26/12 : Bug hunt and polishing the modules (adding ascii for example)


## known problems and/or solutions :
####    -There's no handling in case of an error of type e.g. entering a string instead of an integer
####    -Otherwise, all inputs, as long as they have the correct type, are correctly secured
####    (for example, if you're asked to enter a number between 0 and 3, you won't be able to put 4 or -1)