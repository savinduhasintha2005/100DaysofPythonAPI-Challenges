# 🚀 Challenge 5: Temperature Converter API
---
A simple REST API built with **FastAPI** that converts temperatures between **Celsius**, **Fahrenheit**, and **Kelvin**.
---

## 📚 What You'll Learn

* ✅ Query parameters
* ✅ Mathematical calculations
* ✅ Returning JSON responses
* ✅ Input validation
* ✅ API documentation with Swagger UI
* ✅ Working with multiple temperature units

---

## 🛠 Tech Stack

* Python 3
* FastAPI
* Uvicorn

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/temperature_converter_api.git
cd temperature_converter_api
```

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn
```

Or create a `requirements.txt` file:

```txt
fastapi
uvicorn
```

Then install:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

Server starts at:

```
http://127.0.0.1:8000
```

---

## 🏠 Home Endpoint

### Request

```http
GET /
```

### Response

```json
{
  "message": "Welcome to Temperature Converter API"
}
```

---

# 🌡 Temperature Conversion Endpoint

## Request

```http
GET /convert
```

### Query Parameters

| Parameter   | Type   | Description                               |
| ----------- | ------ | ----------------------------------------- |
| temperature | float  | Temperature value                         |
| from_unit   | string | Source unit (celsius, fahrenheit, kelvin) |
| to_unit     | string | Target unit (celsius, fahrenheit, kelvin) |

---

## Examples

### Celsius → Fahrenheit

Request:

```http
GET /convert?temperature=100&from_unit=celsius&to_unit=fahrenheit
```

Response:

```json
{
  "input_temperature": 100,
  "from_unit": "celsius",
  "to_unit": "fahrenheit",
  "converted_temperature": 212.0
}
```

---

### Fahrenheit → Celsius

Request:

```http
GET /convert?temperature=98.6&from_unit=fahrenheit&to_unit=celsius
```

Response:

```json
{
  "input_temperature": 98.6,
  "from_unit": "fahrenheit",
  "to_unit": "celsius",
  "converted_temperature": 37.0
}
```

---

### Kelvin → Celsius

Request:

```http
GET /convert?temperature=300&from_unit=kelvin&to_unit=celsius
```

Response:

```json
{
  "input_temperature": 300,
  "from_unit": "kelvin",
  "to_unit": "celsius",
  "converted_temperature": 26.85
}
```

---

## 📖 Interactive API Documentation

FastAPI automatically generates Swagger documentation.

Open:

```
http://127.0.0.1:8000/docs
```

You can test all endpoints directly from your browser.

---

## 🧪 Sample URL

```
http://127.0.0.1:8000/convert?temperature=100&from_unit=celsius&to_unit=fahrenheit
```
---

## ⭐ Features

* Convert Celsius ↔ Fahrenheit
* Convert Celsius ↔ Kelvin
* Convert Fahrenheit ↔ Kelvin
* Supports decimal values
* Automatic Swagger UI documentation
* Simple and beginner-friendly code

---



with your actual GitHub repository URL before pushing the project.
