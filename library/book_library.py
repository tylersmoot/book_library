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

def showBooks():
   print('** LIBRARY **')
   print(books)


books = pd.read_csv('./database/dataset.csv')
showBooks()

print()

user_input = ''
user_selection_check_in = ''


while(user_input != 0):
   
   user_input = int(input('What would you like to do?\n\n'
                   '(1) Check Out A Book\n'
                   '(2) Check In A Book\n'
                   '(0) Exit\n'))

   
   if (user_input == 1):
      print('Which book would you like to check out?')

      showBooks()

      print()
      print('Choose a book ID to check OUT')

      user_book_choice = int(input())
      found_book = books.loc[user_book_choice]
      

      print()
      print('****** Book Found: ******')
      print(found_book)

      found_book_status = books.at[user_book_choice, 'status']
      found_book_title = books.at[user_book_choice, 'title']
      found_book_id = books.at[user_book_choice,'book_id']
     
      
      print()
      print(f'This book is currently: {found_book_status}')
      print()

      if(found_book_status != 'Out'):
         
     
         user_confirmation = int(input(f'Confirm: Do you want to check {found_book_title} out?\n\n'
                              '(1) YES\n'
                              '(2) NO\n'))

         if (user_confirmation == 1):
            books.loc[user_book_choice, 'status'] = 'Out'
            books.to_csv('D:/python/projects/library/database/dataset.csv', index=False)
            log_transaction = open('./database/library_transactions.txt', 'a')
            showBooks()
            print()
            log_transaction.write('Occurence: Out,' + ' ' + 'Time: ' + str(timestamp) + ', Book Title: ' + found_book_title + ', Book ID: ' + str(found_book_id) + '\n')
            print('** TRANSACTIONS **')
            log_transaction = open('./database/library_transactions.txt', 'r')
            print(log_transaction.read())
            break
         
            
            

         elif (user_confirmation == 2):
            break

   if(user_input == 2):
      showBooks()
      print('Choose a book ID to check IN')

      user_book_choice = int(input())
      found_book = books.loc[user_book_choice]
      found_book_status = books.at[user_book_choice, 'status']
      found_book_title = books.at[user_book_choice, 'title']
      found_book_id = found_book.at['book_id']
     
    
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
         log_transaction = open('./database/library_transactions.txt', 'a')
         log_transaction.write('Occurence: In,' + ' ' + 'Time: ' + str(timestamp) + ', Book Title: ' + str(found_book_title) + ', Book ID: ' + str(found_book_id) + '\n')
         print('** TRANSACTIONS **')
         log_transaction = open('./database/library_transactions.txt', 'r')
         print(log_transaction.read())
         break
       
   
log_transaction.close()
