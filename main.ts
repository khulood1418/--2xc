let name = "khulood"
basic.showString("khulood")
let grade = 1
basic.showNumber(1)
basic.forever(function on_forever() {
    function on_button_pressed_a() {
        basic.showString("Hello!" + name)
    }
    
    input.onButtonPressed(Button.A, on_button_pressed_a)
    function on_button_pressed_b() {
        basic.showNumber(1)
    }
    
    input.onButtonPressed(Button.A, on_button_pressed_a)
    input.onGesture(Gesture.Shake, function on_gesture_shake2() {
        basic.showIcon(IconNames.Heart)
        
    })
})
