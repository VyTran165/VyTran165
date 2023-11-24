class User:
    def __init__(self, age):
        self.age = age
        if self.age is None:
            self.age_input()

    def age_input(self):
        self.age = int(input("Enter your age: "))

    def can_vote(self):
        return self.age >= 18

    def retirement_years(self, retirement_age=65):
        if self.age < retirement_age:
            return retirement_age - self.age
        else:
            return 0
    def __str__(self):
        return (f"Your age: {self.age}, you can vote:{self.can_vote()}"
                f", you will retire in {self.retirement_years()} years")

if __name__ == '__main__':
    user_instance = User(None)
    print(user_instance)



