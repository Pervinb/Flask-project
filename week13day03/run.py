from flask import Flask,redirect,request,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
app=Flask(__name__)
# database and migration object creation
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/data.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

#define model
class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String)
    content=db.Column(db.String)




 
# app routes
@app.route('/')
def index():
    allProducts=Product.query.all()
    return render_template('app/index.html',content=allProducts)

@app.route('/single/<int:id>',methods=['GET','POST'])
def singleProduct(id):
    singleProduct=Product.query.get(id)
    return render_template('app/product.html',product=singleProduct)

# admin routes
@app.route('/admin')
def adminIndex():
    return render_template('admin/index.html')

@app.route('/admin/add',methods=['GET','POST'])
def adminAddProduct():
    if request.method=='POST':
        product=Product(title=request.form['productHeading'],content=request.form['productContent'])
        db.session.add(product)
        db.session.commit()
        return redirect('/admin/all')
    return render_template('admin/addProduct.html')

@app.route('/admin/all')
def adminAllProducts():
    allProducts=Product.query.all()
    return render_template('admin/allProducts.html',content=allProducts)

if __name__=='__main__':
    app.run(debug=True)
    manager.run()    
