print("Equation is: ax^2 + bx + c = 0")
a = float(input("Enter a's value: "))
b = float(input("Enter b's value: "))
c = float(input("Enter c's value: "))
delta = b ** 2 - 4 * a * c
a_2 = a*2
if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh co vo so nghiem!")
        else:
            print("phuong trinh vo nghiem!")
    else:
        x = - c / b
        print("Phuong trinh la phuong trinh bac nhat")
        print("Phuong trinh co nghiem duy nhat la x =", x)
else:
    if delta < 0:
        print("Phuong trinh vo nghiem!")
    elif delta == 0:
        x = -b / a_2
        print("Phuong trinh co nghiem duy nhat la:", x)
    else:
        delta_sqrt = delta ** 0.5
        x1 = (-b+ delta_sqrt)/ a_2
        x2 = (-b- delta_sqrt)/ a_2
        print("Phuong trinh co hai nghiem phan biet la:", x1,"va", x2)
