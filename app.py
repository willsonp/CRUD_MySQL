from flask import Flask,render_template, request, redirect, url_for, flash
# import MySQLdb.cursors
from flask_wtf.csrf import CSRFProtect
from  flask_login import LoginManager, login_required, login_user, logout_user
import json
from config import config
# Models
from models.modeluser import ModelUser
# Entities
from models.entities.users import Users

app = Flask(__name__)
# para cifrar los formularios generar Token
csrf=CSRFProtect(app)

# app.secret_key='tMUHQ$1rvpUg5Lh'
# para manejar sesiones
login_manager_app = LoginManager(app)
# Config MySQL DB
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_PORT'] = 3306
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Devel0pment!'
# app.config['MYSQL_DB'] = 'products'



@login_manager_app.user_loader
def load_user(id):
    # conn=MySQLdb.connect(host=app.config['MYSQL_HOST'],user=app.config['MYSQL_USER'],password=app.config['MYSQL_PASSWORD'],db=app.config['MYSQL_DB'])
    # instanciamos la conexion
    conn=config['conexion'].get_connection()
    return ModelUser.get_id(conn,id)


@app.route('/home',methods=['POST','GET'])
@login_required
@csrf.exempt # para que no valide el token
def Home(opcionesMenu=None):
    return render_template('layout.html',opcionesMenu=opcionesMenu)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def Login():
    if request.method == 'POST':
       
        # conn=MySQLdb.connect(host=app.config['MYSQL_HOST'],user=app.config['MYSQL_USER'],password=app.config['MYSQL_PASSWORD'],db=app.config['MYSQL_DB'])

        # instanciamos la conexion
        conn=config['conexion'].get_connection()
        
        user = Users(0,request.form['username'],request.form['password'])
        # print(request.form['username'],request.form['password'])
        # print(user.username,user.password)

        logged_user = ModelUser.login(conn,user)
        
        # print(logged_user)

        conn.close()
        
        if logged_user != None:
           if(logged_user.password):    
                login_user(logged_user) 
                # print(logged_user.username)
                flash('Welconme youre Logged In','Success')   

                # llamamos el procedimiento almacenado
                # instanciamos la conexion
                # conn=config['conexion'].get_connection()
                
                # cursor = conn.cursor()
                
                # result = cursor.execute('call mostrar_menuprincipal(%s)',[(logged_user.id,)])
                
                # extract row headers
                # row_headers=[x[0] for x in cursor.description] #this will 

                # result = cursor.fetchall()                
                
                # # print(result)
                # menu_json=[]
                
                # for rs in result:
                #     print(rs)
                #     menu_json.append(dict(zip(row_headers,result)))
               
                # cursor.close()

                # conn.close()            
                # json.dumps(json_data)
                return redirect(url_for('Home',opcionesMenu=get_Menu(logged_user.id)))
                # return redirect(url_for('Home'))
           else:
                flash('Invalid Password','Danger')   
                return render_template('/auth/login.html')            
        else:
            flash('Username Not Found','Danger')
            return render_template('/auth/login.html')
        # Cerramos la conexion
        
    else:
        flash('Username and  Password Does not Exists in the Registry','Danger')
        return render_template('auth/login.html')


@app.route('/logout')
@login_required
def Logout():
    logout_user()   
    # flash('You must be logged in to view this page.','Danger')
    return redirect(url_for('Index'))



@app.route('/home/get_productos')
@login_required
def get_Products():
   # Open connection to MySQL DB
    # conn=MySQLdb.connect(host=app.config['MYSQL_HOST'],user=app.config['MYSQL_USER'],password=app.config['MYSQL_PASSWORD'],db=app.config['MYSQL_DB'])

    # instanciamos la conexion
    conn=config['conexion'].get_connection()
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

@app.route('/home/productos')
@login_required
@csrf.exempt # para que no valide el token
def add_products():
    return render_template('products.html')



@app.route('/home/proveedor_list')
@login_required
def proveedor_list():
    return render_template('proveedorlist.html')


@app.route('/home/add_proveedor')
@login_required
@csrf.exempt # para que no valide el token
def add_proveedor():
    return render_template('proveedor.html')


@app.route('/home/add_product',methods=['POST','GET'])
@login_required
@csrf.exempt # para que no valide el token
def Add_Product():
    if request.method == 'POST':
        descrip=request.form['descrip']
        price=request.form['price'] 
        cost=request.form['cost']        
        
        
        # Connect to MySQL database
        # conn = MySQLdb.connect(host=app.config['MYSQL_HOST'],
        #                        user=app.config['MYSQL_USER'],
        #                        password=app.config['MYSQL_PASSWORD'],
        #                        db=app.config['MYSQL_DB'])
        # instanciamos la conexion
        conn=config['conexion'].get_connection()
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

@app.route('/home/get_product_byId/<id>')
@login_required
def get_productByID(id):       
    # Open connection to MySQL DB
    # conn=MySQLdb.connect(host=app.config['MYSQL_HOST'],user=app.config['MYSQL_USER'],password=app.config['MYSQL_PASSWORD'],db=app.config['MYSQL_DB'])
    # instanciamos la conexion
    conn=config['conexion'].get_connection()
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

@app.route('/home/edit_product/<id>',methods=['POST','GET'])
@login_required
@csrf.exempt # para que no valide el token
def Edit_Product(id):
    if request.method == 'POST':
        descrip=request.form['descrip']
        price=request.form['price'] 
        cost=request.form['cost'] 

        # print(descrip,price,cost,id)

        # Open connection to MySQL DB
        # conn=MySQLdb.connect(host=app.config['MYSQL_HOST'],user=app.config['MYSQL_USER'],password=app.config['MYSQL_PASSWORD'],db=app.config['MYSQL_DB'])
        
        # instanciamos la conexion
        conn=config['conexion'].get_connection()
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

@app.route('/home/delete_product/<id>')
@login_required
@csrf.exempt # para que no valide el token
def Delete_Product(id):
    # Open connection to MySQL DB
    # conn=MySQLdb.connect(host=app.config['MYSQL_HOST'],user=app.config['MYSQL_USER'],password=app.config['MYSQL_PASSWORD'],db=app.config['MYSQL_DB'])
    # instanciamos la conexion
    conn=config['conexion'].get_connection()
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


# controlar errores
@app.errorhandler(401)
def no_loged(e):
    flash('You must be logged in to view this page.','Danger')
    return redirect(url_for('Login'))

@app.errorhandler(403)
def denegado(e):
    return '<h1>Servidor ha denegado su Entrada, Verificar con el Administrador</h1>',403

@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Pagina No Encontrada</h1>',404

@app.errorhandler(500)
def missingSvr(e):
    return '<h1>Servidor NO Disponible</h1>',500

# ejemplo de jsonify para enviar datos a un cliente
# @app.route('/home/get_menu/<id>')
# @login_required
def get_Menu(id):
   # Open connection to MySQL DB
    # conn=MySQLdb.connect(host=app.config['MYSQL_HOST'],user=app.config['MYSQL_USER'],password=app.config['MYSQL_PASSWORD'],db=app.config['MYSQL_DB'])
    
    # instanciamos la conexion
    conn=config['conexion'].get_connection()

        # Create cursor
    cursor = conn.cursor()
        # pasamos los valres a Select       
    # cursor.execute('SELECT id, descripcion, costo, price  FROM productos WHERE status=%s','A')
    
    result = cursor.execute('call mostrar_menuprincipal(%s)',[(id,)])
    # produtcs=cursor.fetchall()
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rvalue = cursor.fetchall() 

    json_data=[]
    for result in rvalue:
        json_data.append(dict(zip(row_headers,result)))
    
        # cerramos cursor 
    cursor.close()
        # close connection
    conn.close()
    # print(produtcs)
    
    return json.dumps(json_data)

    # return jsonify(produtcs)


# run the App
if __name__ == '__main__':
    app.config.from_object(config['development'])
    # usamos o inicializamos el token    
    csrf.init_app(app)
    # para alcanxar los errores generados
    app.register_error_handler(401,no_loged)    
    app.register_error_handler(403,denegado)  
    app.register_error_handler(404,page_not_found)
    app.register_error_handler(500,missingSvr)
    # Iniciamos la Aplicacion
    app.run(port=app.config['PORT'],debug=app.config['DEBUG'])
