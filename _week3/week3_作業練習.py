# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:48:03 2023

@author: User
"""

books = [
    {"書籍1": {"價格": 100, "庫存": 10}},
    {"書籍2": {"價格": 200, "庫存": 2}},
    {"書籍3": {"價格": 300, "庫存": 8}},
    {"書籍4": {"價格": 150, "庫存": 3}}
]

def exist_books(books_name):
    for book in books:
        if books_name in book:
            return True
    return False

def add_books():
    books_name = input("請輸入增加的書籍名稱:")
    books_count = int(input("請輸入增加的書籍數量:"))
    if exist_books(books_name):
        for book in books:
            if books_name in book:
                book[books_name]['庫存'] += books_count
    else:
        books_price = int(input('請輸入書籍價格:'))
        new_book = {books_name: {'價格': books_price, '庫存': books_count}}
        books.append(new_book)
    print(f'\n書籍:"{books_name}"已成功添加至庫存！\n')

def remove_books():
    books_name = input("請輸入要移除的商品名稱:")
    if exist_books(books_name):
        books_count = int(input("請輸入要移除的商品數量:"))
        for book in books:
            if books_name in book:
                book[books_name]['庫存'] -= books_count
                if 'remove' in book[books_name]:
                    book[books_name]['remove'] += books_count
                else:
                    book[books_name]['remove'] = books_count
                print(f'\n書籍:"{books_name}"已成功從庫存中移除！\n')
    else:
        print(f"\n找不到書籍'{books_name}'，移除失敗\n")

def update_books_count():
    books_name = input("請輸入欲更改庫存的書籍名稱:")
    if exist_books(books_name):
        books_count = int(input("請輸入新的庫存量:"))
        for book in books:
            if books_name in book:
                book[books_name]['庫存'] = books_count
                print(f'\n書籍:"{books_name}"的庫存已更新為{books_count}本！\n')
    else:
        print(f'\n找不到書籍"{books_name}"，更新失敗\n')

def select_a_book():
    book_name = input("請輸入欲尋找的書籍名稱:")
    found = False
    for book in books:
        for name, details in book.items():
            if book_name in name:
              print(f'\n找到以下資訊:')
              print(f'書名:{name}, 價格:{details["價格"]}元, 庫存:{details["庫存"]}本\n')
              found = True
    if not found:
        print(f"\n找不到書名為: '{book_name}' 的書籍\n")

def select_all_books():
    print("\n當前庫存:")
    for book in books:
        for name, details in book.items():
            print(f'書名:{name},價格:{details["價格"]}元,庫存:{details["庫存"]}本')
    print()
            
def main():
    f = True
    while f:
        print("請選擇一個功能:")
        print("1.增加書籍")
        print("2.移除書籍")
        print("3.更新書籍庫存")
        print("4.查詢單一書籍訊息")
        print("5.查詢所有書籍訊息")
        print("6.退出")

        choice = input("請輸入選擇的功能代碼(1/2/3/4/5/6):")

        if choice == '1':
            add_books()
        else:
            if choice == '2':
                remove_books()
            else:
                if choice == '3':
                    update_books_count()
                else:
                    if choice == '4':
                        select_a_book()
                    else:
                        if choice == '5':
                          select_all_books()
                        else:
                          if choice == '6':
                            print("\n感謝使用，再見！")
                            f = False
                          else:
                            print("請輸入有效的功能代碼")

if __name__ == '__main__':
    main()