# talent-sumo-assignment

Project Description:

This project aims to create a platform for storing and managing notes. The system allows users to create, store, and share textual, audio, and video notes. The project implements functional REST APIs to provide the required functionality.

Key Features:

User Registration: Users can register on the platform by providing their name, phone number, email, and password.
User Login: Registered users can log in to the system using their phone number and password.
Note Creation: Users can create notes by providing the necessary details such as title, content, type (textual, audio, or video), and optionally share the notes with other users.
Note Querying: Users can retrieve their own notes and notes shared with them by querying the stored notes.
Note Update and Deletion: Users can update and delete their own notes.
Optional Feature:

Note Sharing: Users have the option to share their notes with other users on the platform.
The project uses SQLite as the database for testing the API functionality.

To clone the project on a different computer, follow these steps:

Open a terminal or command prompt.
Navigate to the directory where you want to clone the project.
Run the following command:
> git clone git@github.com:heyman242/talent-sumo-assignment.git

Navigate to the project directory using the cd command. For example:

> cd /path/to/project/directory

Create a virtual environment (optional but recommended) to isolate the project dependencies.
Run the following command:
On Windows: > python -m venv env
On macOS and Linux: > python3 -m venv env

Activate the virtual environment:
On Windows: > env\Scripts\activate

On macOS and Linux: > source env/bin/activate

Install the project dependencies. 
Run the following command:

> pip install -r requirements.txt
This will install the required packages and libraries.

Apply migrations to create the necessary database tables. Run the following command:

> python manage.py migrate

Start the development server:

> python manage.py runserver

This will start the server locally.
Access the project in your web browser by visiting http://localhost:8000/ or the URL mentioned in the terminal.

You can now interact with the project through the provided REST APIs.

Make sure you have Python and pip installed on your computer before running the project. Adjust the commands accordingly if you're using different tools or environments.
