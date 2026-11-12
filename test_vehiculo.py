from vehiculo import Vehiculo

coche1 = Vehiculo("1234-BBB", "Urban-E", 40.0)
coche2 = Vehiculo("5678-FFF", "EcoVan", 75.0)

print("--- Estado inicial ---")
print(coche1.obtener_estado())
print(coche2.obtener_estado())

print("\n--- Prueba 1: Viaje de 100 km en coche1 ---")
coche1.conducir(100.0)
print(coche1.obtener_estado()) # Debe bajar su batería
print(coche2.obtener_estado()) # Debe seguir al 100% (objetos independientes)

print("\n--- Prueba 2: Recarga de prueba en coche1 ---")
coche1.recargar(10.0)
print(coche1.obtener_estado())

print("\n--- Prueba 3: Intento de sobrecarga (freno en 100%) ---")
coche1.recargar(100.0)
print(coche1.obtener_estado()) # Debe marcar exactamente 100.0%