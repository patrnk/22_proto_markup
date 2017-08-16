# Suppliers in Novosibirsk

Source templates used to generate the [Novosibirsk suppliers website](https://patrnk.github.io/novosibirsk_suppliers/).

# Modification

Requires Python 3.
```
pip install -r requirements.txt
python manage.py reset
python manage.py runserver
```

Be sure to run `python manage.py reset` every time one of the `.py` files changes.
The generated website will be placed in the `live_website` folder.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
