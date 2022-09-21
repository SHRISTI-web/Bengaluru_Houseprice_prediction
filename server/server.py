from flask import Flask, request, jsonify
import util
app=Flask(__name__)
@app.route('/grt_location_names')
def get_location_names():
    response=jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return "hi"


if __name__=="__main__":
    print("starting Python Flask Server for home price prediction...")
    app.run()