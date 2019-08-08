import csv

class Users:
  def __init__(self, username, password):
    self.name = username
    self.username = username
    self.password = password

class UserAccount:
  user_count = 0
  def __init__(self):
    self.accounts = []

  def signup(self, account):
    self.accounts.append(account.__dict__)
    UserAccount.user_count += 1

  def view_accounts(self):
    for account in self.accounts:
      template = "NAME: {}, USERNAME: {}, PASSWORD: {}"
      name = account['name']
      username = account['username']
      password = account['password']
      print(template.format(name,username,password))
    return ''
    
  def view_user_count(self):
    return UserAccount.user_count

  def save(self):
    with open('data.csv', 'w') as f:
      fieldnames = ['name', 'username', 'password']
      writer = csv.DictWriter(f, fieldnames=fieldnames)
      writer.writeheader()
      for account in self.accounts:
        writer.writerow(account)

  def change_password(self, username, new_password, old_password):
    if any(username in account['username'] for account in self.accounts) and any(old_password in account['password'] for account in self.accounts):
        acc = next(account for account in self.accounts if account['password'] == old_password)
        acc['password'] = new_password
        return 'Password has changed'
    return "Password doesnt exists."
  def view_total_count_users(self):
      return 'Total number of users: {}'.format(UserAccount.user_count) 
