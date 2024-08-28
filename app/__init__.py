from flask import Flask
from flask_pymongo import PyMongo
from .config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # initializes the PyMongo instance with the Flask application, allowing the application to use the MongoDB database.
    mongo.init_app(app)
    
    with app.app_context():
        from .routes import user_routes
        from .routes import AddFadeWaveCut_routes
        from .routes import AddBobsCuts_routes
        from .routes import AddBrushWaveCut_routes
        from .routes import AddStyleCutDye_routes
        from .routes import AddTopDyeHairCut_routes
        from .routes import AddFadecutFluffyDye_routes
        from .routes import AddDyeCurlyCuts_routes
        from .routes import AddDoubleDyeFade_routes
        from .routes import Addbooking_routes
        from .routes import review_routes
  
        # register the blueprint 
        app.register_blueprint(user_routes.app)
        app.register_blueprint(AddFadeWaveCut_routes.app)
        app.register_blueprint(AddBobsCuts_routes.app)
        app.register_blueprint(AddBrushWaveCut_routes.app)
        app.register_blueprint(AddStyleCutDye_routes.app)
        app.register_blueprint(AddTopDyeHairCut_routes.app)
        app.register_blueprint(AddFadecutFluffyDye_routes.app)
        app.register_blueprint(AddDyeCurlyCuts_routes.app)
        app.register_blueprint(AddDoubleDyeFade_routes.app)
        app.register_blueprint(Addbooking_routes.app)
        app.register_blueprint(review_routes.app)
        
        
    return app