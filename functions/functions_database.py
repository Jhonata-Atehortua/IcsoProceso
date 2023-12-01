import mysql.connector
from mysql.connector import Error

# Configurar la conexión a MySQL


def Conexion():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='icso',
            user='root',
            password='123456789'
        )

        if conn.is_connected():
            return conn

    except Error as e:
        print("Error:", e)
        return None


def CreacionTablas():
    conn = Conexion()
    if conn:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(
                "CREATE TABLE ActividadesEconomicas (id INT AUTO_INCREMENT PRIMARY KEY, codigo_opa INT, descripcion_opa VARCHAR(50), codigo_icso INT, descripcion_icso VARCHAR(50))"
            )
            cursor.execute(
                "CREATE TABLE activo (id INT AUTO_INCREMENT PRIMARY KEY, nit INT, primerapellido VARCHAR(100), segundoapellido VARCHAR(100), nombres VARCHAR(100), segundonombre VARCHAR(100), nombreintegrado VARCHAR(100), direccion VARCHAR(100), telefono1 VARCHAR(100), fechaingreso DATE, fechanacimiento DATE, coddepartamento INT, codciudad INT, codcomuna INT, barrio VARCHAR(100), estrato INT, celular VARCHAR(100), actividadeconomicaid INT, negocioid INT, valorsolicitado INT, montoaprobado INT, plazo INT, periodicidaddias INT, tasaefectiva FLOAT(10, 2), anualidad INT, cedulasociado INT, pagare INT, f_iniciofinanciacion DATE, capital INT, saldocapital INT, miembroid INT, nombre_cs VARCHAR(100), ced_prom INT, promotor VARCHAR(100), cod INT, ZONA VARCHAR(100), MUNICIPIO VARCHAR(100), cuenta VARCHAR(100), cooperativa VARCHAR(100), POLIZA VARCHAR(100), CORREO TEXT, ced_ben_1 VARCHAR(100), nom_beneficiario_1 VARCHAR(100), parentesco_1 VARCHAR(100), ced_ben_2 VARCHAR(100), nom_beneficiario_2 VARCHAR(100), parentesco_2 VARCHAR(100), ciclo INT, sexo VARCHAR(50), estado_civil VARCHAR(100), barrio_id_icso INT)"
            )
            conn.commit()
            cursor.close()
            conn.close()

def DepurarTablaClickActivo():
    conn = Conexion()
    if conn:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE activo SET estrato = 6 WHERE estrato IS NULL OR estrato > 6"
            )
            cursor.execute(
                "UPDATE activo SET correo = 'MICORREO@FOMENTAMOS.COM.CO' WHERE correo NOT LIKE '%@%' OR correo is null"
            )
            cursor.execute(
                "UPDATE activo SET telefono1 = NULL WHERE LENGTH(telefono1) != 7"
            )
            cursor.execute(
                "UPDATE activo SET celular = 9999999999 WHERE LENGTH(celular) != 10 or celular is null"
            )
            conn.commit()
            cursor.close()
            conn.close()
            return {"Estado": "La tabla del click activo ha sido depurada"}


def VerificarCodigoTablaClickActivo(CodigoOpa):
    conn = Conexion()
    if conn:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM activo WHERE cedulasociado = %s", (CodigoOpa,)
            )
            resultado = cursor.fetchall()

            cursor.close()
            conn.close()
            return len(resultado)


def RemplazarCodigoOpa_Icso(codigo_opa, codigo_icso, codigo_opa_rea):
    conn = Conexion()
    if conn:
        if conn.is_connected():
            cursor = conn.cursor()
            if codigo_opa_rea == None:
                cursor.execute(
                    "UPDATE activo SET cod = %s WHERE cedulasociado = %s", (
                        codigo_icso, codigo_opa)
                )
            else:
                cursor.execute(
                    "UPDATE activo SET cod = %s WHERE cedulasociado = %s OR cedulasociado = %s", (
                        codigo_icso, codigo_opa, codigo_opa_rea)
                )

            conn.commit()
            cursor.close()
            conn.close()
            return True

def LimpiarClickActivo():
    conn = Conexion()
    if conn:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("DELETE FROM activo")
            
            conn.commit()
            cursor.close()
            conn.close()

def EstructuraIcsoPromotor(CedulaPromotor):
    conn = Conexion()
    if conn:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM activo WHERE ced_prom = %s", (CedulaPromotor,)
            )

            Resultado = cursor.fetchall()

            conn.commit()
            cursor.close()
            conn.close()
            return Resultado

def ObtenerActividaEconomica(CodigoOpa):
    conn = Conexion()
    if conn:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(
                "SELECT codigo_icso FROM ActividadesEconomicas WHERE codigo_opa = %s",(CodigoOpa,)
            )
            Codigo_Icso = cursor.fetchall()[0][0]
            cursor.execute(
                "SELECT descripcion_icso FROM ActividadesEconomicas WHERE codigo_icso = %s",(Codigo_Icso,)
            )
            Descripcion_Icso = cursor.fetchall()[0][0]

            cursor.close()
            conn.close()
            return [Codigo_Icso,Descripcion_Icso]


def EstructuraModuloCedula(Cedula):
    conn = Conexion()
    if conn:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM activo WHERE nit = %s LIMIT 1", (Cedula,)
            )

            Resultado = cursor.fetchall()

            conn.commit()
            cursor.close()
            conn.close()
            return Resultado