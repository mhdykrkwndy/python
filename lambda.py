people=[
    {"name":"mahdi","house":"mobarekeh"},
    {"name":"sogand","house":"rafsanjan"},
    {"name":"mehran","house":"yazd"}
]

people.sort(key=lambda person:person["house"])
print(people)