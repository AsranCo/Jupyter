import requests



def process(url):
    response = requests.get(url)

    if (response.status_code != 200):
        return 'Bad Query'

    books = response.json()

    categories = list()
    for book in books:
        category = book['category']
        if category not in categories:
            categories.append(category)

    if len(categories) == 1:
        return categories[0]

    return "I can't recognize it"


print(process("https://mocki.io/v1/627ba115-0fdf-484e-8c98-fdc5a75d2a83"))