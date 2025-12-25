words = ['cat' , 'dog' , 'lemon' , 'kitten']

for item in words:
    print(item , len(item) , end="\n")
    
    
print("-------------------")

users = {'Alice' : 'active' , 'Bob' : 'inactive' , 'Charly' : 'inactive' , 'Dylan' : 'active'}

for user , status in users.copy().items():
    if status == 'inactve':
        del users[user]
        
#print(users.copy().items())      

active_users = {}
for active_user , active_status in users.items():
    if active_status == 'active':
        active_users[active_user] = active_status

print(active_users)
        
