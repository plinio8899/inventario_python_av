# Inventory Management System

This is a modular Python-based CLI application designed to manage a product inventory. It supports core CRUD operations, statistical analysis, and data persistence through CSV files with robust error handling and data validation.

---

## 🛠 Features

* **Modular Architecture:** Divided into logic (`servicios.py`), persistence (`archivos.py`), and the main interface (`app.py`).
* **Full CRUD:** Add, View, Search, Update, and Delete products.
* **Smart Statistics:** Calculates total units, total inventory value, and identifies outliers (most expensive/highest stock).
* **Data Persistence:**
    * **Export:** Saves inventory to `inventory.csv`.
    * **Import:** Loads data with strict validation (header checks, type conversion, and non-negative value enforcement).
* **Flexible Loading:** Choose between **overwriting** the current inventory or **merging** data (summing quantities and updating prices).

---

## 📁 Project Structure

* `app.py`: The entry point. Contains the main menu and user interaction logic.
* `servicios.py`: Contains the business logic and inventory manipulation functions.
* `archivos.py`: Handles file I/O operations and CSV parsing/validation.
* `inventory.csv`: (Generated) Stores the persistent data.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed.

### Execution
1. Clone or download the project files into a single folder.
2. Open your terminal or command prompt in that directory.
3. Run the application:
   ```bash
   python app.py
