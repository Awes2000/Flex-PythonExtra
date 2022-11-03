import os

bestand = open("test.txt", "w")
bestand.write("Test 1,2,3!")
bestand.write("2e test")
bestand.close()

bestand2 = open("test.txt", "r")

bestand3 = open("klasgenoten.txt")
bestand3.write("Eugene", "Clement", "Davey", "Jonas", "Sam", "Robert", "Keith", "Bente", "Mucahid", "Gio")

