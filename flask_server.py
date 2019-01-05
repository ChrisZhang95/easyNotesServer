from flask import Flask, jsonify, request

#ocr libraries
from PIL import Image
import sys
import pyocr
import pyocr.builders

app = Flask(__name__)

#setting up for ocr
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = 'eng'
print("Will use lang '%s'" % (lang))

#routing
@app.route('/')
def hello_world():
    return jsonify({"about": "Hello world!"})

@app.route('/multi/<int:num>', methods=['GET'])
def get_mult(num):
    return jsonify({'result': num*10})

@app.route('/image', methods=['POST'])
def convertImg():

    image = request.files["image"]
    image.save("img.jpg")
    txt = tool.image_to_string(
        Image.open('img.jpg'),
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )

    return txt
    #return jsonify({'result': txt})

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
