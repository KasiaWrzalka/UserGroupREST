#  Group User  REST aplication

Aplikacja ORM z dwoma obiektami User, Group w relacji  wiele do wielu. Endpointy  REST z operacjami CRUD i wyświetleniem powiązancyh obiektów.

### Użyte technologie:
* Python 3.6
* Django 2.1
* PostgreSQL 9.6.10
* JavaScript ES6
* Django Rest Framework 3.8.2 **http://www.django-rest-framework.org/**
## Instalacja projektu
Zalecam posiadać na komputerze takie same wersje użytych technologi. <br />
Stwórz virtualenva wirtualne środowisko. <br />
Wpisz w cmd/terminalu:
```bash
git clone git@github.com:KasiaWrzalka/UserGroupREST.git
```
Wpisz w cmd/terminalu aby zainstalować potrzebne . 
```bash
pip install -r requirements.txt 
```
Baza:
```bash
python manage.py migrate
```
```bash
python manage.py makemigrations
```
Wpisz polecenie aby uruchomić serwer
```bash
python manage.py runserver
```
Projekt powinien być dostępny pod **127.0.0.1:8000**.
#### Lista endpointów i linków
###### Start
* Root API Endpoint **http://127.0.0.1:8000/**
* Schemas  **http://127.0.0.1:8000/schema/**
* Lista grup i użytkowników **http://127.0.0.1:8000/UGlist/**
###### Grupy
* Create & List **http://127.0.0.1:8000/group/**
* Retrieve & Update & Delete **http://127.0.0.1:8000/group/2/**
* powiązani użytkownicy **http://127.0.0.1:8000/group/2/users/**
###### Użytkownicy
* Create & List **http://127.0.0.1:8000/user/**
* Retrieve & Update & Delete **http://127.0.0.1:8000/user/2/**
* powiązane grupy **http://127.0.0.1:8000/user/2/groups/**
