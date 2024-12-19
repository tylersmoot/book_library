import pandas as pd
import datetime

current_time = datetime.datetime.now()
current_time_month = current_time.strftime('%m')
current_time_day = current_time.strftime("%d")
current_time_year = current_time.strftime('%Y')

current_time_hour = current_time.strftime('%I')
current_time_minutes = current_time.strftime('%M')
current_time_seconds = current_time.strftime('%S')

timestamp = current_time_hour + ': ' + current_time_minutes + ': ' + current_time_seconds

log_transaction = open('./database/library_transactions.txt', 'a')

books = pd.read_csv('./database/dataset.csv')
print(books.to_string())

print()

def showBooks():
   print(books.to_string())

user_input = ''
user_selection_check_in = ''


while(user_input != 0):
   
   user_input = int(input('Choose an option: \n'
                   '(1) Check Out A Book\n'
                   '(2) Check In A Book\n'
                   '(0) Exit\n'))

   
   if (user_input == 1):
      print('Which book would you like to check out?')
      showBooks()

      print()
      print('Choose a book id to check out')

      user_book_choice = int(input())
      found_book = books.loc[user_book_choice]
      print()
      print('****** Book Found: ******')
      print(found_book)

      found_book_status = books.loc[user_book_choice, 'status']
      found_book_title = books.loc[user_book_choice, 'title']
      found_book_id = books.loc[user_book_choice,'book_id']
      found_book_id = str(found_book_id)

      print()
      print(f'This book is currently: {found_book_status}')
      print()

      if(found_book_status != 'In'):
         print('This book is already checked out')
      
      else:
         user_confirmation = int(input(f'Confirm: Do you want to check {found_book_title} out?\n'
                              '(1) YES\n'
                              '(2) NO\n'))

         if (user_confirmation == 1):
            books.loc[user_book_choice, 'status'] = 'Out'
            books.to_csv('D:/python/projects/library/database/dataset.csv', index=False)
            showBooks()
            print()
            log_transaction.write('Occurence: Out,' + ' ' + 'Time: ' + timestamp + ', Book Title: ' + found_book_title + ', Book ID: ' + found_book_id + '\n')
            print('** TRANSACTIONS **')
            log_transaction = open('./database/library_transactions.txt', 'r')
            print(log_transaction.read())
            continue

         elif (user_confirmation == 2):
            break

   if(user_input == 2):
      showBooks()
      print('Which book would you like to check in?')
      user_book_choice = int(input())
      print(user_book_choice)
      found_book = books.loc[user_book_choice]
      found_book_status = books.loc[user_book_choice, 'status']
      found_book_title = books.loc[user_book_choice, 'title']
      found_book_id = books.loc[user_book_choice, 'book_id']
    
      
      
      print()
      print('****** Book Found: ******')
      print(found_book)
      print()
      
      user_confirmation = int(input(f'Confirm: Do you want to check {found_book_title} in?\n'
                              '(1) YES\n'
                              '(2) NO\n'))
      
      if (user_confirmation == 1):
         books.loc[user_book_choice, 'status'] = 'In'
         books.to_csv('D:/python/projects/library/database/dataset.csv', index=False)
        
         log_transaction.write('Occurence: In,' + ' ' + 'Time: ' + timestamp + ', Book Title: ' + found_book_title + ', Book ID: ' + found_book_id + '\n')
         print('** TRANSACTIONS **')
         log_transaction = open('./database/library_transactions.txt', 'r')
         print(log_transaction.read())
   

      continue

log_transaction.close()

