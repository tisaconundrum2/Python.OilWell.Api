from flask import Blueprint, request, jsonify
from flasggo import swag_from
from app.repositories.api_well_data_repository import APIWellDataRepository
from app.models.api_well_data import APIWellData

api_well_data_bp = Blueprint('api_well_data', __name__)
repository = APIWellDataRepository('api_well_data.db')


@api_well_data_bp.route('/api/well', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'List of well data',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'operator': {'type': 'string'},
                        'status': {'type': 'string'},
                        'well_type': {'type': 'string'},
                        'work_type': {'type': 'string'},
                        'directional_status': {'type': 'string'},
                        'multi_lateral': {'type': 'string'},
                        'mineral_owner': {'type': 'string'},
                        'surface_owner': {'type': 'string'},
                        'surface_location': {'type': 'string'},
                        'gl_elevation': {'type': 'number'},
                        'kb_elevation': {'type': 'number'},
                        'df_elevation': {'type': 'number'},
                        'single_multiple_completion': {'type': 'string'},
                        'potash_waiver': {'type': 'string'},
                        'spud_date': {'type': 'string'},
                        'last_inspection': {'type': 'string'},
                        'tvd': {'type': 'number'},
                        'api': {'type': 'string'},
                        'latitude': {'type': 'number'},
                        'longitude': {'type': 'number'},
                        'crs': {'type': 'string'},
                    }
                }
            }
        }
    }
})
def get_wells():
    wells = repository.get()
    return jsonify([well.__dict__ for well in wells])

@