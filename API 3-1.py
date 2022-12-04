# В рамках этой задачи с помощью pytest необходимо написать тест, который просит ввести в консоли любую фразу короче 15 символов. А затем с помощью assert проверяет, что фраза действительно короче 15 символов.
# Чтобы в переменную получить значение, введенное из консоли, необходимо написать вот такой код:
# phrase = input("Set a phrase: ")
# Внимание, чтобы pytest не игнорировал команду ввода с клавиатуры, запускать тест нужно с ключиком "-s": python -m pytest -s my_test.py

class Test31:
    def test_phrase(self):
        phrase = input("Please enter a phrase no longer than 15 characters: ")
        assert 0 < len(phrase) <= 15, 'Your phrase has the wrong length! Please try again'
