import wsinter
from time import sleep
from random import randint

y = 100
x = 100

last_img_id = 0

# deplacer l'image au clavier
def hbgd(s,d):
    global x,y
    if s=="D":
        if d[5]=='KeyW':
            y-=2
        elif d[5]=='KeyS':
            y+=2
        elif d[5]=='KeyA':
            x-=2
        elif d[5]=='KeyD':
            x+=2

    ws.attributs('img01',style={"left":str(x)+"px","top":str(y)+"px"})

# faire sauter l'image quand on clic dessus
def jump(s,d):
    global x,y
    if s=="D":
        if d[0]=='img01':
            x=randint(0,800)
            y=randint(0,800)
            ws.attributs('img01',style={"left":str(x)+"px","top":str(y)+"px"})

def animer():
    global x
    while x < 800:
        sleep(0.05)
        x+=1
        ws.attributs('img01',style={"left":str(x)+"px"})
       
def add_image(path: str, position: tuple, size: tuple=None):
    """
    Ajoute l'image pointee par path sur la page
    
    Parametres:
    
        - path : Chemin vers l'image relatif au dossier /src/content
        - position : Position pour l'image sur la page sous la forme d'un tuple (x, y)
        - size : Taille de l'image, 0 pour la taille native de l'image, sous la forme d'un tuple (w, h)
    
    Renvoie l'id de l'image
    """
    global last_img_id
    
    style = {"position": "absolute", "left": str(position[0]) + "px", "top": str(position[1]) + "px"}
    if size != None:
        style["width"] = str(size[0]) + "px"
        style["height"] = str(size[1]) + "px"
    img_id = "img" + str(last_img_id)
    ws.insere(img_id, "img", attr={'src':f'../{path}'}, style=style)
    last_img_id += 1
    return img_id    
    
def change_dimensions(id: str, position: tuple=None, size: tuple=None):
    if position == None and size == None:
        raise ValueError("BRUH, faut mettre des valeurs quand meme")
    style = {"position": "absolute"}
    if position != None:
        style["left"] = str(position[0]) + "px"
        style["top"] = str(position[1]) + "px"
    if size != None:
        style["width"] = str(size[0]) + "px"
        style["height"] = str(size[1]) + "px"        
    ws.attributs(id, style=style)


def start():
    global ws
    ws = wsinter.Inter()
    ws.demarre(page="content/pages/index.html", clavier=True)
    
    return ws
    
