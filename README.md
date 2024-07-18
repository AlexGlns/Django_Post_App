# Django Post App

**Create a virtual environment:** This is a recommended practice for Python development. It allows you to isolate your project's dependencies from the system's Python packages.

bash <br />
**:~$ python3 -m venv myenv** <br />
This command will create a virtual environment named myenv in the current directory.

**Activate the virtual environment:**

bash <br />
**:~$ source myenv/bin/activate** <br />
Once activated, your shell prompt will change, indicating that you're now working within the virtual environment. <br />
<br />
### Install Django within the virtual environment:

bash <br />
**:~$ pip install Django** <br />
This command will install Django only within the virtual environment, keeping it isolated from the system-wide packages.<br />

**Check Django installation:** <br />
bash <br />
**:~$ django-admin --version** <br />
This should display the installed Django version. <br />

Deactivate the virtual environment: 
<br />
bash <br />
**:~$ deactivate** <br />
<br />
### Django Start Projecet:
**:~$ django-admin startproject "project name"**
<br />
**Start Server:** <br />
**:~$ python3 manage.py runserver** <br />
