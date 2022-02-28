### Description:
RESTful API with Docker containerisation as a coding challenge.
#### As a user you can:
  * get, create, update and delete items;
  * filter data by date range.
#### As a developer you can:
  * run the project in Docker containers;
  * use Django admin account for editing data.
#### Techs:
  * django==2.2.6
  * python-dotenv==0.13.0
  * djangorestframework==3.11.0
  * django-filter==21.1
  * django-colorfield==0.6.3
  * gunicorn==20.0.4
  * psycopg2-binary==2.8.5
### How to run the project local:
Clone the repo and go to the backend directory:
```bash
git clone https://github.com/DmitriiPugachev/sms_digital_coding_challenge
```
```bash
cd sms_digital_coding_challenge/backend
```
Create ```.env``` file in the root project directory with variables like in ```.env.example``` file.

Install Docker. [This gide](https://docs.docker.com/engine/install/ubuntu/) helps you.

Go to infrastructure directory:
```bash
cd sms_digital_coding_challenge/infra
```
Build an image and run all the containers:
```bash
docker-compose up -d --build
```
Go to the web container:
```bash
docker exec -it infra_web_1 bash
```
Apply migrations:
```bash
python manage.py migrate --noinput
```
Collect static files:
```bash
python manage.py collectstatic
```
Create a superuser:
```bash
python manage.py createsuperuser
```
Load data from JSON file to the DB:
```bash
python manage.py load_data
```
### Links
[redoc](http://localhost/redoc/) this link is for local usage.

[admin](http://localhost/admin/) this link is for local usage.
### Author
Dmitrii Pugachev