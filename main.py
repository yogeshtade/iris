from flask import Flask, render_template,request,jsonify

my_app = Flask(__name__)


@my_app.route('/')
def index():
    return render_template('index.html')

# @my_app.route('/get_data',methods=['POST'])
# def get_data():
#     data = request.form['var']
#     data1 = request.form['var1']

#     print(data,data1)

#     return 'Data Received'


# @my_app.route('/get_data',methods=['GET','POST'])
# def get_data():
#     data = request.form['var']
#     data1 = request.form['var1']

#     print(data,data1)

#     return 'Data Received'


# @my_app.route('/get_data',methods=['GET','POST'])
# def get_data():
#     if request.method == 'POST':
#         data = request.form['var']
#         data1 = request.form['var1']

#         print(data,data1)
#     else:
#         print('Data not received')

#     return 'Data Received'

# @my_app.route('/get_data')
# def get_data():
#     data = request.form['var']
#     data1 = request.form['var1']

#     print(f'{data = },{data1 = }')

#     return 'Data Received'


# @my_app.route('/get_data',methods=['GET','POST'])
# def get_data():
#     data = request.form['var']
#     data1 = request.form['var1']

#     print(f'{data = },{data1 = }')

#     return 'Data Received'

# @my_app.route('/get_data',methods=['GET','POST'])
# def get_data():
#     if request.data == 'POST':
#         data = request.form['var']
#         data1 = request.form['var1']

#         print(f'{data = },{data1 = }')

#     else:
#         var = request.form['var']
#         print(f'{var= }')
#         print('Post method not used')

#     return 'Data Received'

# @my_app.route('/get_data',methods=['POST'])
# def get_data():
#     if request.data == 'POST':
#         data = request.form['var']
#         data1 = request.form['var1']

#         print(f'{data = },{data1 = }')

#     else:
#         var = request.form['var']
#         print(f'{var= }')
#         print('Post method not used')

#     return 'Data Received'

# @my_app.route('/get_data',methods=['GET','POST'])
# def get_data():
#     data = request.form
  
#     print(f'{data}')
#     print(type(data))
#     data_from_im = data['var1']
#     print(data_from_im)

#     return render_template('index.html')

# @my_app.route('/get_data',methods=['GET','POST'])
# def get_data():
#     data = request.form
  
#     print(f'{data}')
#     print(type(data))
#     data_from_im = data['var1']
#     print(data_from_im)

#     return jsonify(data)


@my_app.route('/get_data',methods=['GET','POST'])
def get_data():
    data = request.get_json() ## Data in form of dict
  
    print(f'{data}')
    print(type(data))
    data_from_im = data['var1']
    print(data_from_im)

    return jsonify(data)


@my_app.route('/data',methods=['GET','POST'])
def data():
    var = request.args  ###This is for query parameters
    print(var)
    print(type(var))

    return jsonify(var)


if __name__ == '__main__':
    my_app.run(debug=True)

