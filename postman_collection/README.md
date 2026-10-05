## Postman collection for API testing

The `foodgram.postman_collection.json` file contains a Postman collection: a set of prepared requests for testing the API.

## Preparing the Django project to run the collection:
1. Make sure the virtual environment is created and activated, and the project dependencies are installed.
2. To test the API locally, set SQLite3 as the database in `settings.py`
and set `DEBUG = True`.
3. Run migrations; create at least 2 ingredients and 3 tags in the database.
4. Start the development server.

*After preparing the project, make a copy of the `db.sqlite3` database file:
it may come in handy if something goes wrong.*

## Importing the collection into Postman:

1. Open Postman.
2. In the top left corner, click `File` -> `Import`.
3. In the popup, drag in the collection file or choose it with the file browser.
Import the `foodgram.postman_collection.json` file into Postman.

## Running the collection:

1. After the previous steps, the imported collection appears in the `Collections` tab on the left side of the Postman window.
Hover over it, click the three dots next to the collection name and choose `Run collection` from the dropdown. The list of requests in the collection appears in the center of the screen,
and the run settings menu appears on the right.
2. In the right menu, turn on `Persist responses for a session` so you can view the API responses after the run.
3. Click `Run <collection name>`.
4. The results of the run and its tests appear in the center of the screen. You can filter failed tests with the `Failed` tab.
Click a test to see the details of the request and the response.

## Running the collection again:
1. Go to the `postman_collection` directory in the project root.
2. With the project's virtual environment activated, run the script that removes the objects created by the collection from the database: `bash clear_db.sh`.  
The script deletes all users and objects created during the previous run (as long as `on_delete` is configured correctly in the project's models).
  
If cleaning the database fails, use the backup copy of `db.sqlite3`: replace the current database file with it.
You can also recreate the database and fill it with the objects the collection needs (as described in step 3 of _Preparing the Django project to run the collection_).

## Postman limits
The free version of Postman has a technical limit: you can run a collection without interruption 25 times a month.  
After that, Postman still runs collections, but a run may sometimes be blocked for 30 seconds (occasionally twice in a row) while the app offers you the paid version.  
You can buy the paid version or just keep using the free one and wait out the occasional ad.

There are no limits on sending individual requests.
