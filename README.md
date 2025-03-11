FastAPI URL Shortener
========================

Simple URL shortener built with **FastAPI**, **Python**, and **PostgreSQL**. 

* * * * *

Features
----------
Though pretty straight forward, here we go:

-   **Shorten URLs** with randomly generated slugs.
-   **Persistent storage** using PostgreSQL.
-   **Automatic redirection** via FastAPI endpoints.
-   **Interactive documentation** (Swagger UI) provided by FastAPI.
-   **Automated testing** with Pytest.
-   **Deployed live** on Render.

* * * * *

Quick Start
--------------

### Local Installation

Clone the repository:

```
git clone https://github.com/your-username/fastapi-url-shortener.git
cd fastapi-url-shortener
```

Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate   # For Windows: .\venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Start the server:

```
uvicorn main:app --reload
```

Visit your app locally at http://localhost:8000/docs.

### Running Tests

Execute tests with Pytest:

```
pytest
```

* * * * *

Live Demo
------------

You can check out the deployed version on Render if you'd like :3
https://url-shortener-qus3.onrender.com/docs

(might take a min for it to start up if it's sleeping)
* * * * *

API Usage
------------

### Shorten a URL

**Request:**

```
curl -X POST -H "Content-Type: application/json"\
     -d '{"url":"https://www.google.com"}'\
     https://url-shortener-qus3.onrender.com/shorten
```

**Response:**

```
{
  "short_url": "https://url-shortener-qus3.onrender.com/abc123"
}
```

### Follow the Short URL

Visit the generated short URL in your browser:

```
https://url-shortener-qus3.onrender.com/abc123
```

You'll be redirected to the original URL (e.g., Google).

* * * * *

Tech Stack
--------------
-   **FastAPI**
-   **Python**
-   **SQLAlchemy**
-   **PostgreSQL** (for persistence)
-   **Pytest** (for testing)
-   **Render** (for deployment)
* * * * *

To-Do's
--------------
-   Probably just need to work on a cohesive front-end, will do when I feelz like it :p

* * * * *

Project Links
----------------

-   [GitHub Repository](https://github.com/your-username/fastapi-url-shortener)

-   [Live Demo](https://url-shortener-qus3.onrender.com/docs)

* * * * *

License
----------
Feel free to use or modify this project!
