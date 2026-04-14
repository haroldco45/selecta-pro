"""
SelectaPro - Generador de Claves de Licencia
Vibras Positivas HM - Uso exclusivo del proveedor
"""
import base64

def generar_clave(empresa, fecha_vencimiento):
    """
    empresa: nombre de la empresa cliente
    fecha_vencimiento: 'YYYY-MM-DD'
    """
    raw = f'SELECTAPRO|{empresa}|{fecha_vencimiento}'
    return base64.b64encode(raw.encode()).decode()

def verificar_clave(clave):
    try:
        decoded = base64.b64decode(clave).decode()
        parts = decoded.split('|')
        if len(parts) == 3 and parts[0] == 'SELECTAPRO':
            return {'empresa': parts[1], 'vencimiento': parts[2]}
    except:
        pass
    return None

if __name__ == '__main__':
    print("=" * 55)
    print("  SelectaPro - Generador de Claves de Licencia")
    print("  Vibras Positivas HM")
    print("=" * 55)
    print()

    # Ejemplos de uso
    clientes = [
        ("Empresa Demo S.A.S.", "2026-12-31"),
        ("Distribuidora XYZ Ltda.", "2026-06-30"),
        ("Clinica San Pedro", "2027-03-31"),
    ]

    for empresa, fecha in clientes:
        clave = generar_clave(empresa, fecha)
        print(f"Empresa  : {empresa}")
        print(f"Vence    : {fecha}")
        print(f"Clave    : {clave}")
        # Verify
        v = verificar_clave(clave)
        print(f"Verif.   : {v}")
        print()

    # Modo interactivo
    print("-" * 55)
    print("Para generar una clave nueva, edita este archivo")
    print("y llama a: generar_clave('Empresa', 'YYYY-MM-DD')")
