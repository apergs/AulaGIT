#Escreva um código em Python que peça a temperatura em graus Fahrenheit e converta em graus Celsius.
#Considerando a seguinte fórmula: c = 5 * ((f-32) / 9)

f = float (input('Informe a temperatura em graus Fahrenheit: '))
c = 5 * ((f-32) / 9)

print('A temperatura {}° Fahrenheit é igual a {}° Celsius '.format (f, "%.2f" % c))
