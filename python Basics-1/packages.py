import random

for i in range(0,3,1):
    print(random.random())
    print(random.randint(10,20))


members=["srinivas","krishanth","jithendra","hasan"]
leader=random.choice(members)
print(leader)
