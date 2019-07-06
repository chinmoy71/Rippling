def CheckInput(param, param1):
    wage_range_hour = range(10, 100)
    day_wage_range = range(70, 600)
    wage_range_weekly = range(300, 3000)
    wage_range_monthly = range(1200, 12000)
    wage_range_year = range(14000, 140000)
    Type_lable_match_dictonary = \
        {
            'Hourly Wage': 'HOUR',
            'Daily Wage': 'DAY',
            'Weekly Wage': 'WEEK',
            'Monthly Salary': 'MONTH',
            'Annual Salary': 'YEAR'
        }
    Label_validation_match_dictonary = \
        {
            'Hourly Wage': wage_range_hour,
            'Daily Wage': day_wage_range,
            'Weekly Wage': wage_range_weekly,
            'Monthly Salary': wage_range_monthly,
            'Annual Salary': wage_range_year
        }

    for keys, value in Type_lable_match_dictonary.items():
        if value == param:
            keys = keys
            for key, values in Label_validation_match_dictonary.items():
                if param1 in values and key == keys:
                    print('{} is valid'.format(keys))
                    break
                else:
                    if keys == keys and param1 not in values:
                        print('{} is invalid'.format(keys))
                        break
                    else:
                        pass
                        continue

print(CheckInput('HOUR', 80))



