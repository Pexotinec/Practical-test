def register_user(name, email, existing_emails):
    errors = []

    # Проверка обязательных полей
    if not name:
        errors.append("Введите имя")

    if not email:
        errors.append("Введите email")
    elif "@" not in email or "." not in email:
        errors.append("Некорректный email")
    elif email in existing_emails:
        errors.append("Этот email уже зарегистрирован")

    if errors:
        return {"success": False, "errors": errors}

    return {"success": True, "message": "Регистрация успешна"}


# Примеры проверки
existing_emails = ["user@example.com"]

print(register_user("", "new@example.com", existing_emails))
print(register_user("Daniyar", "wrong-email", existing_emails))
print(register_user("Daniyar", "user@example.com", existing_emails))
print(register_user("Daniyar", "new@example.com", existing_emails))
