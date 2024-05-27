from fastapi import APIRouter

entre_root = APIRouter()

#endpoint
@entre_root.get("/")
def apiRunning():
    res = {
        "status":"ok",
        "message":"Apí is running"
    }
    return res