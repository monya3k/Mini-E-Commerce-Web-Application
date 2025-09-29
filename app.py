from flask import Flask, render_template, redirect, url_for, session
from routes.users.users import users_bp
from routes.products.products import products_bp
from routes.orders.orders import orders_bp

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Register blueprints
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(products_bp, url_prefix="/products")
app.register_blueprint(orders_bp, url_prefix="/orders")

@app.route("/")
def home():
    return redirect(url_for("users.login"))

if __name__ == "__main__":
    app.run(debug=True)
