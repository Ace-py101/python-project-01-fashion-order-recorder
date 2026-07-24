---

# Flask Web Application Migration (Current Progress)

The project has officially begun transitioning from a terminal-based application into a web application using Flask.

The existing Python business logic is being reused instead of rewritten. The goal is to separate the application's presentation layer (HTML pages) from its business logic and storage layer.

---

## Why Flask?

Flask allows the application to:

- Run in a web browser instead of the terminal.
- Accept user input through HTML forms.
- Display information as web pages.
- Reuse existing Python modules.
- Prepare the project for deployment on Render.
- Serve as the backend for future Android and iOS applications.

---

## Flask Installation

Flask 3.1.3 was installed successfully.

The application currently runs using:

```bash
python app.py
```

Flask starts a local development server at:

```text
http://127.0.0.1:5000
```

---

## New Project Structure

```
python-project-01-fashion-order-recorder/

│
├── app.py
├── main.py
├── orders.py
├── storage.py
├── validation.py
├── receipt.py
├── orders.json
│
├── templates/
│      base.html
│      index.html
│      orders.html
│      create_order.html
│
└── static/
       style.css
```

---

## Application Layers

The project now follows a layered architecture.

```
Browser
    │
    ▼
Flask Routes (app.py)
    │
    ▼
Business Logic (orders.py)
    │
    ▼
Storage (storage.py)
    │
    ▼
orders.json
```

Each layer has a single responsibility.

---

## Routes Implemented

Current routes:

| Route | Purpose |
|--------|----------|
| / | Home Page |
| /orders | Orders Menu |
| /orders/create | Create Order |
| /orders/view | View Orders (Placeholder) |
| /orders/search | Search Order (Placeholder) |
| /orders/edit | Edit Order (Placeholder) |
| /orders/delete | Delete Order (Placeholder) |

---

## HTML Templates

The project now uses Flask templates.

Current templates:

- base.html
- index.html
- orders.html
- create_order.html

The base template contains:

- Page title
- Navigation
- Common layout

Other templates inherit from it using Jinja.

---

## Current Progress

Completed:

- Flask installation
- Flask application setup
- Development server
- Project restructuring
- Route creation
- Navigation between pages
- Template inheritance
- HTML Create Order form
- Initial form submission using POST

Next milestone:

- Connect HTML forms to existing Python business logic.
- Save submitted orders directly into orders.json.
- Replace terminal input() with request.form.
