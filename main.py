name = "khulood"
basic.show_string("khulood")
grade = 1
basic.show_number(1)

def on_forever():
    def on_button_pressed_a():
        basic.show_string("Hello!" + name)
    input.on_button_pressed(Button.A, on_button_pressed_a)
    def on_button_pressed_b():
        basic.show_number(1)
    input.on_button_pressed(Button.A, on_button_pressed_a)
    def on_gesture_shake2():
        basic.show_icon(IconNames.HEART)
        pass
    input.on_gesture(Gesture.SHAKE, on_gesture_shake2)
basic.forever(on_forever)
