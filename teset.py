from googlesearch import search

# to search
query = '"Python has many libraries that really help developers in creating very extraordinary applications."'

for j in search(query, tld="co.id", num=10, stop=10, pause=2):
    print(j)

#%%
word = "lkjskdjsljf fdsjflkds f flkdsjf lkds. dlksjfdkls lkjfdsj flkdsj  lkfdsj fkdls"
data = word.split(". ")
for i in data:
    var = '"' + i + '"'
    print(var)
