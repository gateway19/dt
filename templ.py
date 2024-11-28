from fastapi import FastAPI, Form, Request, HTTPException, Query, Body
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from datetime import datetime
import uuid



app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Model:
    def __init__(self, id, name): # id state time(started/ended)
        self.id = id
        self.name = name

class Repository:
    def __init__(self):
        self.entities = []

    def get_all(self):#nothink 
        return None
    def get_by_id(self):# id 
        return None
    def add(self): # object 
        pass
    def delete(self): # id 
        pass
    def update(self):#model object
        pass
pass
repo = Repository()
repo.add("")


class Orders:
    def __init__(self,id):
        self.id =id
        
repo = [Orders(10),Orders(10)]


@app.get("/", response_class=HTMLResponse)
def base(request: Request):
    return  templates.TemplateResponse("index.html", {"request": request,"inside_data": ["DATA FROM PYTHON","ddd",1732174413], "test":repo})

@app.post("/")
async def getdata(data = Body()):
    data["end_date_fr_un"]= datetime.fromtimestamp(data["end_date"]).strftime('%Y-%m-%d %H:%M:%S')
    data["from_dt_unix"] =datetime.fromtimestamp(data["end_date"]).timestamp() # datetime.now().timestamp()
    return data





import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)




<html>
{% for i in inside_data %}
<br>
{{ i }}
<br>

{% endfor %}

{% for el in test %}
<p>{{ el.id }}</p>

{% endfor %}
<script>
var date = new Date( {{ inside_data[2] }}  * 1000);
alert(date)
</script>
</html>





pip install Jinja2
pip install fastapi
pip install uvicorn
