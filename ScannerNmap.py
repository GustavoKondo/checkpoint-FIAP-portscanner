import nmap
import re


ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
porta_min = 0
porta_max = 65535

open_ports = []
# pergunta o ip alvo
while True:
    ip_digitado = input("\n  Coloque o endereço Ip que você deseja escanear :  ")
    if ip_add_pattern.search(ip_digitado):
        print(f"{ip_digitado} é um ip valido")
        break

while True:

    print("Por favor coloque o range de portas que você deseja escanear no formato: <port>-<port>")
    port_range = input("Coloque o range de portas: ")
    range_de_portas_validas = port_range_pattern.search(port_range.replace(" ",""))
    if range_de_portas_validas:
        porta_min = int(range_de_portas_validas.group(1))
        porta_max = int(range_de_portas_validas.group(2))
        break

nm = nmap.PortScanner()

for port in range(porta_min, porta_max + 1):
    try:
        result = nm.scan(ip_digitado, str(port))
        port_status = (result['scan'][ip_digitado]['tcp'][port]['state'])
        print(f"Porta {port} está {port_status}")
    except:
        print(f"não foi poossivel escanear {port}.")