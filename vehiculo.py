class Vehiculo:
    """Molde que representa un vehículo eléctrico en el simulador municipal."""

    def __init__(self, matricula: str, modelo: str, capacidad_kwh: float):
        # Guardamos los datos recibidos dentro del propio objeto usando self
        self.matricula: str = matricula
        self.modelo: str = modelo
        self.capacidad_kwh: float = capacidad_kwh
        self.nivel_bateria: float = 100.0  # Comienza con la carga completa (%)
        self._kilometros_totales: float = 0.0

    @property
    def nivel_bateria(self) -> float:
        """Getter: Devuelve el porcentaje de batería actual."""
        return self._nivel_bateria

    @nivel_bateria.setter
    def nivel_bateria(self, nuevo_nivel: float) -> None:
        """Setter: Valida que el nivel se encuentre siempre en el rango [0.0, 100.0]."""
        if nuevo_nivel < 0.0 or nuevo_nivel > 100.0:
            raise ValueError(f"Nivel de batería inválido: {nuevo_nivel}%. Debe estar entre 0 y 100.")
        self._nivel_bateria = nuevo_nivel
    @property
    def kilometros_totales(self) -> float:
        return self._kilometros_totales

    @kilometros_totales.setter
    def kilometros_totales(self, nuevos_km: float):
        if nuevos_km < self._kilometros_totales:
            raise ValueError("Los kilómetros no pueden disminuir.")
        self._kilometros_totales = nuevos_km

    def conducir(self, distancia_km: float) -> bool:
        """Simula un trayecto urbano. Consume 0.15 kWh por cada km recorrido."""
        energia_necesaria = distancia_km * 0.15
        porcentaje_consumido = (energia_necesaria / self.capacidad_kwh) * 100.0
        # Comprobamos si la batería actual cubre el consumo
        if self.nivel_bateria >= porcentaje_consumido:
            self.nivel_bateria -= porcentaje_consumido
            self.kilometros_totales += distancia_km
            return True  # Trayecto realizado
        else:
            return False  # Batería insuficiente: no se mueve

    def obtener_estado(self) -> str:
        """Devuelve una ficha legible con la telemetría del vehículo."""
        return f"[{self.matricula}] {self.modelo} | Batería: {self.nivel_bateria:.1f}% | Total: {self.kilometros_totales} km"

    def recargar(self, energia_kwh: float) -> float:
        """Recarga la batería del vehículo. Devuelve la energía realmente cargada (kWh)."""
        porcentaje_recarga = (energia_kwh / self.capacidad_kwh) * 100.0
        if self.nivel_bateria + porcentaje_recarga > 100.0:
            porcentaje_recarga = 100.0 - self.nivel_bateria  # Solo recargamos hasta el máximo
        self.nivel_bateria += porcentaje_recarga
        energia_cargada = (porcentaje_recarga / 100.0) * self.capacidad_kwh
        return energia_cargada
class CocheElectrico(Vehiculo):
    """Subclase que representa un automóvil eléctrico de pasajeros."""

    def __init__(self, matricula: str, modelo: str, capacidad_kwh: float, plazas: int = 5):
        # 1. Delegamos en la superclase para inicializar los atributos comunes
        super().__init__(matricula, modelo, capacidad_kwh)
        # 2. Inicializamos el atributo exclusivo de esta subclase
        self.plazas: int = plazas

    def conducir(self, distancia_km: float) -> bool:
        """Consume 0.15 kWh por km recorrido."""
        if distancia_km < 0:
            return False

        energia_necesaria = distancia_km * 0.15
        porcentaje_consumido = (energia_necesaria / self.capacidad_kwh) * 100.0

        if self.nivel_bateria >= porcentaje_consumido:
            self.nivel_bateria -= porcentaje_consumido
            self.kilometros_totales += distancia_km
            return True
        return False

    def obtener_estado(self) -> str:
        """Sobreescribe obtener_estado() añadiendo las plazas del vehículo."""
        estado_base = super().obtener_estado()
        return f"{estado_base} | Plazas: {self.plazas}"

class PatineteElectrico(Vehiculo):
    """Subclase que representa un patinete eléctrico urbano."""

    def __init__(self, matricula: str, modelo: str, capacidad_kwh: float, velocidad_maxima: float = 25.0):
        # 1. Delegamos en la superclase para inicializar los atributos comunes
        super().__init__(matricula, modelo, capacidad_kwh)
        # 2. Inicializamos el atributo exclusivo de esta subclase
        self.velocidad_maxima: float = velocidad_maxima
        if self.velocidad_maxima >= 25:
            raise ValueError("La velocidad máxima legal en ciudad es 25 km/h.")

    def conducir(self, distancia_km: float) -> bool:
        """Consume 0.02 kWh por km recorrido."""
        if distancia_km < 0:
            return False

        energia_necesaria = distancia_km * 0.02
        porcentaje_consumido = (energia_necesaria / self.capacidad_kwh) * 100.0

        if self.nivel_bateria >= porcentaje_consumido:
            self.nivel_bateria -= porcentaje_consumido
            self.kilometros_totales += distancia_km
            return True
        return False



