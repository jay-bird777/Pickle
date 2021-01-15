import pickle

# 1. Leader Numbers

leaders = {}
leaders["Jacore"] = "845-200-6250"
leaders["Gabriel"] = "510-613-6288"
leaders["Aris"] = "510-229-6359"
leaders["Andrew"] = "925-727-4611"
leaders["Richard"] = "845-228-5623"

# 2. create/open pod_nbrs.pkl file
pod_file = open("pod_nbrs.pkl","wb")

# 3. Write leaders numbers
pickle.dump(leaders,pod_file)

# 4. members numbers
members = {}
members["Akari"] = "510-500-2206"
members["Morris"] = "925-286-5922"
members["Mousa"] = "415-717-8414"
members["Prince"] = "510-472-0804"

# 5. add number =s to file
pickle.dump(members,pod_file)

# 6. close pod_nbrs.pkl file
pod_file.close()

# 7.
pod_file = open("pod_nbrs.pkl","rb")

# 8.
print("Pod Leaders: ")
for key, value in leaders.items():
    print(key, value)
print("\n")

# 9
print("Pod Members: ")
for key, value in members.items():
    print(key, value)
print("\n")

# 10.
pod_file.close()
