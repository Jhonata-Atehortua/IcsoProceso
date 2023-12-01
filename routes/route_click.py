from fastapi import APIRouter, File, UploadFile, HTTPException, Form
from fastapi.responses import FileResponse
from functions.functions_database import Conexion, DepurarTablaClickActivo, VerificarCodigoTablaClickActivo, RemplazarCodigoOpa_Icso, EstructuraIcsoPromotor,CreacionTablas,LimpiarClickActivo
from functions.functions_click_activo import InfoInsercionTable, GenerarExcelIcsoPromotor
from functions.funcions_modulos_estructura import ObtenerCedulaBuscar,GenerarEstructuraModulo

Routas_Click_Activo = APIRouter()

@Routas_Click_Activo.get("/CreacionTablasProcesoIcso")
async def CreacionTablasProceso():
    try:
        CreacionTablas()
        return {"estado":"Tablas creadas correctamente"}
    except Exception as e:
        return HTTPException(status_code=500,detail=str(e))

@Routas_Click_Activo.post("/ActualizarCLickActivo/")
async def ActualizarClickActivo(file: UploadFile):
    if not file.filename.endswith(('.xls', '.xlsx')):
        raise HTTPException(
            status_code=400, detail="El archivo debe ser un excel")
    try:
        conn = Conexion()
        if conn:
            if conn.is_connected():
                LimpiarClickActivo()
                filas = await InfoInsercionTable(file)

                cursor = conn.cursor()

                for fila in filas:
                    
                    cursor.execute("""
                        INSERT INTO activo (nit, primerapellido, segundoapellido, nombres, segundonombre,nombreintegrado, direccion, telefono1,
                            fechaingreso, fechanacimiento, coddepartamento, codciudad, codcomuna, barrio, estrato,celular,
                            actividadeconomicaid, negocioid, valorsolicitado, montoaprobado, plazo, periodicidaddias,
                            tasaefectiva, anualidad, cedulasociado, pagare, f_iniciofinanciacion, capital, saldocapital,
                            miembroid, nombre_cs, ced_prom, promotor, cod, ZONA, MUNICIPIO, cuenta, cooperativa, POLIZA,
                            CORREO, ced_ben_1, nom_beneficiario_1, parentesco_1, ced_ben_2, nom_beneficiario_2,
                            parentesco_2, ciclo, sexo, estado_civil, barrio_id_icso
                        )
                        VALUES (
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                        )
                    """, fila)

                conn.commit()
                cursor.close()
                conn.close()

                return {"Estado": "Click Activo Actualizado"}

    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

@Routas_Click_Activo.post("/AgregarRegistroClickActivo")
async def AgregarRegistroClickActivo(file:UploadFile):
    if not file.filename.endswith(('.xls','xlsx')):
        raise HTTPException(status_code=400,detail="No es un archivo de excel")
    try:
        conn = Conexion()
        if conn:
            if conn.is_connected():
                cursor = conn.cursor()
                filas = await InfoInsercionTable(file)
                for fila in filas:
                    cursor.execute("""
                            INSERT INTO activo (nit, primerapellido, segundoapellido, nombres, segundonombre,nombreintegrado, direccion, telefono1,
                                fechaingreso, fechanacimiento, coddepartamento, codciudad, codcomuna, barrio, estrato,celular,
                                actividadeconomicaid, negocioid, valorsolicitado, montoaprobado, plazo, periodicidaddias,
                                tasaefectiva, anualidad, cedulasociado, pagare, f_iniciofinanciacion, capital, saldocapital,
                                miembroid, nombre_cs, ced_prom, promotor, cod, ZONA, MUNICIPIO, cuenta, cooperativa, POLIZA,
                                CORREO, ced_ben_1, nom_beneficiario_1, parentesco_1, ced_ben_2, nom_beneficiario_2,
                                parentesco_2, ciclo, sexo, estado_civil, barrio_id_icso
                            )
                            VALUES (
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                            )
                        """, fila)
                conn.commit()
                cursor.close()
                conn.close()

                return {'Estado':"Registros insertados correctamente"}

    except Exception as e:
        return HTTPException(status_code=500,detail=str(e))

@Routas_Click_Activo.post("/ActualizarEntidadEconomicaOpa_Icso")
async def ActualizarCodigosActividadEconomica(file: UploadFile):
    if not file.filename.endswith(('.xls', '.xlsx')):
        raise HTTPException(
            status_code=400, detail="El archivo debe ser un excel")
    try:
        conn = Conexion()
        if conn:
            if conn.is_connected():
                cursor = conn.cursor()
                filas = await InfoInsercionTable(file)
                for fila in filas:
                    cursor.execute(
                        "INSERT INTO ActividadesEconomicas(codigo_opa,descripcion_opa,codigo_icso,descripcion_icso) VALUES(%s,%s,%s,%s)",fila
                    )
                conn.commit()
                cursor.close()
                conn.close()
                return {"estado":"Actividades Economicas Actualizadas Correctamente"}
                
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@Routas_Click_Activo.get("/DepurarClickActivoDataBase")
async def DepurarBaseDatosClick():
    try:
        DepurarTablaClickActivo()
        return {"estado":"Click Activo Depurado correctamente"}
    except Exception as e:
        return HTTPException(status_code=500,detail=str(e))

@Routas_Click_Activo.post("/ActualizarCodigosIcso")
async def ActualizarCodigos(file: UploadFile):
    if not file.filename.endswith(('.xls', '.xlsx')):
        raise HTTPException(
            status_code=400, detail="El archivo debe ser un excel")

    try:
        conn = Conexion()
        if conn:
            if conn.is_connected():
                Novedades = []
                filas = await InfoInsercionTable(file)
                for fila in filas:
                    codigo_Opa = fila[1]
                    codigo_icso = fila[0]
                    codigo_Opa_rea = fila[2]
                    resultado = VerificarCodigoTablaClickActivo(codigo_Opa)
                    resultadoReajuste = VerificarCodigoTablaClickActivo(
                        codigo_Opa_rea)
                    if resultado != 0:
                        estado = RemplazarCodigoOpa_Icso(
                            codigo_Opa, codigo_icso, codigo_Opa_rea)
                        if estado:
                            if codigo_Opa_rea == None:
                                Novedades.append({
                                    "Success": f"Se realizaron {resultado} cambios codigos cambiados: {codigo_Opa} > {codigo_icso} sin ningun reajuste"
                                })
                            else:
                                Novedades.append({
                                    "Success": f"Se realizaron {resultado} cambios codigos cambiados: {codigo_Opa} > {codigo_icso} con {resultadoReajuste} reajustes"
                                })
                    else:
                        Novedades.append({
                            "Danger": f"No se encontraron resultados con el codigo {codigo_Opa}"
                        })

                return Novedades

    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@Routas_Click_Activo.post("/EstructuraIcsoPromotor")
async def EstructuraPromotorIcso(Cedula: int = Form(...)):
    Datos = EstructuraIcsoPromotor(Cedula)
    archivo = GenerarExcelIcsoPromotor(Datos,Cedula)
    return FileResponse(archivo, filename="Archivo_icso_promotor_{}.xlsx".format(Cedula))


@Routas_Click_Activo.post("/EstructuraModulo")
async def EstructuraModulo(file: UploadFile):
    if not file.filename.endswith(('.xls', '.xlsx')):
        raise HTTPException(
            status_code=400, detail="El archivo debe ser un excel")
    try:
        conn = Conexion()
        if conn:
            if conn.is_connected():
                CedulasObtenidas = await ObtenerCedulaBuscar(file)
                Archivo = GenerarEstructuraModulo(CedulasObtenidas)
                return FileResponse(Archivo, filename="Modulo.xlsx")
    except Exception as e:
            return HTTPException(status_code=500, detail=str(e))