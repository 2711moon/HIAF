from flask_wtf import CSRFProtect
from flask_assets import Environment
from pymongo import MongoClient

# Extensions
csrf = CSRFProtect()
assets = Environment()

# MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['employee_management']
employees_collection = db['employees']
