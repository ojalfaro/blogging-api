from fastapi import FastAPI
from routes.entry import entre_root
from routes.blog import blog_root

app = FastAPI()

app.include_router(entre_root)
app.include_router(blog_root)