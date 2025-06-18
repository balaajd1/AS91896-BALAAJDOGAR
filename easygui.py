import easygui
import easygui.enterbox
min_age = 18
def get_age():
    user_age = easygui.
if user_age < min_age:
    easygui.msgbox("Too young")
elif user_age == min_age:
    print("U can use this u are just of age")
else:
    print("Enjoy")

