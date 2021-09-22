from flask import Flask, request, jsonify,make_response

app = Flask(__name__)

income =[
    {"description":"salary", "amount":5000}
]
@app.route("/")
def index():
    return '<h1> Hello world </h1>'

@app.route("/incomes")
def get_incomes():
    return jsonify(income)

@app.route("/incomes",methods=["POST"])
def add_income():
    income.append(request.get_json())
    return 'Created', 201

stock={
    "fruit":{ "kiwi":100,
    "banana":20,
    "orange":32,
    "pear":232
              }
}

@app.route("/stock")
def get_stock():
    res= make_response(jsonify(stock),200)
    return res

@app.route("/stock/<collection>")
def get_collection(collection):
    if collection in stock:
        res = make_response(jsonify(stock[collection],200))
        return res
    res = make_response(jsonify({"error":"not found"}),404)
    return res

@app.route("/stock/<collection>/<member>")
def get_members(collection,member):
    if collection in stock:
        member= stock[collection].get(member)
        if member:
            res=make_response(jsonify(member),200)
            return res
        res = make_response(jsonify({"error": "not found"}),404)
        return res
    res = make_response(jsonify({"error": "not found"}),404)
    return res

@app.route("/stock/<collection>", methods=["PUT"])
def put_collection(collection):
    req=request.get_json()
    # business logic
    if collection in stock:
        original = stock[collection]
        for key,value in req.items():
            if key in original:
                original[key]=value
            else:
                original[key]=value
        stock[collection]=req
        res=make_response(jsonify({"msg":"collection updated"}),200)
        return res
    #either create or we need to send error saiung record not found for updation
    #stock[collection]=req
    res = make_response(jsonify({"error": "not found"}), 404)
    return res



@app.route("/stock/<collection>/<member>", methods=["DELETE"])
def delete_collection(collection,member):
    if collection in stock:
        if member in stock[collection]:
            del stock[collection][member]
            res = make_response(jsonify({"msg":"deleted..."}),204)
            return res
        res = make_response(jsonify({"msg": "member not there..."}), 204)
        return res
    else:
        res = make_response(jsonify({"msg": "collection not present..."}), 404)
        return res




if __name__=='__main__':
    app.run(debug=True)