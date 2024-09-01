# Parking-Space-Detector
This is my 6th Semester Project

# How to setup Database

1. Download and Install XAMPP to proceed toward testing the code locally:
    
    Go to the following URL for downlaod:
        [Download_here](https://sourceforge.net/projects/xampp/)

    Go to the following link for tutorial of installation of XAMPP:
        [Youtube_Video](https://www.youtube.com/watch?v=-f8N4FEQWyY)

2. Install Apache server and MYSQL inside of XAMPP

3. Run Apache server and MYSQL

4. Create Db inside of MYSQL/PHPMYADMIN
    - Go to admin of mysql [Local_host](http://localhost/phpmyadmin/)
    - Create a database named **psds**
    - Import the provided database i.e. **\Parking-Space-Detector\Database\psds.sql**

5. Admin id: sanks@mail.com
   Pass: 1234


# How to run this code

1. Create a New Virtual Environment:

    Run the following command in your project directory to create a new virtual environment:

        python -m venv venv

2. Activate the Virtual Environment:

    Activate the newly created virtual environment:

        venv\Scripts\activate    

3. Install the Dependencies:

    Install your project’s dependencies using:

        pip install -r requirement.txt

4. Run the code:

    Run your python cv code using:

        python app_main.py                 

    Run your flask code using:

        flask run    
        **CTRL+C to close the flask app in terminal**
        **Q to end the cv window of the python app** 