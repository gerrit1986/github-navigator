# Summary #

This is a Django Application that enables search for GitHub repositories.
It gets results for a search term and displays five most recent repositories by
creation date and presents some details about them.


# Installation #

* Create a virtual environment
* Install or update requirements:
`$ pip install -r requirements.txt`
* Add a SECRET_KEY to settings.py
* Run the application
`$ python manage.py runserver`
* Open a browser and navigate to the served site
* Enter a search term:
<http://localhost:8000/navigator/?search_term=arrow>
* Look at the results
