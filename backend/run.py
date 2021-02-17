from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/data.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)



class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    product_name=db.Column(db.String)
    product_about=db.Column(db.String)
    # product_price=db.Column(db.Integer)
    # product_photo=db.Column(db.String)

     

@app.route('/')
def products():
    products=Product.query.all()
    return render_template('index.html',all=products)

@app.route('/product/<int:id>',methods=['GET','POST'])
def product(id):
    single=Product.query.get(id)
    return render_template('product.html',product=single)

# Admin Routes

@app.route('/admin')
def adminIndex():
    products=Product.query.all()
    return render_template('admin/index.html',products=products)

@app.route('/admin/add',methods=['GET','POST'])
def adminAdd():
    if request.method == 'POST':
        product=Product(
            product_name=request.form['name'],
            product_info=request.form['info'],
            product_about=request.form['about'], 
            product_price=request.form['price']
            )
        db.session.add(product)
        db.session.commit() 
        return redirect('/admin')   
    return render_template('admin/add.html')    
    

if __name__ == '__main__':
    app.run(debug=True)