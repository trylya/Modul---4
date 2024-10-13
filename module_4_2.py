def test_function ():

    def inner_function ():
     print("Я в области видимости функции test_function")
    inner_function()
test_function()

# inner_function ()
#     def inner_function ():
#     ^
# IndentationError: expected an indented block after function definition on line 1

