# Producer - Consumer

## Getting started

Cloning repository:
```
git clone git@github.com:Kozatskiy-Artem/producer-consumer.git
```
Or
```
git clone https://github.com/Kozatskiy-Artem/producer-consumer.git
```

If you haven't previously created a project with a virtual environment, for example, in PyCharm, you can do it using the following commands:

To create a virtual environment, execute the command:
```
python -m venv venv
```

To activate the virtual environment in Unix-like systems, execute the command:
```
source venv/bin/activate
```

To activate the virtual environment in Windows, execute the command:
```
venv\Scripts\activate
```
This will allow you to create and activate a virtual environment for your project.

Install the necessary dependencies:
```
pip install -r requirements.txt
```

Apply migrations:
```
python manage.py migrate
```

### Project Launch

Start the Django development server:
```
python manage.py runserver
```

Open your web browser and navigate to http://localhost:8000/.
