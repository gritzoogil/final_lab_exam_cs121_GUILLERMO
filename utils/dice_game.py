import random
import os
from datetime import datetime

class DiceGame:
	def __init__(self, user_manager):
		self.user_manager = user_manager
		self.scores_folder = "data"
		self.scores_file = os.path.join(self.scores_folder, "rankings.txt")

		self.load_scores()

	def load_scores(self):
		if not os.path.exists(self.scores_folder):
			os.makedirs(self.scores_folder)
		
		if os.path.exists(self.scores_file):
			try:
				with open(self.scores_file, "r") as file:
					scores = [line.strip().split(',') for line in file.readlines()]
				return scores
			except IOError:
				print("Unable to load scores.")
				return []
		else:
			return []
		
	def save_scores(self, scores):
		try:
			with open(self.scores_file, "w") as file:
				for score in scores:
					file.write(','.join(map(str, score)) + '\n')
		except IOError:
			print("Unable to save score.")
			
	def play_game(self, username):
		total_points = 0
		total_stages_won = 0
		game_over = False
		tie_count = 0
		game_scores = self.load_scores()

		print(f"Starting game as {username}...")

		while not game_over:
			stage_points = 0

			for i in range(3):
				user_roll = random.randint(1, 6)
				computer_roll = random.randint(1, 6)

				print(f"{username} rolled {user_roll}")
				print(f"CPU rolled {computer_roll}")

				if user_roll > computer_roll:
					print(f"You win this round! {username}")
					stage_points += 1
				elif user_roll < computer_roll:
					print("CPU wins this round!")
					continue
				else:
					print("It's a tie!")
					tie_count += 1

			while tie_count == 3:
				user_roll = random.randint(1, 6)
				computer_roll = random.randint(1, 6)

				print(f"{username} rolled {user_roll}")
				print(f"CPU rolled {computer_roll}")

				if user_roll == computer_roll:
					print("It's a tie!")
				elif user_roll > computer_roll:
					print(f"You won this round! {username}")
					stage_points += 2
					total_points += stage_points - 1
					break
				else:
					print("CPU wins this round!")
					break

			if stage_points >= 2:
				print(f"You won this stage {username}!")
				total_stages_won += 1
				total_points += stage_points + 3
				stage_points = 0
				tie_count = 0
			elif stage_points == 0:
				print("Game over. You didn't win any stages.")
				game_over = True
			else:
				print(f"You lost this stage {username}")
				game_over = True

			print(username)
			print(f"Total points: {total_points}, Stages Won: {total_stages_won}")

			if not game_over:
				choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")
				while choice not in ('0', '1'):
					choice = input("Invalid input. Enter 1 to continue, 0 to stop: ")

				if choice == '0':
					print(f"Game over. You won {total_stages_won} stage(s) with a total of {total_points} points.")
					game_over = True

		if total_stages_won > 0:
			game_scores.append((username, total_points, total_stages_won))
			self.save_scores(game_scores)


	def show_top_scores(self):
		scores = self.load_scores()

		if scores:
			sorted_scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)  # Sort by points
			print("Top Scores:")
			for i, (username, points, wins) in enumerate(sorted_scores[:10], start=1):
				print(f"{i}. {username}: Points - {points}, Wins - {wins}")
		else:
			print("No games yet. Play a game to see top scores.")

	def logout(self):
		print("logout")

	def menu(self, username):
		while True:
			print(f"\nWelcome, {username}")
			print("Menu:")
			print("1. Start game")
			print("2. Show top scores")
			print("3. Log out")
			choice = input("Enter your choice or leave blank to cancel: ")
			if not choice:
				return
			else:
				try:
					choice = int(choice)
					if choice == 1:
						self.play_game(username)
					elif choice == 2:
						self.show_top_scores()
					elif choice == 3:
						self.logout()
					else:
						print("\nInvalid choice. Please try again.")
				except ValueError:
					print("\nInvalid choice. Please try again.")
		