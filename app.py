from flask import Flask, render_template
import qrcode
app = Flask(__name__)

@app.route('/')
def hello():
    a = input("하고 싶은 말: ")
    img = qrcode.make(a)
    ad = "C:/Users/고객님/Desktop/vaction/flask -a/pyqrhtml/static/asdf.png"
    img.save(ad)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)