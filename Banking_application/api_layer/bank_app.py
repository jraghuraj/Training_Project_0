from flask import Flask, jsonify

from dal_layer.customer_dao.customer_dao_imp import CustomerDAOImp
from entities.customer_class_information import Customer
from tests.customer_service_test.test_customer_service import customer_service

app: Flask = Flask(__name__)
customer_dao = CustomerDAOImp


@app.route("/customer", methods=["POST"])
def create_customer():
    customer_id = Customer(["firstname"], ["lastname"], ["customIDnumber"])
    result = customer_service.service_create_customer()
    result_dict = result.convert_to_dictionary()
    result_json = jsonify(result_dict)
    return result_json, 202


app.run()
