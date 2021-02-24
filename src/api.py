import http.client

conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "ae4bb96bf0msh746044ca17d0831p16e18ejsndda99fade3b8",
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
}

conn.request("GET", "/words/eat", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))