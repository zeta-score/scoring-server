# Zeta Score - Scoring Server

This repository will hold the code of a Python Flask server that implements the scoring service for the Zeta Score application.

This server fetches transactional data, performs analysis, and outputs a score that is published to the blockchain.

## Setting Up Local Instance

You must have Python 3.7.2 to run the server.

Set up a virtualenv and activate it

`$ source venv/bin/activate`

Your console should now look like

`(venv) $ `

Then install the pip requirements 

`$ pip install -r requirements.txt`

Now just start the server!

`$ python app.py`
