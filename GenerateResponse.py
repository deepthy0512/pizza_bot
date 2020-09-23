from flask import jsonify


def generateResponse(data, msg):
    response_data = {}
    data_list = []
    try:
        for i in data:
            temp = {}
            temp["order_id"] = i[0]
            temp["pizza_name"] = i[1]
            temp["size"] = i[2]
            temp["status"] = i[3]
            data_list.append(temp)
            response_data["data"] = data_list

        response_data["msg"] = msg
        print(f"Respone data : {response_data}")
        return jsonify(response_data)
    except IndexError as e:
        print(e)
        return str(e)

