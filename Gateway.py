from flask import Flask, url_for, jsonify, request
import paho.mqtt.client as mqtt
import os
app = Flask(__name__)

messages = []
client = mqtt.Client("lmwxznif")

@app.route('/', methods=['POST'])
def api_root():
    new = request.get_json()
    messages.append(new)
    client.connect("m13.cloudmqtt.com", 1883, 60)
    client.publish("Lior")
    return jsonify({"messages": messages})


@app.route('/', methods=['GET'])
def api_root2():
    return jsonify({"messages": messages})


if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=int(os.environ.get("PORT" , 5000)))