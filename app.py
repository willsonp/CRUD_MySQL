from flask import Flask,render_template, request, redirect, url_for, flash
import MySQLdb.cursors

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
   # Open connection to MySQL DB
    conn=MySQLdb.connect(host=app.config['MYSQL_HOST'],user=app.config['MYSQL_USER'],password=app.config['MYSQL_PASSWORD'],db=app.config['MYSQL_DB'])

        # Create cursor
    cursor = conn.cursor()
        # pasamos los valres a Select       
    cursor.execute('SELECT id, descripcion, price, costo FROM productos WHERE status=%s','A')
    produtcs=cursor.fetchall()
        # cerramos cursor 
    cursor.close()
        # close connection
    conn.close()
    # print(produtcs)
    return render_template('index.html',products=produtcs)

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
        cursor.execute('INSERT INTO productos (descripcion,price,costo) VALUES (%s,%s,%s)',(descrip,price,cost))
        # almacenamos los cambios de manera permanente        
        conn.commit()
        # cerramos cursor 
        cursor.close()
        # close connection
        conn.close()

        #  para enviar un mesaje al usuario
        flash('Product Added successfully','success')
        
        # redireccionar al index                
        return redirect(url_for('Index'))

@app.route('/get_product_byId/<id>')
def get_productByID(id):       
    # Open connection to MySQL DB
    conn=MySQLdb.connect(host=app.config['MYSQL_HOST'],user=app.config['MYSQL_USER'],password=app.config['MYSQL_PASSWORD'],db=app.config['MYSQL_DB'])

    # Create cursor
    cursor = conn.cursor()
    # pasamos los valres a Select       
    cursor.execute('SELECT id, descripcion, price, costo FROM productos WHERE id=%s',(id))
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
        cursor.execute('UPDATE productos SET descripcion=%s,price=%s,costo=%s WHERE id=%s',(descrip,price,cost,id))
        # ejecutamos la consulta
        conn.commit()
        # cerramos cursor 
        cursor.close()
        # close connection
        conn.close()
        #  para enviar un mesaje al usuario
        flash('Product Edited successfully','success')
       
    return redirect(url_for('Index'))

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

    return redirect(url_for('Index'))

# run the App
if __name__ == '__main__':
    app.run(port=3000,debug=True)
