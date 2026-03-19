import requests


def buscar_noticias(query):
    
    url = "https://newsapi.org/v2/everything"

    params = {
        "q":query,
        "apiKey":"c60665da20b145a78379987efc611e89"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return  data.get("articles" , [])
    















buscar_noticias("chile")










