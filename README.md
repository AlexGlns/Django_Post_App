# H1 Django Post App

Create a virtual environment: This is a recommended practice for Python development. It allows you to isolate your project's dependencies from the system's Python packages.

bash
python3 -m venv myenv
This command will create a virtual environment named myenv in the current directory.

Activate the virtual environment:

bash
source myenv/bin/activate
Once activated, your shell prompt will change, indicating that you're now working within the virtual environment.

Install Django within the virtual environment:

bash
pip install Django
This command will install Django only within the virtual environment, keeping it isolated from the system-wide packages.

Check Django installation:

bash
django-admin --version
This should display the installed Django version.

Deactivate the virtual environment:

bash
deactivate

Django Start Projecet:
django-admin startproject "project name"

Start Server:
python3 manage.py runserver
