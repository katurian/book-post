import pymongo
import requests
import json


def addBook(isbn):
    r = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}')
    bookJSON = r.json()['items'][0]['volumeInfo']

    title = bookJSON['title']
    try:
        year = int(bookJSON['publishedDate'])
    except:
        year = 'NA'
    
    author = bookJSON['authors'][0]
    description = bookJSON['description']

    client = pymongo.MongoClient('mongodb+srv://katskiUser:XXXXXX@folio-database.4q0uf.azure.mongodb.net/default')
    db = client['default']
    col = db['books']
    entry = {'title': title, 'year': year, 'author': author, 'description': description}
    col.insert_one(entry)

addBook('9780393325997')
