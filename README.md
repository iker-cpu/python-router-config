# Cisco Network Configuration Scripts 

Conjunto de scripts Python para automatizar la configuración de routers Cisco IOS mediante SSH usando la librería **Netmiko**. Proyecto de aprendizaje universitario sobre automatización de redes.

## Descripción General

Estos scripts demuestran cómo conectarse a dispositivos Cisco, consultar configuraciones y aplicar cambios de forma programática en lugar de manual.

## Scripts Incluidos

### 1. **cisco_interface_config.py**
Configura una interfaz física de un router Cisco.

**Qué hace:**
- Conecta a un router via SSH
- Obtiene lista de interfaces activas
- Accede a modo de configuración global
- Configura la interfaz GigabitEthernet 1 con descripción
- Verifica los cambios
- Guarda la configuración en memoria

### 2. **cisco_loopback_setup.py**
Crea múltiples interfaces loopback en un router.

**Qué hace:**
- Crea interfaz Loopback 0 con IP 10.0.0.1/24
- Genera dinámicamente 5 interfaces loopback adicionales (1-5)
- Asigna IPs secuenciales (10.0.1.1, 10.0.2.1, etc.)
- Verifica todas las interfaces creadas

**Caso de uso:**
- Simular múltiples subredes virtuales en un router
- Practicar routing dinámico


### 3. **multi_router_cisco.py**
Configura múltiples routers simultáneamente.

**Qué hace:**
- Conecta a 2 routers (192.168.176.130 y 192.168.176.131)
- Cambia hostname de cada uno
- Crea 6 interfaces loopback por router con IPs diferentes
- Cierra las conexiones ordenadamente

**Caso de uso:**
- Automatizar setup de laboratorios con varios dispositivos
- Evitar configuración manual repetitiva


## Instalación

### Requisitos
- Python 3.6+
- Acceso SSH a routers Cisco IOS

### Setup

1. **Clonar el repositorio**
   ```bash
   cd Redes
   ```

2. **Instalar dependencias**
   ```bash
   pip install netmiko
   ```

3. **Configurar routers (opcional si no tienes acceso SSH)**
   - Modifica las variables `host`, `username` y `password` en los scripts con tus credenciales
   - Asegúrate que los routers tengan SSH habilitado

## Uso

Ejecuta cualquier script directamente:

```bash
python cisco_interface_config.py
python cisco_loopback_setup.py
python multi_router_cisco.py
```

**Nota:** Los scripts imprimirán el estado actual y confirmaciones de cada comando ejecutado.

## Importante

- Reemplaza las direcciones IP y credenciales según tu laboratorio
- Estos scripts están diseñados para Cisco IOS
- No ejecutes en dispositivos en producción sin revisar primero

**Última actualización:** 2026
