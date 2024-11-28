from fastapi import FastAPI, Form, Request, HTTPException, Query, Body
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from datetime import datetime
import uuid
print(uuid.uuid4())


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



@app.post("/postdata")
def postdata(username: str = Form(default ="Undefined", min_length=2, max_length=20), 
            age: int =Form(default=18, ge=18, lt=111)):
    return {"name": username, "age": age}
# https://metanit.com/python/fastapi/1.15.php



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

with open("file.txt", "r+") as f:
    text = f.read()
    print(text)
    f.write("stuff to append")




# https://metanit.com/python/fastapi/

#https://www.w3schools.com/html/html_tables.asp


#AUTH
<!DOCTYPE html>
<html>
<head>
    <title>Авторизация</title>
</head>
<body>
    <input type="text" name="login" id="login" placeholder="Логин" required>
    <input type="password" name="password" id="password" placeholder="Пароль" required>
    <button onclick="Auth()">Войти</button>
</body> 
<script>
    const trueLogin = "123";
    const truePassword = "123";

    function Auth()
    {
        let login = document.getElementById("login").value;
        let password = document.getElementById("password").value;

        if(login != trueLogin || password != truePassword)
        {
            alert("Неправильный логин или пароль");
            return;
        }

        sessionStorage.setItem("token", "key");
        window.location.href = "/orders.html";
    }
</script>
</html>

#// <script>
    if(!sessionStorage.getItem("token"))
        window.location.href = "auth.html";
</script>



