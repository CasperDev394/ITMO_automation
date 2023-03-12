
# Задача №1

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2


rec_1 = Rectangle(2, 2)
rec_2 = Rectangle(4, 6)
rec_3 = Rectangle(10, 15)

print(f'Площади прямоугольников: '
      f'rec_1 = {rec_1.get_area()}, '
      f'rec_2 = {rec_2.get_area()}, '
      f'rec_3 = {rec_3.get_area()}')
print(f'Периметры прямоугольников: '
      f'rec_1 = {rec_1.get_perimeter()}, '
      f'rec_2 = {rec_2.get_perimeter()}, '
      f'rec_3 = {rec_3.get_perimeter()}')


# Задача 2
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)


# Задача 3
class Button:
    type = 'Кнопка'

    def __init__(self, text, loc=''):
        self.text = text

    def click(self):
        return f'Клик по кнопке {self.text}'


text_Box = Button('Text Box')
print(f'{text_Box.text}, {text_Box.click()}')

Check_Box = Button('Check Box')
print(f'{Check_Box.text}, {Check_Box.click()}')

Radio_Button = Button('Radio Button')
print(f'{Radio_Button.text}, {Radio_Button.click()}')

Web_Tables = Button('Web Tables')
print(f'{Web_Tables.text}, {Web_Tables.click()}')

Buttons = Button('Buttons')
print(f'{Buttons.text}, {Buttons.click()}')

Links = Button('Links')
print(f'{Links.text}, {Links.click()}')

Broken_Links_Images = Button('Broken Links - Images')
print(f'{Broken_Links_Images.text}, {Broken_Links_Images.click()}')

Upload_and_Download = Button('Upload and Download')
print(f'{Upload_and_Download.text}, {Upload_and_Download.click()}')

Dynamic_Properties = Button('Dynamic Properties')
print(f'{Dynamic_Properties.text}, {Dynamic_Properties.click()}')
