import matplotlib.pyplot as plt

class Vuelo:
  def __init__(self, id_vuelo, asientos_vuelo):
    self.id_vuelo = id_vuelo
    self.asientos_vuelo = asientos_vuelo   #100
    self.asientos_vendidos = 0             #40 => 10 + 80 = 90
    self.asientos_cancelados = 0           #100
                                           #ven (90)-cancelados(100) >= 0

class Aerolinea:
  def __init__(self, nombre):
    self.nombre = nombre
    self.vuelos = []   # [Vuelo("a100", 100), Vuelo("a200", 200), Vuelo("a300", 300)..]

  #Metodos
  def registrar_vuelo(self,id_vuelo_i, asientos_vuelo_i):
    vueloTemporal = Vuelo(id_vuelo_i, asientos_vuelo_i)
    self.vuelos.append(vueloTemporal)

  def vender_asiento(self, id_vuelo_i, asientos_vendidos_i):
    existe = False
    for variableFor in self.vuelos:
      if variableFor.id_vuelo == id_vuelo_i:
        existe = True
        if variableFor.asientos_vendidos + asientos_vendidos_i <= variableFor.asientos_vuelo:
          variableFor.asientos_vendidos = variableFor.asientos_vendidos + asientos_vendidos_i
        else:
          print("No hay suficiente cantidad de asientos")
    if not existe:
      print("No se encontro el id de vuelo")

  def cancelar_asiento(self, id_vuelo_i, asientos_cancelados_i):
    existe = False
    for variableFor in self.vuelos:
      if variableFor.id_vuelo == id_vuelo_i:
        existe = True
        if variableFor.asientos_vendidos - asientos_cancelados_i >= 0:
          variableFor.asientos_vendidos -= asientos_cancelados_i
          variableFor.asientos_cancelados +=  asientos_cancelados_i
        else:
          print("No hay suficiente cantidad de asientos vendidos")
    if not existe:
      print("No se encontro el id de vuelo")

  def generar_graficos(self):
    id_vuelos = [variable.id_vuelo for variable in self.vuelos]
    #id_vuelos = ["a100","a200"]

    cant_asientos_v = [variable.asientos_vendidos for variable in self.vuelos]
    #id_vuelos = [80,190, 210]

    cant_asientos_c = [variable.asientos_cancelados for variable in self.vuelos]
    #id_vuelos = [40,300, 120]

    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.bar(id_vuelos, cant_asientos_v, color= 'blue')
    plt.title("Ventas por vuelo")
    plt.xlabel("Nombre del vuelo")
    plt.ylabel("Cantidad de asientos vendidos")

    # Ejemplo 1: Gráfico de barras agrupadas
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 3, 1)
    plt.bar(id_vuelos, cant_asientos_v, color='blue', label='Ventas')
    plt.bar(id_vuelos, cant_asientos_c, color='red', bottom=cant_asientos_v, label='Cancelaciones')
    plt.title('Ventas y Cancelaciones por Vuelo')
    plt.xlabel('Número de Vuelo')
    plt.ylabel('Cantidad')
    plt.legend()

    # Ejemplo 2: Gráfico de líneas
    plt.subplot(1, 3, 2)
    plt.plot(id_vuelos, cant_asientos_v, marker='o', label='Ventas', color='blue')
    plt.plot(id_vuelos, cant_asientos_c, marker='o', label='Cancelaciones', color='red')
    plt.title('Ventas y Cancelaciones por Vuelo (Líneas)')
    plt.xlabel('Número de Vuelo')
    plt.ylabel('Cantidad')
    plt.legend()

    # Ejemplo 3: Gráfico de torta
    plt.subplot(1, 3, 3)
    total_ventas = sum(cant_asientos_v)
    total_cancelaciones = sum(cant_asientos_c)
    totales = [total_ventas, total_cancelaciones]
    etiquetas = ['Ventas', 'Cancelaciones']
    colores = ['blue', 'red']
    plt.pie(totales, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=90)
    plt.title('Proporción de Ventas y Cancelaciones')



    plt.tight_layout()
    plt.show()


print("Aquí inicia nuestro programa")
latam = Aerolinea("LATAM")

while True:
  print("\nMenú de opciones")
  print("1. Registrar vuelo")
  print("2. Vender asiento")
  print("3. Cancelar asiento vendido")
  print("4. Generar graficos")
  print("5. Grafico de contabilidad")
  print("6. Grafico de ventas")
  print("7. Grafico de usuarios")
  print("8. Grafico de vuelos")
  print("9. Salir")
  opcion = int(input("Elige una opción: "))

  if opcion == 1:
    id_vuelo_input = input("Ingrese el número de vuelo")
    asientos_vuelo_input = int(input("Ingrese la cantidad de asientos del vuelo"))
    latam.registrar_vuelo(id_vuelo_input, asientos_vuelo_input)

  elif opcion == 2:
    id_vuelo_input = input("Ingresa el ID de vuelo")
    asientos_vendidos = int(input("Ingresa la cantidad de asientos a comprar: "))
    latam.vender_asiento(id_vuelo_input , asientos_vendidos)

  elif opcion == 3:
    id_vuelo_input = input("Ingresa el ID de vuelo")
    asientos_cancelados = int(input("Ingresa la cantidad de asientos a cancelar: "))
    latam.cancelar_asiento(id_vuelo_input , asientos_cancelados)

  elif opcion == 4:
    latam.generar_graficos()
  elif opcion ==5:
    print("Opción 5")
  elif opcion == 6:
    print("Opción 6")
  elif opcion == 7:
    print("Opción 7")
  elif opcion == 8:
    print("Opción 8")
  elif opcion == 9:
    break;
  else:
    print("Opción invalida!")

