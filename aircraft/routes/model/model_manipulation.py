from flask import request, jsonify
from utils.settings import CONNECTION

class ModelManipulation():
    def __init__(self, app):
        self.app = app
        app.route('/models', methods=['GET'])(self.get_models)
        app.route('/models/<int:model_id>', methods=['GET'])(self.get_model_by_id)
        app.route('/models', methods=['POST'])(self.create_model)
        app.route('/models/<int:model_id>', methods=['PUT'])(self.update_model)
        app.route('/models/<int:model_id>', methods=['DELETE'])(self.delete_model)

    def get_models(self):
        try:
            with CONNECTION as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM management.aircrafts_model")
                models = cursor.fetchall()
                return jsonify({'models': models}), 200
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    def get_model_by_id(self, model_id):
        try:
            with CONNECTION as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM management.aircrafts_model WHERE aircraft_model_id = %s", (model_id,))
                model = cursor.fetchone()
                if model:
                    return jsonify({'model': model}), 200
                else:
                    return jsonify({'message': 'Model not found'}), 404
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    def create_model(self):
        try:
            data_model = request.get_json()
            
            insert_query = """
            INSERT INTO management.aircrafts_model (
                model, manufacturer, manufacturing_year, aircraft_type, passenger_capacity,
                cargo_capacity, range, maximum_speed, service_ceiling, engine_type,
                number_of_engines, maximum_takeoff_weight, fuel_system, electrical_system,
                hydraulic_system, landing_gear, avionics_system, certifications,
                documentation, leasing_history, image
            ) VALUES (
                %(model)s, %(manufacturer)s, %(manufacturing_year)s, %(aircraft_type)s,
                %(passenger_capacity)s, %(cargo_capacity)s, %(range)s, %(maximum_speed)s,
                %(service_ceiling)s, %(engine_type)s, %(number_of_engines)s,
                %(maximum_takeoff_weight)s, %(fuel_system)s, %(electrical_system)s,
                %(hydraulic_system)s, %(landing_gear)s, %(avionics_system)s,
                %(certifications)s, %(documentation)s, %(leasing_history)s, %(image)s
            )
            """

            with CONNECTION as connection:
                cursor = connection.cursor()
                cursor.execute(insert_query, data_model)  # Use data_model in the execute statement
                # Additional logic if needed
                return jsonify({'message': 'Model created successfully'}), 201
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    def update_model(self, model_id):
            try:
                data_model = request.get_json()
                
                update_query = """
                UPDATE management.aircrafts_model
                SET
                    model = %(model)s,
                    manufacturer = %(manufacturer)s,
                    manufacturing_year = %(manufacturing_year)s,
                    aircraft_type = %(aircraft_type)s,
                    passenger_capacity = %(passenger_capacity)s,
                    cargo_capacity = %(cargo_capacity)s,
                    range = %(range)s,
                    maximum_speed = %(maximum_speed)s,
                    service_ceiling = %(service_ceiling)s,
                    engine_type = %(engine_type)s,
                    number_of_engines = %(number_of_engines)s,
                    maximum_takeoff_weight = %(maximum_takeoff_weight)s,
                    fuel_system = %(fuel_system)s,
                    electrical_system = %(electrical_system)s,
                    hydraulic_system = %(hydraulic_system)s,
                    landing_gear = %(landing_gear)s,
                    avionics_system = %(avionics_system)s,
                    certifications = %(certifications)s,
                    documentation = %(documentation)s,
                    leasing_history = %(leasing_history)s,
                    image = %(image)s
                WHERE
                    aircraft_model_id = %s
                """

                with CONNECTION as connection:
                    cursor = connection.cursor()
                    cursor.execute(update_query, {**data_model, 'aircraft_model_id': model_id})  # Use data_model in the execute statement
                    # Additional logic if needed
                    return jsonify({'message': 'Model updated successfully'}), 200
            except Exception as e:
                return jsonify({'message': str(e)}), 500
    def delete_model(self, model_id):
        try:
            with CONNECTION as connection:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM management.aircrafts_model WHERE aircraft_model_id = %s", (model_id,))
                # Lógica de exclusão
                return jsonify({'message': 'Model deleted successfully'}), 200
        except Exception as e:
            return jsonify({'message': str(e)}), 500
