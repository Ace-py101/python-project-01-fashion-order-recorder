from flask import Flask, render_template, request

from storage import save_order, generate_order_id

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/orders")
def orders():
    return render_template("orders.html")

@app.route("/orders/create", methods=["GET", "POST"])
def create_order_page():

    if request.method == "POST":
    
        order = {
            "order_id": generate_order_id(),
            "customer_name": request.form["customer_name"],
            "phone_number": request.form["phone_number"],
            "garment_type": request.form["garment_type"],
            "quantity": int(request.form["quantity"]),
            "delivery_date": request.form["delivery_date"],
            "price": int(request.form["price"]),
            "deposit": int(request.form["deposit"])
        }
    
        order["balance"] = order["price"] - order["deposit"]
    
        save_order(order)
    
        return f"""
        <h2>Order Saved Successfully!</h2>
    
        <p>Order ID: {order['order_id']}</p>
    
        <a href="/orders/create">
            Create Another Order
        </a>
        """

    return render_template("create_order.html")

@app.route("/orders/view")
def view_orders_page():
    return "<h2>View Orders Page</h2>"


@app.route("/orders/search")
def search_order_page():
    return "<h2>Search Order Page</h2>"


@app.route("/orders/edit")
def edit_order_page():
    return "<h2>Edit Order Page</h2>"


@app.route("/orders/delete")
def delete_order_page():
    return "<h2>Delete Order Page</h2>"

if __name__ == "__main__":
    app.run(debug=True)
