#Input
child_data = {
    "name": input("Name of the child : "),
    "age": int(input("Age of the child : ")),
    "gender": input("Gender of the child : "),
    "height_inches": int(input("Height of the child (in inches) : ")), #in inches
    "weight_pounds": int(input("Weight of the child (in pounds) : ")) #in pounds
}

food_consumed = {
    "Milk": int(input("Milk consumed by the child (in grams) : ")), 
    "Egg": int(input("Egg consumed by the child (in grams) : ")), 
    "Rice": int(input("Rice consumed by the child (in grams) : ")), 
    "Vegetable": int(input("Vegetable consumed by the child (in grams) : ")), 
    "Meat": int(input("Meat consumed by the child (in grams) : ")), 
    "Lentils": int(input("Lentils consumed by the child (in grams) : "))
}

#Class
class Child:
    def __init__(self, name, age, gender, height_inches, weight_pounds):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height_inches
        self.weight = weight_pounds

    def calculate_bmi(self):
        bmi = (self.weight/(self.height**2))*703
        return bmi

    def get_bmi_categories(self, bmi):
        if bmi < 16:
            return "Severely underweight"
        elif 16 <= bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Healthy"
        elif 25 <= bmi < 30:
            return "Overweight"
        elif 30 <= bmi:
            return "Obese"
        else:
            return "None"
        
    def get_daily_calorie_requirement(self):
        if 0 <= self.age <= 2:
            return 800
        elif 2 < self.age <= 4:
            return 1400
        elif 4 < self.age <= 8:
            return 1800
        else:
            return None

    def calculate_daily_calories_consumed(self, food_items):
        calorie_dict = {
            "Milk": 100,
            "Egg": 155,
            "Rice": 130,
            "Lentils": 113,
            "Vegetable": 85,
            "Meat": 143
        }
        
        total_calories = 0
        for food, quantity in food_items.items():
            if food in calorie_dict:
                total_calories += (calorie_dict[food] * quantity / 100)
        return total_calories

    def check_nutrition_status(self, daily_calories_consumed):
        recommended_calories = self.get_daily_calorie_requirement()
        if recommended_calories is not None:
            if daily_calories_consumed < recommended_calories:
                return f"Child is undernourished and recommended calories is {recommended_calories} "
            else:
                return "Well-nourished"
        else:
            return "Calorie requirement of your age is not defined"
        
#Assigning class into variables
child = Child(**child_data)
bmi = child.calculate_bmi()
bmi_categories = child.get_bmi_categories(bmi)
daily_calories_consumed = child.calculate_daily_calories_consumed(food_consumed)
nutrition_status = child.check_nutrition_status(daily_calories_consumed)

#Output
print(f"Child's BMI: {bmi:.2f}")
print(f"BMI Category: {bmi_categories}")
print(f"Child's Daily Calorie Consumption: {daily_calories_consumed:.2f} cal")
print(f"Nutrition Status: {nutrition_status}")
