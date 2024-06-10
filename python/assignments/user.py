class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("=======================")
        print(f"First Name : {self.first_name}")
        print(f"Last Name : {self.last_name}")
        print(f"Email : {self.email}")
        print(f"Age : {self.age}")
        print(f"Is reward member? : {self.is_reward_member}")
        print(f"Gold card points : {self.gold_card_points}")
        print("=======================")
        return self
    
    def enroll(self):
        if self.is_reward_member == True:
            print("User already a member")
        else: 
            self.is_reward_member = True
            self.gold_card_points = 200

    def spend_points(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points -= amount
        else:
            print("Not enough points to use!")

user_1 = User("Jihwan", "Eo","greation7@email.com", 31)
user_1.display_info()
user_1.enroll()
user_1.spend_points(10)
user_1.display_info()
user_1.enroll()
user_1.spend_points(200)
user_1.display_info()