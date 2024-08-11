def test_function():
    def inner_function():
        print ('Я в области видимости функции test_function')
    #inner_function() Не работает, не возвращает
#inner_function() Ошибка
#test_function() Работает