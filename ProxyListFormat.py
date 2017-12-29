import sys

# Leer una lista de proxys con el formato ip:puerto y darle el formato
# <tipo> <ip> <puerto>
# para añadir a proxichains config.

ruta = sys.argv[1]
tipo_prox = sys.argv[2]

def ParsearArchivo(ruta_ar,tipo_p):
    # Abrir archivo en modo lectura
    print(ruta_ar)
    print(tipo_p)
    archivo_poxys = open(ruta_ar,'r')
    lineas_de_archivo = archivo_poxys.readlines()
    lista_proxys = []
    for x in lineas_de_archivo:
        cad = "{tipo} {ip} {puerto}"
        ip_prox = x.split(":")[0]
        puerto_prox = x.split(":")[1].strip("\n")
        proxy = cad.format(tipo=tipo_p, ip=ip_prox, puerto=puerto_prox)
        lista_proxys.append(proxy)
    return lista_proxys

lista_prox = ParsearArchivo(ruta,tipo_prox)

for proxy in lista_prox:
    print(proxy)
