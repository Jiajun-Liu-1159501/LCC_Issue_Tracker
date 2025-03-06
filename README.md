# Lincoln Community Campground (06 March 2025)

This sample app demonstrates a simple login system that allows users to
register, log in, and view pages specific to their user role. Those pages don't
really do anything: it's just a simplified example to share some basic tools
and techniques you might need when building a real-world login system.

There are three user roles in this system:
- **Customer**
- **Staff**
- **Admin**

Anyone who registers via the app will be a **Customer**. The only way to create
**Staff** or **Admin** accounts in this simple app is to insert them directly
into the database. Hey, we didn't say this app was complete!

## Getting this Project Running

To run the example yourself, you'll need to:

1. Open the project in Visual Studio Code.
2. Create yourself a virtual environment.
3. Install all of the packages listed in requirements.txt (Visual Studio will
   offer to do this for you during step 2).
4. Use the [Database Creation Script](create_database.sql) to create your own
   copy of the **loginexample** database.
5. Use the [Database Population Script](populate_database.sql) to populate
   the **loginexample** ***users*** table with example users.
6. Modify [connect.py](loginapp/connect.py) with the connection details for
   your local database server.
7. Run [The Python/Flask application](run.py).

At that point, you should be able to register yourself a new **customer**
account or log in using one of the **customer**, **staff**, or **admin**
accounts listed in the [Database Population Script](populate_database.sql).

Enjoy!