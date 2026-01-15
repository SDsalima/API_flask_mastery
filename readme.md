API Flask Mastery



 ---------------------------Overview-------------------------------------
API Flask Mastery is a modular Flask project designed to demonstrate RESTful API development with:
- Custom CLI commands for database management (db_create, db_drop, db_seed)
- CRUD routes for managing countries (add, update, delete)
- Integration with Flask‑Marshmallow for clean JSON serialization
- Organized project structure for scalability and maintainability

--------------------------Costom CLI commands---------------------------

flask db_create   # Create all tables
flask db_drop     # Drop all tables
flask db_seed     # Seed database with sample data

---------------------------------API Endpoints-----------------------------------

| POST | /add_country |  add new country
| PATCH | /update_country | update existing country
|  DELETE | /delete_country |delete country   
| GET | /countries |  list all contries


------------------------------Technologies Used------------------------------------

- Flask – Web framework
- Flask‑SQLAlchemy – ORM for database models
- Flask‑Marshmallow – Serialization & validation
- MySQL – Database backend
