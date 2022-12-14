from flask import Flask, render_template

from controllers.members_controller import members_blueprint
from controllers.sessions_controller import sessions_blueprint
from controllers.attendance_controller import attendance_blueprint



app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(sessions_blueprint)
app.register_blueprint(attendance_blueprint)



@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
