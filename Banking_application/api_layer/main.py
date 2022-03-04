from flask import Flask, request, jsonify

app: Flask = Flask(__name__)

my_list = ["I need to get Milk", "I need to go to Publix", "BATMAN!"]


@app.route("/greeting", methods=["GET"])
def hello_world():
    return "Hello World!"


@app.route("/personal/<name>", methods=["GET"])
def personal_greeting(name: str):
    return f"Hello {name}!"


@app.route("/add/<num_one>/<num_two>", methods=["GET"])
def addition_function(num_one: str, num_two: str):
    result = int(num_one) + int(num_two)
    return str(result)


@app.route("/list/<index>", methods=["GET"])
def get_phrase_from_list(index: str):
    global my_list
    return my_list[int(index)]


@app.route("/list", methods=["GET"])
def get_all_phrases_from_list():
    global my_list
    my_json_list = jsonify(my_list)
    return my_json_list, 200


@app.route("/json", methods=["GET"])
def return_a_json():
    customer_id = 1
    first_name = "Ted"
    last_name = "Teddington"

    customer_as_dictionary = {
        "customerId": customer_id,
        "fistName": first_name,
        "lastName": last_name
    }
    customer_as_json = jsonify(customer_as_dictionary)
    return customer_as_json, 200


@app.route("/list", methods=["POST"])
def add_phrase_to_list():
    request_content = request.get_json()
    global my_list
    my_list.append(request_content["key"])
    return "Phrase added successfully"


@app.route("/query", methods=["GET"])
def get_filtered_phrases():
    min_index = request.args["min"]
    max_index = request.args["max"]
    global my_list
    return_list = []
    for index in range(0, len(my_list)-1, 1):
        if int(min_index) <= index <= int(max_index):
            return_list.append(my_list[index])
    return_list_as_json = jsonify(return_list)
    return return_list_as_json, 200


app.run()
