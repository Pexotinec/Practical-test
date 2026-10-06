from datetime import date
from email.utils import parseaddr

def validate_registration(email, birth_date):
errors = []

# Проверка email
if not email:
    errors.append("Введите email")
elif parseaddr(email)[1] != email or "@" not in email:
    errors.append("Введите корректный email")

# Проверка даты рождения
try:
    birth_date = date.fromisoformat(birth_date)

    if birth_date > date.today():
        errors.append("Дата рождения не может быть в будущем")

except (ValueError, TypeError):
    errors.append("Введите корректную дату рождения")

return errors

# Пример использования

email = "student@example.com"
birth_date = "2005-04-15"

errors = validate_registration(email, birth_date)

if errors:
    print("Регистрация не выполнена:")
    for error in errors:
        print("-", error)
else:
    print("Данные корректны. Можно продолжить регистрацию.")
