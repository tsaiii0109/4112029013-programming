# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:43:15 2023

@author: User
"""

# 初始化空的圖書館書籍清單
library = []

# 創建一本新書並加入圖書館
def add_book(title,author,publication_date,ISBN,quantity):
    book = {
        "title":title,
        "author":author,
        "publication_date":publication_date,
        "ISBN":ISBN,
        "quantity":quantity
    }
    library.append(book)
    print(f"\n成功新增書籍：{title}")

# 借閱一本書且庫存-1
def borrow_book(title_or_ISBN):
    for book in library:
        if book["title"] == title_or_ISBN or book["ISBN"] == title_or_ISBN:
            if book["quantity"] > 0:
                book["quantity"] -= 1
                print(f"\n成功借閱書籍：{book['title']}")
                return
            else:
                print(f"\n書籍：{book['title']}的庫存不足")
                return
    print("\n未找到書籍或ISBN編號不正確")

# 歸還一本書且庫存+1
def return_book(title_or_ISBN):
    for book in library:
        if book["title"] == title_or_ISBN or book["ISBN"] == title_or_ISBN:
            book["quantity"] += 1
            print(f"\n成功歸還書籍：{book['title']}")
            return
    print("\n未找到書籍或ISBN編號不正確")

#查詢書籍資訊
def search_book(title_or_ISBN):
    for book in library:
        if book["title"] == title_or_ISBN or book["ISBN"] == title_or_ISBN:
            print(f"\n書名：{book['title']}")
            print(f"作者：{book['author']}")
            print(f"出版日期：{book['publication_date']}")
            print(f"ISBN編號：{book['ISBN']}")
            print(f"庫存數量：{book['quantity']}")
            return
    print("\n未找到書籍或ISBN編號不正確")




            
