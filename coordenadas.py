import asyncio
from mavsdk import System
from mavsdk.action import OrbitYawBehavior
import sys

async def run():
    drone = System()

    try:
        await asyncio.wait_for(drone.connect(system_address="udp://:14540"), timeout=3)
    except asyncio.TimeoutError:
        print("Error: No se pudo conectar al dron dentro del tiempo especificado")
        file_path = "coordenadas.txt"  # Ruta del archivo
        with open(file_path, "a") as file:
            file.write("No se pudo conectar con el dron\n")
        return


    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone discovered!")
            break

    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break
        else
            file_path = "coordenadas.txt"  # Ruta del archivo
            with open(file_path, "a") as file:
                file.write("No se pudo acceder al gps\n")
            return

    async for position in drone.telemetry.position():
        orbit_height = position.absolute_altitude_m + 10
        break

    latitude = position.latitude_deg
    longitude = position.longitude_deg
    location_str = f"{latitude}, {longitude}"

    print(f"Ubicación: Latitud={latitude}, Longitud={longitude}")

    file_path = "coordenadas.txt"  # Ruta del archivo
    with open(file_path, "a") as file:
        file.write(location_str + "\n")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())