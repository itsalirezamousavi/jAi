import requests

def image(query):
    try:
        count = 3
        unsplash = 'https://api.unsplash.com/search/photos/?client_id=RimcLCvwd-6-O6XfpAJil8YlFYYpOyAlP2nrGhbXKzk'
        payload = {'query': query + ' city', 'per_page': count}
        r = requests.get(unsplash, params=payload)
        rdict = r.json()

        images_url = dict({
                    }
                    )

        for i in range(count):
            images_url[i] = rdict['results'][i]['urls']['regular']

        return images_url
    except:
        return None

print(image('londom'))