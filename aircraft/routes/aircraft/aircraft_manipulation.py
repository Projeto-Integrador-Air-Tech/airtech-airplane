from flask import request, jsonify
from utils.settings import CONNECTION

class AircraftManipulation():
    def __init__(self, app):
        self.app = app
        app.route('/aircrafts', methods=['GET'])(self.get_aircrafts)
        app.route('/aircrafts/<int:aircraft_id>', methods=['GET'])(self.get_aircraft_by_id)
        app.route('/aircrafts', methods=['POST'])(self.create_aircraft)
        app.route('/aircrafts/<int:aircraft_id>', methods=['PUT'])(self.update_aircraft)
        app.route('/aircrafts/<int:aircraft_id>', methods=['DELETE'])(self.delete_aircraft)

    def get_aircrafts(self):
        try:
            with CONNECTION as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM management.aircrafts")
                aircrafts = cursor.fetchall()
                return jsonify({'aircrafts': aircrafts}), 200
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    def get_aircraft_by_id(self, aircraft_id):
        try:
            with CONNECTION as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM management.aircrafts WHERE aircraft_id = %s", (aircraft_id,))
                aircraft = cursor.fetchone()
                if aircraft:
                    return jsonify({'aircraft': aircraft}), 200
                else:
                    return jsonify({'message': 'Aircraft not found'}), 404
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    def create_aircraft(self):
        try:
            data_aircraft = request.get_json()
            # Validar e extrair os dados necessários do JSON

            with CONNECTION as connection:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO management.aircrafts (...) VALUES (...)")
                # Lógica de inserção
                return jsonify({'message': 'Aircraft created successfully'}), 201
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    def update_aircraft(self, aircraft_id):
        try:
            data_aircraft = request.get_json()
            # Validar e extrair os dados necessários do JSON

            with CONNECTION as connection:
                cursor = connection.cursor()
                cursor.execute("UPDATE management.aircrafts SET ... WHERE aircraft_id = %s", (aircraft_id,))
                # Lógica de atualização
                return jsonify({'message': 'Aircraft updated successfully'}), 200
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    def delete_aircraft(self, aircraft_id):
        try:
            with CONNECTION as connection:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM management.aircrafts WHERE aircraft_id = %s", (aircraft_id,))
                # Lógica de exclusão
                return jsonify({'message': 'Aircraft deleted successfully'}), 200
        except Exception as e:
            return jsonify({'message': str(e)}), 500
