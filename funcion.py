



class test():

        def create_concesionado(acceso_obj, mock_crea_consecion, mock_crea_consecion_otro ):
        """
        Crea un articulo concesionado con varios equipos.

        Detalles:
            1. Se obtiene informacion del turno
            2. Se inicia el turno
            3. Se obtiene informacion del turno
            4. Se finaliza el turno
        """
        logging.info('================> Arranca TEST #1: Creando Articulo concesionado2...')
        articulo = create_article_concessioned(acceso_obj, mock_crea_consecion)
        assert articulo.get("status_code") == 201
        articulo_otro = create_article_concessioned(acceso_obj, mock_crea_consecion_otro)
        assert articulo_otro.get("status_code") == 201
        logging.info(f'articulo {articulo}')
        record_id = articulo.get('id')
        return articulo, articulo_otro

    def partial_return(articulo, data_concesion):
        equipos = data_concesion['equipos']
        data = {
            'record_id' : articulo['id'],
            'status' : 'partial',
            'quien_entrega' :  data_concesion['persona_nombre_otro'],
            'identificacion_entrega' : data_concesion['persona_identificacion_otro'],
            'comentarios' : "Devolucion de Parical: partial_return",
            'entregado_por': "otro",
            'equipos' : []
            }
        for equipo in equipos:
            row = {}
            row['id_movimiento'] = equipo['id_movimiento']
            row['cantidad_devuelta'] = round(equipo['cantidad_equipo_concesion']/3)
            row['state'] = "complete"
            row['evidencia'] = [{
                'file_name':'equipo_total.png',
                'file_url':'https://f001.backblazeb2.com/file/app-linkaform/public-client-126/68600/6076166dfd84fa7ea446b917/2026-02-25T11:44:39_5.png'}]
            data['equipos'].append(row)
        response = acceso_obj.update_article_concessioned(data, articulo['id'])
        return True

    def complete_return_empleado(articulo, data_concesion):
        data = {
            'record_id' : articulo['id'],
            'status' : 'total',
            'state' : 'complete',
            'quien_entrega' :  data_concesion['persona_nombre_concesion'],
            'identificacion_entrega' : data_concesion['persona_identificacion_otro'],
            'comentarios' : "Devolucion de Pruebas: complete_return_empleado",
            'evidencia' : [{
                'file_name':'equipo_total.png',
                'file_url':'https://f001.backblazeb2.com/file/app-linkaform/public-client-126/68600/6076166dfd84fa7ea446b917/2026-02-25T11:44:39_5.png'}]
            }
        alog nueo a complyete
        response = acceso_obj.update_article_concessioned(data, articulo['id'])
        return response

    def one_article_return():
        aca tambine 
        pero esta es de test
        return True
