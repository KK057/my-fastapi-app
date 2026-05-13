from fastapi import FastAPI,Request,HTTPException,status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from schemas import PostResponse,PostCreate

app=FastAPI()

app.mount("/static", StaticFiles(directory="static"),name="static") #For image and files extraction
templates = Jinja2Templates(directory="templates")

posts= [
    {"id": 1, "name": "Alice", "role": "Admin","date":"12-9-26","content":"Hello, how are you?"},
    {"id": 2, "name": "Bob", "role": "Editor","date":"12-9-26","content":"Hello, how are you?",},
    {"id": 3, "name": "Charlie", "role": "Viewer","date":"12-9-26","content":"Hello, how are you?"}
]

@app.get("/",include_in_schema=False) #for hiding the routes in docs
def Home(request:Request):
    return templates.TemplateResponse(request, "home.html",{"posts":posts})

@app.get("/api/posts/",response_model=list[PostResponse])
def get_posts():
    return posts

@app.post("/api/posts/hello/",response_model=PostResponse,status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate):
    new_id=max(p["id"] for p in posts)+1 if posts else 1
    new_post={
        "id":"new_id",
        "title":posts.role,
        "author":posts.name,
        "content":posts.content,
        "post_date":posts.date
    }

@app.get("/api/posts/{posts_id}",include_in_schema=False)
def post_click(request: Request,posts_id: int):
    for post in posts:
        if post.get("id") == posts_id:
            return templates.TemplateResponse(request,"posts.html",{"posts":posts})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")


@app.get("/api/posts/{posts_id}",response_model=PostResponse)
def post_match(request: Request,posts_id: int):
    for post in posts:
        if post.get("id") == posts_id:
            return templates.TemplateResponse(request,)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")

