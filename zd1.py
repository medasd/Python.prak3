from datetime import datetime

def datetime_info(date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        
        formatted_date = date.strftime('%d-%m-%Y')
        
        day_of_week = date.strftime('%A')
        
        next_year = datetime(year=date.year + 1, month=1, day=1)
        days_until_next_year = (next_year - date).days
        
        return {
            'Дата': formatted_date,
            'День недели': day_of_week,
            'Дней до следующего года': days_until_next_year
        }
    except ValueError:
        return "неправильный формат даты. 'YYYY-MM-DD'."

date_str = input("Введите дату в формате 'YYYY-MM-DD': ")
print(datetime_info(date_str))
