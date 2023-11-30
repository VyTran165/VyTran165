class User2:
    def __init__(self, age):
        self.age = age
        if self.age is None:
            self.age_input()

    def age_input(self):
        self.age = int(input("Enter your age: "))

    def can_vote(self):
        return self.age >= 18

    def can_drink(self):
        return self.age >= 21

    def __str__(self):
        return (f"Your age: {self.age}, you can vote:{self.can_vote()}"
                f", you can drink :{self.can_drink()}")

if __name__ == '__main__':
    user_instance = User2(None)
    print(user_instance)

