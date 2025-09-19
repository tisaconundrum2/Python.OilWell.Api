from flask import Flask
from flasgger import Swagger
from app.controllers.api_well_data_controller import api_well_data_bp

def create_app():
    app = Flask(__name__)
    app.config['SWAGGER'] = {
        'title': 'Oil Well API',
        'uiversion': 1
    }
    Swagger(app)

    app.register_blueprint(api_well_data_bp)

    return app

# In a production system, I would technically put this in its own file.
# And I'd have it setup as a background service to keep the DB updated.
# But for this demo, we're opting for simplicity and putting it here... 🤷‍♂️
def load_db():
    # Crawl https://wwwapps.emnrd.nm.gov/OCD/OCDPermitting/Data/WellDetails.aspx?api=xx-xxx-xxxxx
    
