#Importeer os module
import os

#huidige directory opvragen en opslaan in de variables
werkmap = os.getcwd()



print("De huidige map is: " + werkmap)

mapnaam=""

lengte_mapnaam = 0

while lengte_mapnaam == 0:
    mapnaam = input("Welke naam wil je voor je map?")

    lengte_mapnaam = len(mapnaam)

    if lengte_mapnaam >0:
        os.mkdir(mapnaam)
    else:
        print("Je hebt geen naam ingevoerd")

print("De map" + domdom + "is gemaakt")