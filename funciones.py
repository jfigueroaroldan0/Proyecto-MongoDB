import pymongo
from datetime import datetime

def obtener_coleccion():
    try:
        cliente = pymongo.MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=2000)
        
        db = cliente['ciberseguridad']
        coleccion = db['vulnerabilidades']
        cliente.admin.command('ping')
        print("Conexión exitosa a MongoDB.")

        return coleccion
    
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

def insertar_vuln(col):

    cve = input("CVE ID: ")
    nombre = input("Producto: ")
    vendor = input("Fabricante: ")

    try:
        score = float(input("Puntuación (0-10): "))

    except ValueError:
        score = 0.0

    doc = {
        "cveID": cve,
        "vulnerabilityName": nombre,
        "vendorProject": vendor,
        "cvssV3BaseScore": score,
        "isPatched": False,
        "affectedVersions": ["v1.0"],
        "mitigationDetails": {"requiresReboot": False}
    }
    res = col.insert_one(doc)
    print(f"Insertado ID: {res.inserted_id}")

def eliminar_vuln(col):

    cve = input("CVE ID a eliminar: ")
    res = col.delete_one({"cveID": cve})
    print(f"Eliminados: {res.deleted_count}")

def modificar_vuln(col):

    cve = input("CVE ID a parchear: ")
    res = col.update_one({"cveID": cve}, {"$set": {"isPatched": True}})
    print(f"Modificados: {res.modified_count}")

def consulta_simple(col):

    print("\n--- Consultando: Ransomware (Campo Real) ---")
    cursor = col.find(
        {"knownRansomwareCampaignUse": "Known"}, 
        {"_id": 0, "cveID": 1, "vendorProject": 1}
    ).limit(5)
    for doc in cursor: print(doc)

def consulta_array(col):

    print("\n--- Consultando: Versiones (Requiere JSON Modificado) ---")
    cursor = col.find(
        {"affectedVersions": "v1.0"}, 
        {"_id": 0, "cveID": 1, "affectedVersions": 1}
    ).limit(5)
    for doc in cursor: print(doc)

def consulta_embebido(col):

    print("\n--- Consultando: Documentos Embebidos (Reinicio Requerido) ---")
    cursor = col.find(
        {"mitigationDetails.requiresReboot": True},
        {"_id": 0, "cveID": 1, "mitigationDetails": 1}
    ).limit(5)
    
    encontrados = False
    
    for doc in cursor:
        print(doc)
        encontrados = True
    
    if not encontrados:
        print("No se han encontrado documentos con campos embebidos.")

def consulta_agregacion(col):
    print("\n--- Consultando: Total por Fabricante ---")
    pipeline = [
        {"$group": {"_id": "$vendorProject", "total": {"$sum": 1}}},
        {"$sort": {"total": -1}},
        {"$limit": 5}
    ]
    for res in col.aggregate(pipeline):
        print(f"Fabricante: {res['_id']} | Total: {res['total']}")

def menu():
    coleccion = obtener_coleccion()
    if coleccion is None: 
        return

    menu = """
==========================================
   GESTOR DE VULNERABILIDADES (CISA)
==========================================
1. Añadir vulnerabilidad
2. Eliminar vulnerabilidad
3. Marcar como parcheada
4. Consulta Simple (Severas)
5. Consulta Array (Versiones)
6. Consulta Embebido (Reinicio)
7. Consulta Agregación (Estadísticas)
8. Salir
==========================================
Selecciona una opción: """

    opcion = 0
    while opcion != "8":
        try:
            opcion = input(menu)
            
            if opcion == '1':
                insertar_vuln(coleccion)

            elif opcion == '2':
                eliminar_vuln(coleccion)

            elif opcion == '3':
                modificar_vuln(coleccion)

            elif opcion == '4':
                consulta_simple(coleccion)

            elif opcion == '5':
                consulta_array(coleccion)

            elif opcion == '6':
                consulta_embebido(coleccion)

            elif opcion == '7':
                consulta_agregacion(coleccion)

            elif opcion == '8':
                print("Saliendo del sistema...")

            else:
                print("Opción no válida. Intenta de nuevo.")

        except:
            print("Introduzca una opción")