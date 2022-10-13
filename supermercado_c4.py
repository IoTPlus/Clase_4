productos = [
    #(id_producto, nombre, precio, cantidad_bodega)
    (41419, 'Fideos', 450, 210),
    (70717, 'Cuaderno', 900, 119),
    (78714, 'Jabon', 730, 708),
    (30877, 'Desodorante', 2190, 79),
    (47470, 'Yogur', 99, 832),
    (50809, 'Palta', 500, 55),
    (75466, 'Galletas', 235, 0),
    (33692, 'Bebida', 700, 20),
    (89148, 'Arroz', 900, 121),
    (66194, 'Lapiz', 120, 900),
    (15982, 'Vuvuzela', 12990, 40),
    (41235, 'Chocolate', 3099, 48),
]

clientes = [
    #(rut, nombre)
    ('11652624-7', 'Juan Perez'),
    ('8830268-0', 'Sebastian Casanueva'),
    ('7547896-8', 'Victor Gamonal'),
]

ventas = [
    #(num_boleta, fecha_venta, rut_cliente)
    (1, (2010, 9, 12), '8830268-0'),
    (2, (2010, 9, 19), '11652624-7'),
    (3, (2010, 9, 30), '7547896-8'),
    (4, (2010, 10, 1), '8830268-0'),
    (5, (2010, 10, 13), '7547896-8'),
    (6, (2010, 11, 11), '11652624-7'),
]

itemes = [
    #(num_boleta, id_producto, cantidad)
    (1, 89148, 3),
    (2, 50809, 4),
    (2, 33692, 2),
    (2, 47470, 6),
    (3, 30877, 1),
    (4, 89148, 1),
    (4, 75466, 2),
    (5, 89148, 2),
    (5, 47470, 10),
    (6, 41419, 2),
]

#Ejercicios en clase
#1
def producto_mas_caro(productos):
    l=len(productos)
    i=0
    mayor=0
    while i < l:
        if productos[i][2] > mayor:
            mayor = productos[i][2]
            mas_caro = productos[i][1]
        i+=1
    return mas_caro

print(producto_mas_caro(productos))

#2
def valor_total_bodega(productos):
    l = len(productos)
    i=0
    sum=0
    while i < l:
        sum = sum + productos[i][2]*productos[i][3]
        i+=1
    return sum

print(valor_total_bodega(productos))

#3
def ingreso_total_por_ventas(itemes, productos):
    l_itemes = len(itemes)
    l_productos = len(productos)
    i=0
    j=0
    suma=0
    while i < l_itemes:
        while j < l_productos:
            if itemes[i][1] == productos[j][0]:
                suma = suma + productos[j][2]*itemes[i][2]
            j+=1
        j=0
        i+=1
    return suma

print(ingreso_total_por_ventas(itemes,productos))

#Ejercicios extra
#4
def producto_con_mas_ingresos(itemes, productos):
    i=0
    j=0
    total_ventas = 0
    mayor_ingreso = 0
    producto=''
    while i < len(itemes):
        while j < len(productos):
            if productos[j][0] == itemes[i][1]:
                if (itemes[i][2]*productos[j][2]) > mayor_ingreso:
                    mayor_ingreso = itemes[i][2]*productos[j][2]
                    producto = productos[j][1]
            j+=1
        j=0
        i+=1
    return producto

print(producto_con_mas_ingresos(itemes, productos))

#5
def cliente_que_mas_pago(itemes, productos, clientes, ventas):
    i = 0
    j = 0
    total_boletas = []
    boleta = 0
    clientes_consumo = []
    while i < len(itemes):
        while j < len(productos):
            if itemes[i][1] == productos[j][0]:
                total_item = itemes[i][2] * productos[j][2]
                boleta = boleta + total_item
                if i < len(itemes) - 1:
                    if itemes[i][0] != itemes[i + 1][0]:
                        total_boletas.append(boleta)
                        boleta = 0
                elif i == len(itemes) - 1:
                    total_boletas.append(boleta)
                    boleta = 0
            j += 1
        j = 0
        i += 1
    for rut, nombre in clientes:
        k = 0
        total_cliente = 0
        while k < len(ventas):
            if rut == ventas[k][2]:
                total_cliente = total_cliente + total_boletas[ventas[k][0] - 1]
            k += 1
        clientes_consumo.append((rut, nombre, total_cliente))
    mayor = 0
    z = 0
    cliente_mayor_consumo = ''
    while z < len(clientes_consumo):
        if clientes_consumo[z][2] > mayor:
            mayor = clientes_consumo[z][2]
            cliente_mayor_consumo = clientes_consumo[z][1]
        z += 1
    return cliente_mayor_consumo

print(cliente_que_mas_pago(itemes, productos, clientes, ventas))

#6 Esta repetida, es la misma que la 3.

#7
def total_ventas_del_mes(año,mes,itemes,productos,ventas):
    i = 0
    total_mes = 0
    j = 0
    for num_boleta, fecha_venta, rut_cliente in ventas:
        if fecha_venta[1] == mes:
            while i < len(itemes):
                if itemes[i][0] == num_boleta:
                    while j < len(productos):
                        if productos[j][0] == itemes[i][1]:
                            precio_item = itemes[i][2] * productos[j][2]
                            total_mes = total_mes + precio_item
                        j += 1
                j = 0
                i += 1
        i = 0

    return(total_mes)

print(total_ventas_del_mes(2010,10,itemes,productos,ventas))

#8
def fecha_ultima_venta_producto(cod_producto,itemes,ventas):
    j = 0
    ultima_fecha = (0, 0, 0)
    for num_boleta, id_producto, cantidad in itemes:
        if id_producto == cod_producto:
            while j < len(ventas):
                if ventas[j][0] == num_boleta:
                    if ventas[j][1] > ultima_fecha:
                        ultima_fecha = ventas[j][1]
                j += 1
        j = 0
    return ultima_fecha

print(fecha_ultima_venta_producto(47470,itemes,ventas))
