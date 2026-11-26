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

print("\n--- Prueba 4: Provocar error con batería negativa ---")
try:
    coche1.nivel_bateria = -25.0
    print("❌ FALLO: El sistema permitió asignar batería negativa.")
except ValueError as error:
    print(f"✅ ÉXITO: Bloqueado por el setter -> {error}")

print("\n--- Prueba 5: Provocar error reduciendo kilómetros ---")
try:
    coche1.kilometros_totales = 10.0 # Tenía 100 km acumulados
    print("❌ FALLO: El sistema permitió reducir el odómetro.")
except ValueError as error:
    print(f"✅ ÉXITO: Bloqueado por el setter -> {error}")
