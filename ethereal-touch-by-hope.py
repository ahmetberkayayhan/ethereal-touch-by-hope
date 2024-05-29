import random


class Character:
    def __init__(self):
        self.health = 100
        self.money = 1000
        self.smartness = 50
        self.charisma = 50
        self.happiness = 50
        self.job = None
        self.age = 20

    def age_up(self):
        self.age += 1
        print(f"Age: {self.age}")
        # Apply random changes to main stats
        money_change = random.randint(-200, -50)
        health_change = random.randint(-5, -1)
        smartness_change = random.randint(-5, -2)

        self.money += money_change
        self.health += health_change
        self.smartness += smartness_change

        # Ensure that stats do not drop below zero
        if self.money < 0:
            self.money = 0
        if self.health < 0:
            self.health = 0
        if self.smartness < 0:
            self.smartness = 0

    def get_job(self):
        jobs = [
            {"name": "Engineer", "salary": 5000, "satisfaction": 10, "improvement": 5, "intensity": 10,
             "reputation": 5},
            {"name": "Doctor", "salary": 7000, "satisfaction": 8, "improvement": 10, "intensity": 15, "reputation": 10},
            {"name": "Teacher", "salary": 4000, "satisfaction": 12, "improvement": 7, "intensity": 8, "reputation": 6}
            # You can add more jobs here
        ]
        self.job = random.choice(jobs)
        print(f"Your new job: {self.job['name']}")

    def quit_job(self):
        if self.job:
            print(f"You quit your job as a {self.job['name']}.")
            self.job = None
        else:
            print("You currently don't have a job.")

    def ask_for_raise(self):
        if self.job:
            success_chance = self.smartness + (self.job['intensity'])
            if random.randint(0, 100) < success_chance:
                self.job['salary'] += 1000
                print("You got a raise!")
            else:
                print("Your raise request was denied.")
        else:
            print("You currently don't have a job.")

    def work_hard(self):
        if self.job:
            self.job['intensity'] += 5
            print("You worked harder and the intensity increased.")
        else:
            print("You currently don't have a job.")

    def work_less(self):
        if self.job and self.job['intensity'] > 0:
            self.job['intensity'] -= 5
            print("You worked less and the intensity decreased.")
        else:
            print("You currently don't have a job or the intensity is already at minimum.")

    def exercise(self):
        self.money -= 50
        self.health += 3
        self.charisma += 1
        print("You exercised.")

    def play_games(self):
        self.money -= 30
        self.health -= 2
        self.happiness += 10
        print("You played games.")

    def study(self):
        self.money -= 40
        self.health -= 5
        self.smartness += 10
        print("You studied.")

    def show_stats(self):
        print(
            f"Health: {self.health}, Money: {self.money}, Smartness: {self.smartness}, Charisma: {self.charisma}, "
            f"Happiness: {self.happiness}")


def main():
    character = Character()

    while character.age < 100 & character.health > 0:  # The duration or end of the game can be determined
        character.age_up()
        character.show_stats()

        # Ask the user to choose multiple actions
        print(
            "Actions: 1- Get a job, 2- Quit job, 3- Ask for raise, 4- Work hard, 5- Work less, 6- Exercise, "
            "7- Play games, 8- Study")
        actions = input("Choose your actions (separated by commas): ").split(',')

        for action in actions:
            action = action.strip()
            if action == '1':
                character.get_job()
            elif action == '2':
                character.quit_job()
            elif action == '3':
                character.ask_for_raise()
            elif action == '4':
                character.work_hard()
            elif action == '5':
                character.work_less()
            elif action == '6':
                character.exercise()
            elif action == '7':
                character.play_games()
            elif action == '8':
                character.study()
            else:
                print("Invalid action.")

        # The game loop continues


if __name__ == "__main__":
    main()
