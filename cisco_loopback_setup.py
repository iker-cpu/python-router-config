from netmiko import ConnectHandler

# Datos de conexión al dispositivo
device = {
    "device_type": "cisco_ios",
    "host": "192.168.176.130",
    "username": "cisco",
    "password": "cisco123!",
}

# Conexión SSH
conn = ConnectHandler(**device)

print("Entorno actual:", conn.find_prompt())

# Configurar Loopback0
crear_loopback0 = [
    "interface loopback 0",
    "ip address 10.0.0.1 255.255.255.0",
    "description Interfaz Loopback0 CSR1000v",
    "no shutdown"
]

print(conn.send_config_set(crear_loopback0))
print(conn.send_command("show ip interface brief"))

# Crear múltiples loopbacks
for n in range(1, 6):
    crear_loopback = [
        f"interface loopback {n}",
        f"ip address 10.0.{n}.1 255.255.255.0",
        f"description Interfaz Loopback{n} CSR1000v",
        "no shutdown"
    ]
    print(conn.send_config_set(crear_loopback))

print(conn.send_command("show ip interface brief"))

# Cerrar conexión
print("\nCerrando conexión....")
conn.disconnect()