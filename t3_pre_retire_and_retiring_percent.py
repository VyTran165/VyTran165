class User1:
    def __init__(self, age):
        self.age = age
        if self.age is None:
            self.age_input()

    def age_input(self):
        self.age = int(input("Enter your age: "))

    def pre_retire(self, pre_retire_age=60):
        if self.age < 60:
            return pre_retire_age - self.age
        else:
            return 0

    def retirement_percent(self, retirement_age=65):
        if self.age >= 60 and self.age < retirement_age:
            retire_percent = 60 + (self.age - 60) / (retirement_age - 60) * 40
        elif self.age < 60:
            retire_percent = 0
        else:
            retire_percent = 100
        return retire_percent

    def __str__(self):
        return (f"Your age: {self.age}, "
                f"You have {self.pre_retire()} years until pre-retirement, "
                f"retirement percent: {self.retirement_percent()}%")

if __name__ == '__main__':
    user_instance = User1(None)
    print(user_instance)