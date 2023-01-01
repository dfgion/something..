from datetime import date 
from application import salary as s
from application.db import people as p


if __name__ == "__main__":
    print(date.today())
    print(s.calculate_salary())
    print(p.get_employees())
