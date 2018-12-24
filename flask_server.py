from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"about": "Hello world!"})

@app.route('/multi/<int:num>', methods=['GET'])
def get_mult(num):
    return jsonify({'result': num*10})

@app.route('/image', methods=['POST'])
def convertImg():

    image = request.files["image"]
    image.save("img.jpeg")
    return jsonify({'result': 'succeeded!!!'})
    #return jsonify({'result': 'succeeded!!!'})

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
