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

  
    
 
 