Inventory management is designed to implement asset management system for an engineering organization comprising multiple departments. This system is focused on tracking procured products, their allocation to staff members, and the recording of pertinent information, including the staff member's name, department, and other relevant details.ensuring accurate records of the allocation process.

clone the project
``` git clone https://github.com/awahidanon/inventory-management.git```

Create a virtual environment 
``` python3 -m venv env ``` 

Activate virtual environment for mac or linux 
``` source env/bin/activate  ``` 

Activate virtual environment for Windows
```env\Scripts\activate```
 
create .env file in main directory and add Database credentials, security_key and debugging

create MySQL database 

install the requirements
```pip install -r requirements.txt```

make migrations
```python manage.py makemigrations```
```python manage.py migrate```

To run the App
```python manage.py runserver ```
