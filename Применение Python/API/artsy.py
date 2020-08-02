# Вам даны идентификаторы художников в базе Artsy. Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.

data = []
with open('input.txt') as f:
    for artists_id in f:
        artists_id = artists_id.rstrip()
        res = requests.get("https://api.artsy.net/api/artists/" + artists_id, headers=headers)
        tmpdata = json.loads(res.text)
        data.append((tmpdata['sortable_name'], tmpdata['birthday']))

data.sort(key=lambda i: (int(i[1]), i[0]))

for i in data:
    print(i[0])
