from flask import Flask,render_template,request
from flask_cors import CORS,cross_origin  #If in future we deploy it on AWS or AZURE
import math

app=Flask(__name__)

#hmara objective ye hai ki hme addition,subtraction division multiplication krne hai aur uske andar data pass krna hai.
#Remember GET and POST both sends data difference is GET sends through URL and POST through Body.
@app.route('/',methods=['GET','POST'])  #post me daala gya input kisi ko visible nhi milega URL me.'/'mtlb root
def home_page():
    return render_template('index.html')#render krwane ke liye.

@app.route('/operation', methods=['POST'])
@cross_origin()
def operation():
    operation_type = request.form.get('operation-type')
    if operation_type == 'algebraic':
        return render_template('algebraic.html')
    elif operation_type == 'trigonometric':
        return render_template('trigonometric.html')
    elif operation_type == 'miscellaneous':
        return render_template('miscellaneous.html')
    else:
        return "Invalid Operation Type"

@app.route('/algebraic', methods=['POST'])
@cross_origin()
def algebraic_operations():
    number1 = float(request.form['number1'])
    number2 = float(request.form['number2'])
    operation = request.form['operation']
    
    if operation == 'add':
        result = number1 + number2
        message = f'The sum of {number1} and {number2} is {result}'
    
    elif operation == 'subtract':
        result = number1 - number2
        message = f'The subtraction of {number1} and {number2} is {result}'
    
    elif operation == 'multiply':
        result = number1 * number2
        message = f'The multiplication of {number1} and {number2} is {result}'
    
    elif operation == 'divide':
        result = number1 / number2
        message = f'The division of {number1} and {number2} is {result}'
    
    elif operation == 'modulus':
        result = number1 % number2
        message = f'The modulus of {number1} and {number2} is {result}'
    
    elif operation == 'power':
        result = math.pow(number1, number2)
        message = f'{number1} raised to the power of {number2} is {result}'
    
    else:
        message = 'Invalid operation'
        
    return render_template('results.html', result=message)
    
@app.route('/trigonometric', methods=['POST'])
@cross_origin()
def trigonometric_operations():
    number = float(request.form['number'])
    operation = request.form['operation']
    
    if operation == 'sin':
        result = math.sin(math.radians(number))
        message = f'The sine of {number} degrees is {result}'
    
    elif operation == 'cos':
        result = math.cos(math.radians(number))
        message = f'The cosine of {number} degrees is {result}'
    
    elif operation == 'tan':
        result = math.tan(math.radians(number))
        message = f'The tangent of {number} degrees is {result}'
    
    elif operation == 'cosec':
        result = 1 / math.sin(math.radians(number))
        message = f'The cosecant of {number} degrees is {result}'
    
    elif operation == 'sec':
        result = 1 / math.cos(math.radians(number))
        message = f'The secant of {number} degrees is {result}'
    
    elif operation == 'cot':
        result = 1 / math.tan(math.radians(number))
        message = f'The cotangent of {number} degrees is {result}'
    
    else:
        message = 'Invalid operation'
    
    return render_template('results.html', result=message)

@app.route('/miscellaneous', methods=['POST'])
@cross_origin()
def miscellaneous_operations():
    number1 = float(request.form['number1'])
    operation = request.form['operation']
    if operation == 'log10':
        result = math.log10(number1)
        message = f'The base-10 logarithm of {number1} is {result}'
    
    elif operation == 'log2':
        result = math.log2(number1)
        message = f'The base-2 logarithm of {number1} is {result}'
    
    elif operation == 'sqrt':
        result = math.sqrt(number1)
        message = f'The square root of {number1} is {result}'
    
    elif operation == 'degrees':
        result = math.degrees(number1)
        message = f'{number1} radians is {result} degrees'
    
    elif operation == 'radians':
        result = math.radians(number1)
        message = f'{number1} degrees is {result} radians'
    
    elif operation == 'percentage':
        number2 = float(request.form['number2'])
        result = (number1 / 100) * number2
        message = f'{number1} % of  {number2} is  {result}'
    
    else:
        message = 'Invalid operation'
    
    return render_template('results.html', result=message)

if __name__ == '__main__':
    app.run(debug=True)

