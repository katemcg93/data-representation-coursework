import requests
url = "http://andrewbeatty1.pythonanywhere.com/books"

def readbooks():
    response = requests.get(url)
    return response.json()

def get_avg_price ():
    bookdata = readbooks()
    prices = []
    for x in bookdata:
        prices.append(x["Price"])
    avg = sum(prices)/len(prices)
    return avg

def getbyid(id):
    get_url = url + "/" + str(id)
    response = requests.get(get_url)
    return response.json()

def new_book(book):
    response = requests.post(url, json = book)
    print(response)
    return response.json()

def update_book(id, book):
    update_url = url + "/" + str(id)
    response = requests.put(update_url, json = book)
    print(response)
    print(getbyid(id))
    return response.json()

def delete_book(id):
    delete_url = url + "/" + str (id)
    response = requests.delete(delete_url)
    print(response)
    print(getbyid(id))


if __name__ == "__main__":
    print(get_avg_price())


