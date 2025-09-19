from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }
    # Create the database and tables
with app.app_context():
    db.create_all()
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        price=data['price'],
        stock=data['stock']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201
# Fetch (Read) all Products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    products_list = [product.to_dict() for product in products]
    return jsonify(products_list)
# Fetch a single Product
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict())
# Search for products with custom queries
@app.route('/products/search', methods=['GET'])
def search_products():
    name_query = request.args.get('name')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)

    query = Product.query

    if name_query:
        query = query.filter(Product.name.ilike(f'%{name_query}%'))
    if min_price:
        query = query.filter(Product.price >= min_price)
    if max_price:
        query = query.filter(Product.price <= max_price)

    products = query.all()
    products_list = [product.to_dict() for product in products]
    return jsonify(products_list)