from googlesearch import search
f = open("word.txt", "r")
inputan_mentah = f.read()
inputan = inputan_mentah.replace("\n", " ").split(". ")
hasil_plagiarism = []
link_output = []
hasil_link = []
for i in range(len(inputan)):
    query = '"' + inputan[i].strip().replace(".", "").replace('"', "'") + '"'
    for j in range(len(list(search(query, tld="co.in", num=10, stop=10, pause=2)))):
        if i != j:
            continue
        hasil_link.append(inputan[i] + " " + list(search(query, tld="co.in", num=10, stop=10, pause=2))[j])
print(hasil_link)