from flask import Flask

app = Flask(__name__)






@app.route('/test/<zeyad>')   # method --> get //// method --> post 
def test_zeyad(zeyad):
    return f"Hello, {zeyad}! This is a test route."



if __name__ == '__main__':
    app.run(debug=True)