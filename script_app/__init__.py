from flask import Flask, render_template, request 

app = Flask(__name__)

# index page
@app.route('/')
def index():
    return render_template('index.html')

# script page
@app.route('/script', methods=['GET'])
def write_script():
    # input 값 받아오기 
    file_type = request.args.get("file_type")
    # {{ file_type1 }} : 총 문장 수 / {{ file_type2 }} : 최소 수정률 / {{ file_type3 }} : 수정해야 할 최소 문장 수 
    if file_type == "TS":
        file_type1 = "1,500"
        file_type2 = "30%"
        file_type3 = "450"
    elif file_type == "NM":
        file_type1 = "1,000"
        file_type2 = "90%"
        file_type3 = "900"

    lang_pair = request.args.get("lang_pair")
    token = request.args.get("token")
    volume = request.args.get("volume")
    unit_price = request.args.get("unit_price")
    deadline = request.args.get("deadline")
    reply_deadline = request.args.get("reply_deadline")
    pm = request.args.get("pm")

    return render_template('result.html', 
                           file_type=file_type, file_type1=file_type1, file_type2=file_type2, file_type3=file_type3, 
                           lang_pair=lang_pair, token=token, volume=volume, unit_price=unit_price, 
                           deadline=deadline, reply_deadline=reply_deadline, pm=pm
                            )


if __name__ == "__main__":
    app.run(debug=True)