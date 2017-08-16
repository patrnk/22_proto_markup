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

# Conventions

All extendable template names start with double underscores, all includable templates start with one underscore and all final templates start with no underscore. The CSS files for all of the templates do not start with underscores.

All indents are two spaces long.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
