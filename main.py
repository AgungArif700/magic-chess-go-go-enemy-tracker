data_musuh = []
#tahap pertama
enemy1 = input("Musuh Pertama :")
data_musuh.append(enemy1)

#tahap kedua
enemy2, enemy3 = input(f"Musuh Ke dua & dan Musuh {enemy1} di pisah oleh spaci  :").split()
data_musuh.append(enemy2)
data_musuh.append(enemy3)

#tahap ketiga
print(f"Musuh berikutnya {data_musuh[2]}")
input(f"Enter Jika sedang battle dengan melawan {data_musuh[2]}")

#tahap keempat
enemy4, enemy5 = input(f"Musuh Keempat & dan Musuh {enemy1} di pisah oleh spaci :").split()
data_musuh.append(enemy4)
data_musuh.append(enemy5)

#tahap kelima
print(f"\nMusuh berikutnya {data_musuh[4]}")
enemy6 = input(f"Musuh dari {data_musuh[2]} : ")
data_musuh.append(enemy6)

#tahap keenam
print(f"\nMusuh berikutnya {data_musuh[5]}")
input(f"Enter Jika sedang battle dengan melawan {data_musuh[5]}")

#tahap ketujuh
print(data_musuh)
enemy7 = input(f"Musuh Tersisa : ")
data_musuh.append(enemy7)

#tahap list musuh 
print("\n")
for e in data_musuh:
    print(e)