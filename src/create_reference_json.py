import math
import json

from csv import DictReader


def get_books(file_path):
    books_list = []

    with open(file_path, newline='') as f:
        books = DictReader(f)

        for raw_book in books:
            book = {
                "title": raw_book['Title'],
                "author": raw_book['Author'],
                "pages": raw_book['Pages'],
                "genre": raw_book['Genre']
            }
            books_list.append(book)
    return books_list


def get_users(file_path):
    users_list = []
    with open(file_path, "r") as f:
        users = json.loads(f.read())
        for raw_user in users:
            user = {
                "name": raw_user["name"],
                "gender": raw_user["gender"],
                "address": raw_user["address"],
                "age": raw_user["age"],
                "books": []
            }
            users_list.append(user)
    return users_list


users = get_users("../data/users.json")
books = get_books('../data/books.csv')

cont_users = len(users)
count_books = len(books)
count_books_for_user = math.ceil(count_books / cont_users)
count_users_1 = count_books - ((count_books_for_user - 1) * cont_users)

i = 0
end = 0
for user in users:
    if count_users_1 == i:
        count_books_for_user -= 1

    start = end
    end = start + count_books_for_user
    i += 1
    slice_books = books[start:end]
    user['books'] = slice_books

with open("../data/result.json", "w") as file:
    s = json.dumps(users, indent=4)
    file.write(s)


