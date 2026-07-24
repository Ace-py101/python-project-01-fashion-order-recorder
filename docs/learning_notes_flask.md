---

# Learning Update - Introduction to Flask

This section documents the beginning of the web version of the Fashion House Manager project.

---

# What is Flask?

Flask is a lightweight Python web framework.

Instead of interacting with users through the terminal, Flask allows Python applications to communicate with web browsers.

Old workflow:

```
User
 │
Keyboard
 │
Python
 │
Terminal
```

New workflow:

```
User
 │
Browser
 │
Flask
 │
Python
 │
JSON Storage
```

The Python code remains mostly the same.

Only the user interface changes.

---

# Flask Application

A Flask application begins with:

```python
from flask import Flask

app = Flask(__name__)
```

Meaning:

- Import the Flask framework.
- Create a Flask application object.

The application object manages routes and handles incoming browser requests.

---

# Routes

Routes connect a URL to a Python function.

Example:

```python
@app.route("/")
def home():
    return "Welcome"
```

When the browser visits:

```
/
```

Flask executes:

```python
home()
```

and sends the returned result back to the browser.

---

# Route Decorators

Example:

```python
@app.route("/orders")
```

This decorator tells Flask:

"When someone visits /orders, execute the function immediately below."

Decorators attach additional behavior to functions without changing the function itself.

---

# render_template()

Instead of returning plain text, Flask can return HTML pages.

Example:

```python
return render_template("index.html")
```

Flask automatically looks inside the:

```
templates/
```

folder.

---

# Templates Folder

The templates folder stores HTML pages.

Example:

```
templates/

index.html
orders.html
create_order.html
```

Flask automatically searches this folder whenever render_template() is called.

---

# Static Folder

The static folder stores resources that normally do not change.

Examples:

- CSS
- JavaScript
- Images
- Icons

Example:

```
static/
    style.css
```

---

# Jinja Templates

Flask uses Jinja as its template engine.

Jinja allows Python-like syntax inside HTML.

Example:

```html
{% block content %}
```

Example:

```html
{{ variable }}
```

Jinja is responsible for combining Python data with HTML pages.

---

# Template Inheritance

Instead of repeating the same HTML on every page, Flask allows templates to inherit from a base template.

Example:

```
base.html
      │
      ├── index.html
      ├── orders.html
      └── create_order.html
```

Each page shares:

- Header
- Navigation
- CSS

Only the page content changes.

This follows the DRY principle (Don't Repeat Yourself).

---

# HTML Forms

Terminal application:

```python
input()
```

Web application:

```html
<form>
```

HTML forms collect information from users.

Each input field contains a name attribute.

Example:

```html
<input
    type="text"
    name="customer_name">
```

The name attribute identifies the submitted data.

---

# GET Request

GET requests ask the server for information.

Example:

```
Browser
      │
      ▼
Show me the Create Order page.
```

Flask responds by displaying an HTML page.

---

# POST Request

POST requests send data to the server.

Example:

```
Browser
      │
Completed Form
      ▼
Flask
```

POST is commonly used for:

- Creating records
- Updating records
- Login forms

---

# request.form

In the terminal:

```python
customer_name = input()
```

In Flask:

```python
customer_name = request.form["customer_name"]
```

Both retrieve user input.

The difference is where the data comes from.

Terminal:

```
Keyboard
```

Flask:

```
HTML Form
```

---

# Separation of Concerns

The project architecture is now divided into layers.

```
Browser
        │
        ▼
Flask Routes
        │
        ▼
Business Logic
        │
        ▼
Storage
```

Each layer has one responsibility.

This makes the application easier to maintain and extend.

---

# Current Flask Progress

Completed:

- Flask installation
- Development server
- Application object
- Routes
- Navigation
- Templates
- Template inheritance
- HTML forms
- GET requests
- POST requests
- request.form

Upcoming:

- Connect forms to existing business logic.
- Reuse validation.py.
- Save orders from the browser.
- Display JSON data inside HTML pages.
