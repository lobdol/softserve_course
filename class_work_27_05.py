# names = ['Sam', 'Don', 'Daniel']
# for i in range(len(names)):
#     names[i] = hash(names[i])
# print(names)

names = ['Sam', 'Don', 'Daniel']
hash_name=map(hash, names)
print (list(hash_name))