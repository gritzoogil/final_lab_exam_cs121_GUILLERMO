import os

class UserManager:
	def __init__(self):
		self.data_folder = "data"
		self.users_file = os.path.join(self.data_folder, "users.txt")

		self.load_users()

	def load_users(self):
		if not os.path.exists(self.data_folder):
			os.makedirs(self.data_folder)
		
		if os.path.exists(self.users_file):
			try:
				with open(self.users_file, "r") as file:
					users = [line.strip().split(',') for line in file.readlines()]
				return users
			except IOError:
				print("Unable to load users")
				return []
		else:
			return []


	def save_users(self, users):
		try:
			with open(self.users_file, "w") as file:
				for username, password in users:
					file.write(f'{username},{password}\n')
		except IOError:
			print("Unable to save users.")

	def validate_username(self, username, users):
		for user in users:
			if user[0] == username:
				return self.validate_password(username, user[1])
		return True

	def validate_password(self, username, password, users):
		for user in users:
			if user[0] == username and user[1] == password:
				return True
		return False
	
	def register(self):
		while True:
			existing_users = self.load_users()
			username = input("Enter username (at least 4 characters), or leave blank to cancel: ")
			if not username:
				return False

			if len(username) <= 4:
				print("Username must be at least 4 characters.")
				continue

			password = input("Enter a password (at least 8 characters), or leave blank to cancel: ")
			if not password:
				return False

			if len(password) <= 8:
				print("Password must be at least 8 characters.")

			if not self.validate_username(username, existing_users):
				print("Username already exists. Please choose a different one.")
				continue

			existing_users.append((username, password))
			self.save_users(existing_users)
			print(f"Welcome, {username}!")
			return True
		
	def login(self):
		print("login")

	