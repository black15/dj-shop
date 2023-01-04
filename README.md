<br/>
<p align="center">
  <a href="https://github.com/black15/dj-shop ">
    <img src="https://dotmobo.github.io/images/djangopony.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Django E-Shop</h3>

  <p align="center">
    E-Commerce Website Built With Python Django. 
    <br/>
    <br/>
    <a href="https://github.com/black15/dj-shop /issues">Request Feature</a>
  </p>

## About The Project

![Screen Shot](images/screenshot.png)

In this project i used the following technologies:
***Backend***: Python Djnago (Only).
***Frontend***: Javascript, TailwindCss.

I plan to work on another *e-commerce project* using deferent technologies for both **Backend** & **Frontend** (Hopefuly with a team).

## Getting Started

In order for this website to work in your machine (localhost) follow these steps:

### Prerequisites

* python
* tailwind (npm)

### Installation

1. Clone the repo
```sh
git clone https://github.com/black15/dj-shop.git
cd dj-shop/
```

2. Setup a new python virtual env
```sh
python -m venv venv
source venv/bin/activate
```

3. Install the required python libraries
```sh
pip install -r requirements.txt
```

4. Install and create the config file for TailwindCss
```sh
npm install -D tailwindcss
npx tailwindcss init

python manage.py tailwind install
```

5. Setup SQLite3
```sh
python manage.py migrate
```

6. **Important !** Create Stripe Account and Copy the Secret and Public Key to ***djshop/.env***
```env
STRIPE_SECRET_KEY='YOUR STRIPE SECRET KEY HERE'
STRIPE_PUBLISHABLE_KEY='YOUR STRIPE PUBLIC KEY HERE'
BASE_URL='http://localhost:8000/'
```
7. ***Optional*** Create superuser
```sh
python manage.py createsuperuser
```

## Usage
*Launch 2 Terminals to run both django web server and tailwindcss.*

***Django***
```sh
python manage.py runserver
```
***Tailwind***
```sh
python manage.py tailwind start
```

## Authors

* [Oussama](https://www.facebook.com/unknownkid.18)

</p>
