from flask import jsonify, request
from db.db import cnx

class DataSet():
    global cur
    cur = cnx.cursor()

    def list():
        lista = []
        cur.execute("SELECT * FROM datasets")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(columns, row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close

    def create(body):
        data = (body['idProyecto'],body['nombreProyecto'], body['encargado'], body['tipoArchivo'], body['archivoDir'],body['archivoNombre'])
        sql = "INSERT INTO datasets(id_proyecto,nombre_proyecto, encargado, tipo_archivo, archivo_dir,archivo_nombre) VALUES(%s, %s, %s, %s,%s,%s)"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': 'Insertado con exito'}, 200
        cnx.close

    def delete(id):
        data = (id,)
        sql = "DELETE FROM datasets WHERE id_archivo = %s"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': 'Eliminado con exito'}, 200
        cnx.close

    def updateEncargado(id,encargado):
        data = (encargado,id)
        sql = "UPDATE datasets SET encargado = %s WHERE id_archivo = %s"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': 'Actualizado con exito'}, 200
        cnx.close

    def updateArchivo(body):
        data = (body['tipoArchivo'],body['archivoDir'], body['idArchivo'])
        sql = "UPDATE datasets SET tipo_archivo = %s, archivo_dir = %s WHERE id_archivo = %s"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': 'Actualizado con exito'}, 200
        cnx.close