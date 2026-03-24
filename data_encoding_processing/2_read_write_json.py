import json

data =  {
    'name' : 'Bill',
    'username' : 'Kill_Bill',
    'password' : '12345' 
}

data_str = json.dumps(data)
print(data_str)


with open("data2.json" , 'w') as f:
    json.dump(data , f)
    
with open('data2.json' , 'r') as f:
    data = json.load(f)
    