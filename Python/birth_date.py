from datetime import datetime, timedelta
def calculate_age(birth_date):
    current_date = datetime.now()
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    age = current_date - birth_date
    years = age.days // 365
    remaining_days = age.days % 365
    months = remaining_days // 30
    days = remaining_days % 30
    day_of_week = birth_date.strftime("%A")
    return years, months, days, day_of_week

user_birth_date = input("Wprowadz date urodzenia w podanym formacie (YYYY-MM-DD): ")
years, months, days, day_of_week = calculate_age(user_birth_date)
print("Od tej daty uplynelo: " + str(years) + " lat, " + str(months) + " miesiecy, " + str(days) + " dni. Aktualny dzien tygodnia w ktorym sie urodziles: " + str(day_of_week))
