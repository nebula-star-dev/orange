from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    #return {"message": "Demo Application for Kubernetes Deployment"}
    return RedirectResponse("/seeyourname/var_name", status_code=307)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/seeyourname/{name}", response_class=HTMLResponse)
async def see_your_name(request: Request, name: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"name": name}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=9995)