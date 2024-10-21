import numpy as np
import pandas as pd

def generar_reporte_ventas_por_categoria(df, categorias_unicas):
    
    # Revisar categorias
    categorias_unicas = np.unique(df['Product Category'])
    
    # 1. Calcular el total de ventas por categoría de producto
    ventas_totales = np.array([df[df['Product Category'] == categoria]['Total Amount'].sum() for categoria in categorias_unicas])

    # 2. Calcular el promedio de ventas por categoría de producto
    promedio_ventas = np.array([df[df['Product Category'] == categoria]['Total Amount'].mean() for categoria in categorias_unicas])

    # 3. Identificar la categoría con mayores y menores ventas
    categoria_mayor_ventas = categorias_unicas[ventas_totales.argmax()]
    categoria_menor_ventas = categorias_unicas[ventas_totales.argmin()]

    # Generar un reporte en formato string con los resultados
    reporte = f"""
    Reporte de Ventas por Categoría de Producto

    ---------------------------------------------
    1. Total de Ventas por Categoría de Producto:
    - {categorias_unicas[0]}: {ventas_totales[0]}
    - {categorias_unicas[1]}: {ventas_totales[1]}
    - {categorias_unicas[2]}: {ventas_totales[2]}

    ---------------------------------------------
    2. Promedio de Ventas Diarias por Categoría de Producto:
    - {categorias_unicas[0]}: {promedio_ventas[0]:.2f}
    - {categorias_unicas[1]}: {promedio_ventas[1]:.2f}
    - {categorias_unicas[2]}: {promedio_ventas[2]:.2f}

    ---------------------------------------------
    3. Categoría con Mayores Ventas:
    - {categoria_mayor_ventas}

    4. Categoría con Menores Ventas:
    - {categoria_menor_ventas}
    """

    # Mostrar el reporte en la consola
    print(reporte)
    return reporte

def operaciones_ventas_electronica(ventas_electronica):
    # 1. Suma: Total de ventas de productos de Electrónica
    total_ventas_electronica = ventas_electronica['Total Amount'].sum()

    # 2. Resta: Restar un valor de cada monto de venta
    resta_ventas_electronica = ventas_electronica['Total Amount'] - 10

    # 3. Multiplicación: Multiplicar la cantidad de productos vendidos por el precio por unidad
    multiplicacion_ventas_electronica = ventas_electronica['Quantity'] * ventas_electronica['Price per Unit']

    # 4. División: Dividir el monto total entre la cantidad vendida para obtener el precio promedio por producto
    division_ventas_electronica = ventas_electronica['Total Amount'] / ventas_electronica['Quantity']

    # Mostrar resultados de las operaciones
    print(f"Total de ventas de Electrónica: {total_ventas_electronica}")
    print(f"Ventas de Electrónica menos 10: \n{resta_ventas_electronica.head()}")
    print(f"Multiplicación (Cantidad * Precio por Unidad): \n{multiplicacion_ventas_electronica.head()}")
    print(f"División (Total / Cantidad para obtener el precio promedio): \n{division_ventas_electronica.head()}")

    # Devolver los resultados si es necesario en lugar de solo imprimirlos
    return {
        'total_ventas_electronica': total_ventas_electronica,
        'resta_ventas_electronica': resta_ventas_electronica,
        'multiplicacion_ventas_electronica': multiplicacion_ventas_electronica,
        'division_ventas_electronica': division_ventas_electronica
    }