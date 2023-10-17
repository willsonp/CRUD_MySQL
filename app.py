from flask import Flask,render_template, request, redirect, url_for, flash
import MySQLdb.cursors
# from config import config
# from models.modeluser import ModelUser
# from models.entities.user import User

# Models

# Entities



app = Flask(__name__)
app.secret_key='mysecretkey'
# Config MySQL DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Devel0pment!'
app.config['MYSQL_DB'] = 'products'


@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/get_productos')
def get_Products():
   # Open connection to MySQL DB
    conn=MySQLdb.connect(host=app.config['MYSQL_HOST'],user=app.config['MYSQL_USER'],password=app.config['MYSQL_PASSWORD'],db=app.config['MYSQL_DB'])

        # Create cursor
    cursor = conn.cursor()
        # pasamos los valres a Select       
    cursor.execute('SELECT id, descripcion, costo, price  FROM productos WHERE status=%s','A')
    produtcs=cursor.fetchall()
        # cerramos cursor 
    cursor.close()
        # close connection
    conn.close()
    # print(produtcs)
    return render_template('list_products.html',products=produtcs)

@app.route('/productos')
def add_products():
    return render_template('products.html')



@app.route('/proveedor_list')
def proveedor_list():
    return render_template('proveedorlist.html')


@app.route('/add_proveedor')
def add_proveedor():
    return render_template('proveedor.html')

# @app.route('/login',methods=['POST','GET'])
# def Login():
#     if request.method == 'POST':
#         user = User(0,request.form['username'],request.form['password'])
#         logged_user = ModelUser.login(conn,user)
        
#         if logged_user:
#             return redirect(url_for('Index'))
#         else:
#             flash('Username or Password incorrect','danger')

#         return render_template('auth/login.html')
#     else:
#         return render_template('auth/login.html')


@app.route('/add_product',methods=['POST','GET'])
def Add_Product():
    if request.method == 'POST':
        descrip=request.form['descrip']
        price=request.form['price'] 
        cost=request.form['cost']        
        
        
        # Connect to MySQL database
        conn = MySQLdb.connect(host=app.config['MYSQL_HOST'],
                               user=app.config['MYSQL_USER'],
                               password=app.config['MYSQL_PASSWORD'],
                               db=app.config['MYSQL_DB'])

        # Create cursor
        cursor = conn.cursor()

        # pasamos los valres a insertar       
        cursor.execute('INSERT INTO productos (descripcion,costo,price) VALUES (%s,%s,%s)',(descrip,cost,price))
        # almacenamos los cambios de manera permanente        
        conn.commit()
        # cerramos cursor 
        cursor.close()
        # close connection
        conn.close()

        #  para enviar un mesaje al usuario
        flash('Product Added successfully','success')
        
        # redireccionar al index                
        return redirect(url_for('get_Products'))

@app.route('/get_product_byId/<id>')
def get_productByID(id):       
    # Open connection to MySQL DB
    conn=MySQLdb.connect(host=app.config['MYSQL_HOST'],user=app.config['MYSQL_USER'],password=app.config['MYSQL_PASSWORD'],db=app.config['MYSQL_DB'])

    # Create cursor
    cursor = conn.cursor()
    # pasamos los valres a Select NOTA: el id debe ser una tupla       
    cursor.execute("SELECT id, descripcion, costo,price FROM productos WHERE id=%s",(id,)) 

    produtc_byId=cursor.fetchall()
    # cerramos cursor 
    cursor.close()
    # close connection
    conn.close()
    #  para enviar un mesaje al usuario
    return render_template('edit_product.html',product=produtc_byId[0])

@app.route('/edit_product/<id>',methods=['POST','GET'])
def Edit_Product(id):
    if request.method == 'POST':
        descrip=request.form['descrip']
        price=request.form['price'] 
        cost=request.form['cost'] 

        # print(descrip,price,cost,id)

        # Open connection to MySQL DB
        conn=MySQLdb.connect(host=app.config['MYSQL_HOST'],user=app.config['MYSQL_USER'],password=app.config['MYSQL_PASSWORD'],db=app.config['MYSQL_DB'])

        # Create cursor
        cursor = conn.cursor()
        # pasamos los valres a Select       
        cursor.execute('UPDATE productos SET descripcion=%s,costo=%s,price=%s WHERE id=%s',(descrip,cost,price,id))
        # ejecutamos la consulta
        conn.commit()
        # cerramos cursor 
        cursor.close()
        # close connection
        conn.close()
        #  para enviar un mesaje al usuario
        flash('Product Edited successfully','success')
       
    return redirect(url_for('get_Products'))

@app.route('/delete_product/<id>')
def Delete_Product(id):
    # Open connection to MySQL DB
    conn=MySQLdb.connect(host=app.config['MYSQL_HOST'],user=app.config['MYSQL_USER'],password=app.config['MYSQL_PASSWORD'],db=app.config['MYSQL_DB'])

    # Create cursor
    cursor = conn.cursor()
    # pasamos los valres a Select       
    cursor.execute('UPDATE productos SET status=%s WHERE id=%s',('I',id))
    # ejecutamos la consulta
    conn.commit()
    # cerramos cursor 
    cursor.close()
    # close connection
    conn.close()
    #  para enviar un mesaje al usuario
    flash('Product Deleted successfully','success')

    return redirect(url_for('get_Products'))

# run the App
if __name__ == '__main__':
    # app.config.from_object(config['development'])
    app.run(port=3000,debug=True)
