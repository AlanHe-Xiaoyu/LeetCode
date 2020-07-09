# Standardized Interview Questions

For the human-readable version of this project, check out the site: [https://eng-interview-questions.static.corp.creditkarma.com](https://eng-interview-questions.static.corp.creditkarma.com).

[Conversation guidelines & structure of the overall interview](https://dtrejo.com/engineer-interview-script)

## Running the site locally

Install dependencies:

```
pip install mkdocs-material
```

Then:

```
mkdocs serve
```

and visit http://localhost:8000.

------

_Alternatively_, if you're having trouble with Python, you could try Docker.

Run these commands in this directory:

```
docker pull squidfunk/mkdocs-material
```
```
docker run --rm -it -p 8000:8000 -v "${PWD}:/docs" squidfunk/mkdocs-material
```

It will compile, watch, and serve the docs at `http://localhost:8000`