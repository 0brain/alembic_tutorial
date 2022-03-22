### The Migration Environment¶
* yourproject/
    * alembic/
        * env.py
        * README
        * script.py.mako
        * versions/
            * 73f0dbef66c4_add_a_column.py
            * 6657f52fd5db_create_account_table.py
### Creating an Environment¶
* $ cd /path/to/yourproject
* $ source /path/to/yourproject/.venv/bin/activate   # assuming a local virtualenv
* $ alembic init alembic
### Editing the .ini File
sqlalchemy.url = postgresql://nazar:15946837135@localhost/flask_db
### Create a Migration Script
* $ alembic revision -m "create account table"
### Running our First Migration
* $ alembic upgrade head

### Running our Second Migration
* $ alembic revision -m "Add a column"
* $ alembic upgrade head

### Partial Revision Identifiers
* $ alembic upgrade 73f
* $ alembic downgrade 665

### Relative Migration Identifiers
* $ alembic upgrade +1
* $ alembic downgrade -1
* $ alembic upgrade 665+1

### Getting Information
* $ alembic current
* $ alembic history --verbose

### Viewing History Ranges¶
* $ alembic history -r6657f5:73f0db
* $ alembic history -r-1:current
* $ alembic history -r6657f5:

### Downgrading
* $ alembic downgrade base
* $ alembic upgrade head