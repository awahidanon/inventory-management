It is designed to implement product management for an engineering organization comprising multiple departments. This system is focused on tracking procured products, their allocation to staff members, and the recording of pertinent information, including the staff member's name, department, and other relevant details.ensuring accurate records of the allocation process.

- it generates invoice and Qr codes for each assigned products.
- it exports daily, weekly and monthly assigned products.

- clone the project
``` git clone https://github.com/awahidanon/inventory-management.git```

- Create a virtual environment 
``` python3 -m venv env ``` 

- Activate virtual environment for mac or linux 
``` source env/bin/activate  ``` 

- Activate virtual environment for Windows
```env\Scripts\activate```
 
- create .env file in main directory and add Database credentials, security_key and debugging

- create MySQL database 

- install the requirements
```pip install -r requirements.txt```

- make migrations
```python manage.py makemigrations```
```python manage.py migrate```

- run the App
```python manage.py runserver ```


<img width="1531" alt="Screenshot 2024-01-27 at 4 53 03 in the afternoon" src="https://github.com/awahidanon/inventory-management/assets/92226916/9c8d6b55-40ab-4644-bb05-71567d945ae6">
<img width="1728" alt="Screenshot 2024-01-27 at 5 31 02 in the afternoon" src="https://github.com/awahidanon/inventory-management/assets/92226916/e26717e2-215f-4457-b389-6e6940d69f82">
<img width="1712" alt="Screenshot 2024-02-23 at 11 18 01 in the morning" src="https://github.com/awahidanon/inventory-management/assets/92226916/22ef28a2-b2d5-4587-a0c1-a2c9e61e7f7a">
