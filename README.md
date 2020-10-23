## Instructions on how to set up the backend and frontend to run the application

### Dependencies

- pipenv
- flask
- requests
- nltk
- pandas
- numpy

### Step-by-step instructions

1. pipenv is used to create the virtual environment of the project. Please use command **pip3 install pipenv** to install pipenv on your machine. 
2. Please create a project directory (such as dadjock) and run **pipenv install** in the project directory to setup the pipenv environment.
3. Run **pipenv shell** to launch the virtual environment in the directory. (Type **exit** if you want to go back to the regular version of the terminal.)
4. Install dependencies in the pipenv environment:
   - **pipenv install flask**
   - **pipenv install requests**
   - **pipenv install nltk**
   - **pipenv install pandas**
   - **pipenv install numpy**
5. Run **flask run** in the terminal and go to **http://127.0.0.1:5000/**. The resulting term counting table will be shown up there. 
