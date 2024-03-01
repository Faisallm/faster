from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


# the name of the function doesn't matter
# base url
# we shouldn't try to retrieve all blogs

# accepting query paramters into my function
# all query parameters are accepted as 'str'
# it is upto us to coerce them
# giving default values to our query parameters

# when we don't want to provide a default value for sort...
# we set a value of Optional equaling None.

@app.get('/blog')
def homepage(limit: int = 10, skip: int=0, published: bool=True, sort: Optional[str]=None):
    # only get 10 published blogs
    if published:
        return {"data": f"{limit} blogs from the database."}
    else:
        return {"data": "All the blogs"}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "All unpublished blogs"}

# we have path parameters and query parameters.

# we are coercing the id to int
@app.get("/blog/{id}/comments")
def comments(id: int, limit=10):
    # fetch comments of blog with id
    print(type(id))
    return {"data": {"1", "2"}}

# the pydantic model will 
# carry out the validation for us.

class Blog(BaseModel):
    title: str
    body: str
    # optional field with no default value.
    # we don't want to always provide for this field.
    published: Optional[bool] = None

@app.post('/blog')
def create_blog(blog: Blog):
    return {"data": f"Blog is created with title as '{blog.title}'"}