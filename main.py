# PLAY

def on_button_pressed_a():
    global ligado
    ligado = True
input.on_button_pressed(Button.A, on_button_pressed_a)

# RESET

def on_button_pressed_ab():
    global ligado, contador
    ligado = False
    contador = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# STOP

def on_button_pressed_b():
    global ligado
    ligado = False
input.on_button_pressed(Button.B, on_button_pressed_b)

# INICIALIZAÇÃO
contador = 0
ligado = False
ligado = False
contador = 0
tempo = control.millis()
# AÇÃO PRINCIPAL

def on_forever():
    global contador, tempo
    if ligado == True:
        if control.millis() - tempo > 1000:
            contador += 1
            if contador > 9:
                contador = 0
            tempo = control.millis()
        basic.show_number(contador)
    else:
        basic.show_icon(IconNames.NO)
basic.forever(on_forever)

