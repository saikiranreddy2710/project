from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/book-call", response_class=HTMLResponse)
async def book_call(request: Request, name: str = Form(...), email: str = Form(...), phone: str = Form(...), date: str = Form(...), time: str = Form(...)):
    # Do something with the form data
    return templates.TemplateResponse("booking_confirmation.html", {"request": request, "name": name, "email": email, "phone": phone, "date": date, "time": time})
