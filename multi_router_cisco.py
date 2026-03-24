from netmiko import ConnectHandler

# Lista de IPs de routers
lista_ip_routers = [f'192.168.176.{n}' for n in range(130, 132)]

listaDispositivos = []

# Crear diccionarios de conexión
for router in lista_ip_routers:
    device = {
        "device_type": "cisco_ios",
        "host": router,
        "username": "cisco",
        "password": "cisco123!",
    }
    listaDispositivos.append(device)

print(listaDispositivos)

# Nombres de routers y hosts
nombresRouter = [f'CSR1000v{i}' for i in range(1, 3)]
hosts = [1, 2]

# Conexión y configuración
for dev, nombre, host in zip(listaDispositivos, nombresRouter, hosts):
    conn = ConnectHandler(**dev)

    print("Entorno actual (EXEC):", conn.find_prompt())

    # Entrar a configuración global y cambiar hostname
    conn.config_mode()
    print("Entorno actual (config):", conn.find_prompt())
    print(conn.send_command(f"hostname {nombre}"))

    # Crear interfaces loopback
    for subred in range(0, 6):
        crear_loopback = [
            f"interface loopback {subred}",
            f"ip address 10.0.{subred}.{host} 255.255.255.0",
            f"description Interfaz Loopback {subred} {nombre}"
        ]
        print(conn.send_config_set(crear_loopback))

    # Verificación
    print(conn.send_command("show ip interface brief"))

    # Cerrar conexión
    print("Cerrando conexión...")
    conn.disconnect()