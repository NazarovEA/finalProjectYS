import sender_stand_request
# Назаров Евгений, — Финальный проект. Инженер по тестированию плюс
def get_numbers ():
    numbers = sender_stand_request.post_zakaz ()
    return numbers.json ()["track"]

# тест на статус 200
def test_order():
    numbers = get_numbers ()
    zakaz_response = sender_stand_request.get_zakaz (numbers)
    assert zakaz_response.status_code == 200
