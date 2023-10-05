# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:49:50 2023

@author: User
"""

#使用模組
import library_module as im

#主程式
def main():
    while True:
        print("\n圖書館管理系統")
        print("1. 新增書籍")
        print("2. 借閱書籍")
        print("3. 歸還書籍")
        print("4. 查詢書籍")
        print("5. 退出")
    
        choice = input("請選擇操作：")
        
        #使用者欲新增書籍
        if choice == "1":
            title = input("輸入書名：")
            author = input("輸入作者：")
            publication_date = input("輸入出版日期：")
            ISBN = input("輸入ISBN編號：")
            quantity = int(input("輸入庫存數量："))
            im.add_book(title,author,publication_date,ISBN,quantity)
        
        #使用者欲借閱書籍
        elif choice == "2":
            title_or_ISBN = input("輸入要借閱的書名或ISBN編號：")
            im.borrow_book(title_or_ISBN)
        
        #使用者欲歸還書籍
        elif choice == "3":
            title_or_ISBN = input("輸入要歸還的書名或ISBN編號：")
            im.return_book(title_or_ISBN)
        
        #使用者欲查詢書籍
        elif choice == "4":
            title_or_ISBN = input("輸入要查詢的書名或ISBN編號：")
            im.search_book(title_or_ISBN)
    
        #退出程式
        elif choice == "5":
            print("感謝使用，再見！")
            break
        
        #使用者輸入錯誤選項
        else:
            print("無效的選項，請重新選擇。")
main()