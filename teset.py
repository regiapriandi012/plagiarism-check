from googlesearch import search

word = "jflkdsjf dsfkdsj flkdsjlkf dsjfklds jflkds jflkdsj flkdsj lkfjds fklds jkfdsjf dslkjflkds fkdsjlkf flkjdslkf dsflkds jfkdsfskdl."

data = word.replace("\n", " ").split(". ")
hasil = []
for i in data:
    query = '"' + i.strip().replace(".", "").replace('"', "'") + '"'
    for j in search(query, tld="co.id", num=10, stop=10, pause=2):
        hasil.append(j)

count = len(data)
count_hasil = len(hasil)
hasil_persen = (count_hasil / count) * 100
for i in range(len(hasil)):
    print('https://www.google.com/search?q="{}"'.format(data[i]).replace(" ", "%20"))
print(hasil_persen, "%")
