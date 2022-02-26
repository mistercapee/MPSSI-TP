#Debut code python
#Deuxieme ligne
 
name = "ESMT"
age = 30
country = "Senegal"
Stack = {}

def holdInfoInStack(name : str , age : int , country : str, option : int):
    Stack[name.lower()] = [name, age, country, option]
    # print("Information is holded")

def divider(n = 20):
    print('-'*n)

def displayInfo(name : str, age : int , country : str) -> tuple:
    holdInfoInStack(name, age, country, 1)
    return name, age, country

def displayInfoByInput(name : str, age : int, country : str):
    holdInfoInStack(name, age, country, 2)
    return displayInfo(name, age, country)


if __name__ == "__main__":
    #Simulation One
    divider()
    name = "ESMT"
    age = 30
    country = "Senegal"
    print(displayInfo(name, age, country))
    print('\n')


    #Simulation 2
    divider(30)
    name2 = input("Enter a name : ")
    age2 = int(input("Enter a age : "))
    country2 = input("Enter a country : ")
    print(displayInfoByInput(name2, age2, country2))

