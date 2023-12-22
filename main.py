from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

thumbnail = "https://cdn.britannica.com/77/170477-050-1C747EE3/Laptop-computer.jpg"
datasets = [
    {
        "name": "Dataset 1",
        "image_count": 100,
        "class_count": 10,
        "progress": 10,
        "thumbnail": thumbnail,
    },
    {
        "name": "Dataset 2",
        "image_count": 100,
        "class_count": 10,
        "progress": 20,
        "thumbnail": thumbnail,
    },
    {
        "name": "Dataset 3",
        "image_count": 100,
        "class_count": 10,
        "progress": 30,
        "thumbnail": thumbnail,
    },
    {
        "name": "Dataset 4",
        "image_count": 100,
        "class_count": 10,
        "progress": 40,
        "thumbnail": thumbnail,
    },
    {
        "name": "Dataset 5",
        "image_count": 100,
        "class_count": 10,
        "progress": 50,
        "thumbnail": thumbnail,
    },
    {
        "name": "Dataset 6",
        "image_count": 100,
        "class_count": 10,
        "progress": 60,
        "thumbnail": thumbnail,
    },
    {
        "name": "Dataset 7",
        "image_count": 100,
        "class_count": 10,
        "progress": 70,
        "thumbnail": thumbnail,
    },
    {
        "name": "Dataset 8",
        "image_count": 100,
        "class_count": 10,
        "progress": 80,
        "thumbnail": thumbnail,
    },
]


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        "main.html", {"request": request, "datasets": datasets}
    )


@app.get("/login", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
