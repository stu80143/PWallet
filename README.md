# [Flask Berry Bootstrap 5](https://appseed.us/product/berry-dashboard/flask/)

Open-source **[Flask Dashboard](https://appseed.us/admin-dashboards/flask/)** project crafted on top of **Berry**, an open-source `Bootstrap 5` design from `CodedThemes`.
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. `Berry` has an easy and intuitive responsive design whether it is viewed on retina screens or laptops.

- 👉 [Flask Berry](https://appseed.us/product/berry-dashboard/flask/) - `Product page`
- 👉 [Flask Berry](https://flask-berry.onrender.com) - `LIVE Demo`

<br />

## Features

> `Have questions?` Contact **[Support](https://appseed.us/support/)** (Email & Discord) provided by **AppSeed**

| Free Version                          | [PRO Version](https://appseed.us/product/berry-dashboard-pro/flask/)          | [Custom Development](https://appseed.us/custom-development/) |  
| --------------------------------------| --------------------------------------| --------------------------------------|
| ✓ **Up-to-date dependencies**             | **Everything in Free**, plus:                                        | **Everything in PRO**, plus:       |
| ✓ Best Practices                          | ✅ **Premium Bootstrap 5 Design**                                    | ✅ **1mo Custom Development**     | 
| ✓ DB: SQLite, MySql                       | ✅ **PRO Support** - [Email & Discord](https://appseed.us/support/)  | ✅ **Team**: PM, Developer, Tester        |
| ✓ DB Tools: ORM, Flask-Migrate            | ✅ `Private REPO Access`                                             | ✅ Weekly Sprints                 |
| ✓ Session-Based authentication            |  -                                                                    | ✅ Technical SPECS               |
| ✓ `Docker`                                |  -                                                                    | ✅ Documentation                  |
| ✓ `CI/CD` Flow via Render                 |  -                                                                    | ✅ **30 days Delivery Warranty**  |
| ✓ `Free Support`                          |  -                                                                    |  -                                 |
| ---------------------------------         | ---------------------------------                                     | ---------------------------------  |
| ✓ [LIVE Demo](https://flask-berry.onrender.com)  | 🚀 [LIVE Demo](https://flask-berry-pro.onrender.com) `PRO` | 🛒 `Order`: **[$3,999](https://appseed.gumroad.com/l/rocket-package)** (GUMROAD) |

![Berry Bootstrap 5 - Dark-Mode ready, Open-source Template.](https://user-images.githubusercontent.com/51070104/207091062-e805b36c-663a-4a01-acb8-9c55ab914f4f.jpg)

<br /> 

## ✨ Start the app in Docker

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/flask-berry-dashboard.git
$ cd flask-berry-dashboard
```

<br />

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## ✨ How to use it

> Download the code 

```bash
$ git clone https://github.com/app-generator/flask-berry-dashboard.git
$ cd flask-berry-dashboard
```

<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

Edit `.env` using `env.sample` or simply export the variables in the `environment`. Here are the expected values: 

- `DEBUG`: controls the `Development`, `Production` mode
  - Default `False` (production)
- `FLASK_APP=run.py`: mandatory (APP entry point) 
- `SECRET_KEY`: optional, random value used if not provided
- `DB credentials`
  - `Note`: if NOT provided, or wrong values, **SQLite is used**
  - `DB_ENGINE`, `DB_HOST`, `DB_NAME` ...
- `CDN_DOMAIN`: disabled by default
  - Used only when `DEBUG=False` (production mode)   
 
<br />

> Start the app

```bash
$ flask run
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

Edit `.env` using `env.sample` or simply export the variables in the `environment`. Here are the expected values: 

- `DEBUG`: controls the `Development`, `Production` mode
  - Default `False` (production)
- `FLASK_APP=run.py`: mandatory (APP entry point) 
- `SECRET_KEY`: optional, random value used if not provided
- `DB credentials`
  - `Note`: if NOT provided, or wrong values, **SQLite is used**
  - `DB_ENGINE`, `DB_HOST`, `DB_NAME` ...
- `CDN_DOMAIN`: disabled by default
  - Used only when `DEBUG=False` (production mode)  

<br />

> Start the app

```bash
$ flask run
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />

## ✨ Code-base structure

The project has a simple, intuitive structure presented bellow:

```bash
< PROJECT ROOT >
   |
   |-- apps/__init__.py
   |-- apps/
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/
   |         |
   |         |-- includes/                 # Page chunks, components
   |         |    |
   |         |    |-- navigation.html      # Top bar
   |         |    |-- scripts.html         # JS scripts common to all pages
   |         |    |-- footer.html          # The common footer
   |         |
   |         |-- layouts/                  # App Layouts (the master pages)
   |         |    |
   |         |    |-- base.html            # Used by common pages like index, UI
   |         |
   |         |-- home/                     # UI Kit Pages
   |              |-- index.html           # default page
   |              |-- page-404.html        # 404 error page
   |              |-- *.html               # Used by common pages like index, UI
   |
   |-- requirements.txt
   |
   |-- run.py
   |
   |-- ************************************************************************
```

<br />

## Screenshots

![Berry Bootstrap 5 - Sign IN, Open-source Starter by AppSeed.](https://user-images.githubusercontent.com/51070104/207091198-2753246e-3d65-4aac-96de-0598a9a94788.jpg)

<br />

> [Flask Berry Bootstrap 5](https://github.com/app-generator/flask-berry-dashboard) - `Icons` Page

![Berry Bootstrap 5 - UI Icons page, Open-source Starter by AppSeed](https://user-images.githubusercontent.com/51070104/207091655-d5005e08-7ea0-4367-ab3a-2cd16934d2fd.jpg)

<br />

> [Flask Berry Bootstrap 5](https://github.com/app-generator/flask-berry-dashboard) - `Colors` page

![Berry Bootstrap 5 - Colors page, Open-source Starter by AppSeed](https://user-images.githubusercontent.com/51070104/207091441-942be542-2794-4bdb-a51d-85c75b5bc692.jpg)

<br />

---
[Flask Berry Bootstrap 5](https://appseed.us/product/berry-dashboard/flask/) - Minimal **Flask** starter provided by **[AppSeed](https://appseed.us/)**
