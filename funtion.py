x = [ [5,2,3], [10,8,9] ] 

print("form 10 to 15")
x [1][0] = 15
print(x)






students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print("change the last name from jordan to bryant")

students[0]["last_name"] = "bryant"
print(students)
print(students[0]["last_name"])



sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

print("chage Messi to Andres")

sports_directory['soccer'][0] = "Andres"

print(sports_directory)
print(sports_directory['soccer'][0])


print("change the value 20 to 30")
z = [ {'x': 10, 'y': 20} ]
z[0]["y"]= 30

print(z)
print(z[0]["y"])








students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for item in some_list:
        for key in item:
            print(key)
            print(item[key])

names = iterateDictionary(students)



students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])

iterateDictionary2('first_name', students)

print("______________________________")


iterateDictionary2('last_name', students)





def printInfo(some_dict):
    for key in some_dict:
        print(key)
        somevar = some_dict[key] 
        print(len(somevar))
        for item in somevar:
            print(item)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
# output:
'''7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon'''
