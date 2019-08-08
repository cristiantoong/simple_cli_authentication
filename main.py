from models import Users, UserAccount

user_account = UserAccount()

def register(username, password):
  user = Users(username, password)
  user_account.signup(user)
  print('Successfully registerered!')



def login(username, password):
  for account in user_account.accounts:
    if password == account['password'] and username == account['username']:
      return 'You are now logged In!'
  return "Sorry account does not exist, register if you don't have an account yet."

 


def menu():
  choice = input("""
  1.) r - register
  2.) l - login
  3.) d - display user account data
  4.) cp - forgot/change password?
  5.) s - save user account data
  6.) q - quit
  """)
  while choice != 'q':
    if choice == 'r':
      username1 = input('Enter Username: ')
      password1 = input('Enter Password: ')
      if username1 != '' and password1 != '':
        register(username1, password1)
      else:
        print('Please input Username or Password')
    elif choice == 'l':
      username = input('Enter Username: ')
      password = input('Enter Password: ')
      print(login(username, password))
    elif choice == 'd':
      user_account.view_accounts()
    elif choice == 'cp':
      username = input('Enter Username: ')
      old_password = input('Enter Old Password: ')
      new_password = input('Enter New Password: ')
      print(user_account.change_password(username, new_password, old_password))
    elif choice == 's':
      user_account.save()
    elif choice == 'q':
      break
    choice = input("""
  1.) r - register
  2.) l - login
  3.) d - display user account data
  4.) cp - forgot/change password?
  5.) s - save user account data
  6.) q - quit
  """)

menu()