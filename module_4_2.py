def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

inner_function() # Эта функция находится внутри функции test_function
                 # и не видима из общей программы. Что приводит к ошибке:
                 # NameError: name 'inner_function' is not defined.
                 # Did you mean: 'test_function'?
test_function()