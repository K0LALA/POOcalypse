from web.main_web import add_image, change_dimensions

IMG_PATH = "assets/spritesheets/square/square_001.png"
MOVE_AMOUNT = 2

# Contient le joueur
class Player:
    def __init__(self, position: tuple):
        self.x = position[0]
        self.y = position[1]
        self.id = add_image("assets/spritesheets/square/square_001.png", (self.x, self.y))
        
        
    def move(self, movement: tuple):
        """
        Mouvement sur la position du joueur
        
        Parametres:
        
            - movement : tuple de la forme (x, y) indiquant la quantite de mouvement dans chacune des directions
        """
        self.x += movement[0]
        self.y += movement[1]
        self.render()
        
    def move_input(self, key):
        """
        Recupere l'evenement d'appui de touche pour bouger le joueur
        """
        match key:
            case "KeyW":
                self.move((0, -MOVE_AMOUNT))
            case "KeyA":
                self.move((-MOVE_AMOUNT, 0))
            case "KeyS":
                self.move((0, MOVE_AMOUNT))
            case "KeyD":
                self.move((MOVE_AMOUNT, 0))
        
    def render(self):
        change_dimensions(self.id, (self.x, self.y))