// PLAY
input.onButtonPressed(Button.A, function () {
    tempo = control.millis()
    ligado = true
})
// RESET
input.onButtonPressed(Button.AB, function () {
    contador = 0
    tempo = control.millis()
})
// STOP
input.onButtonPressed(Button.B, function () {
    ligado = false
})
// INICIALIZAÇÃO
let tempo = 0
let contador = 0
let ligado = false
ligado = false
contador = 0
tempo = control.millis()
// AÇÃO PRINCIPAL
basic.forever(function () {
    if (ligado == true) {
        if (control.millis() - tempo > 1000) {
            contador += 1
            if (contador > 9) {
                contador = 0
            }
            tempo = control.millis()
        }
    }
    basic.showNumber(contador)
})
