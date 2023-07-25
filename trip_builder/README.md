# Trip Builder

Choose vacation plans from trip legs stored in the system.

## Quick Start

If you want to hack on this, it's best to follow the detailed steps in [the accompanying blog post](../). But to try it out quickly, all you need is python 3.

### Mac or Linux

```
python3 -mvenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 ./manage.py migrate
python3 ./manage.py createsuperuser
python3 ./manage.py runserver
```

then open a web browser to http://localhost:8000/

### Windows

These are from memory and may be wrong.

```
py3 -mvenv venv
venv\scripts\activate
pip3 install -r requirements.txt
py3 .\manage.py migrate
py3 .\manage.py createsuperuser
py3 .\manage.py runserver
```

then open a web browser to http://localhost:8000/
