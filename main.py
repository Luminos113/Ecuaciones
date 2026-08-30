import math

def f(t, y):
    return y


t=0;
y=1;
h=0.2;
y_nueva = y + h * f(t, y) 

print("y actual:", y)
print("y nueva:", y_nueva)


while t < 1:
    y = y + h * f(t, y)
    t = t + h
    exacta = math.exp(t)
    error = abs(exacta - y)

  
    print(
        "t =", round(t, 1),
        "Euler =", round(y, 4),
        "Exacta =", round(exacta, 4),
        "Error =", round(error, 4)
    )