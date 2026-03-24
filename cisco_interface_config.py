from netmiko import ConnectHandler

# Datos de conexión
device = {
    "device_type": "cisco_ios",
    "host": "192.168.176.130",
    "username": "cisco",
    "password": "cisco123!",
    "secret": "enable",   # modo privilegiado
    "port": 22
}

# Conexión
conn = ConnectHandler(**device)

print("Conectado como:", conn.find_prompt())

# Ver interfaces
output = conn.send_command("show ip interface brief")
print(output)

# Modo configuración global
print("\nAccedemos al modo de configuración global...")
conn.config_mode()
print("Entorno actual:", conn.find_prompt())

# Configuración de interfaz
print("\nAccedemos al modo de configuración de interfaz...")
conn.send_command(
    "interface GigabitEthernet 1",
    expect_string=r"CSR1kv\(config-if.*\)#"
)

print("Entorno actual:", conn.find_prompt())

# Configurar descripción
conn.send_command("description Interfaz Gi1 Host Only")

# Salir del modo interfaz
print("\nSaliendo del modo de configuración de la interfaz...")
conn.exit_config_mode()

print("Entorno actual:", conn.find_prompt())

# Verificar configuración
print("\n", conn.send_command("show running-config | section interface GigabitEthernet1"))

# Guardar configuración
print("\n", conn.send_command("write memory"))

# Cerrar conexión
print("\nCerrando conexión....")
conn.disconnect()