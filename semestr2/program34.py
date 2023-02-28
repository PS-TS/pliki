import phonenumbers

phonenumbers.phone_numbers['David'] = '456-789-012'
del phonenumbers.phone_numbers['Charlie']
phonenumbers.phone_numbers['Anna'] = '111-222-333'
phonenumbers.print_phone_numbers(phonenumbers.phone_numbers)


def day_name_to_eng(day_name):
    days = {'poniedzialek': 'Monday', 'wtorek': 'Tuesday', 'sroda': 'Wednesday',
            'czwartek': 'Thursday', 'piatek': 'Friday', 'sobota': 'Saturday', 'niedziela': 'Sunday'}
    return days[day_name.lower()]

def day_name_to_pl(day_name):
    days = {'Monday': 'poniedzialek', 'Tuesday': 'wtorek', 'Wednesday': 'sroda',
            'Thursday': 'czwartek', 'Friday': 'piatek', 'Saturday': 'sobota', 'Sunday': 'niedziela'}
    return days[day_name]


print(day_name_to_pl("Tuesday"))