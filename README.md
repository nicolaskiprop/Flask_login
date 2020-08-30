# Flask_login
## create a virtual environment
     virtualenv env --python=python3.8
    
## Activate environment
     source env/bin/activate

#### Create app.py with the following content
        from flask import Flask

        app = Flask(__name__)


        @app.route('/')
        def home():
            return "hello there!"


        if __name__ == '__main__':
            app.run(debug=True)
## skipped
  
### add a configuration file 
add config.py in the main directory
 
## export APP_SETTINGS
      export APP_SETTINGS="config.DevelopmentConfig"  
### update config.py to search the environment for the variable DATABASE_URL:
       
       SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
## add the DATABASE_URL environment
        export DATABASE_URL="sqlite:///posts.db"
        
      