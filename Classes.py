class Plataforma:
    def info(self, largura, altura, posx, posy):
        self.l = largura
        self.h = altura
        self.x = posx
        self.y = posy
class Entidade:
    def info(self, largura, altura, posx, posy, velocidade, gravidade, estado, pulo):
        self.l = largura
        self.h = altura
        self.x = posx
        self.y = posy
        self.veloc = velocidade
        self.grav = gravidade
        self.status = estado
        self.pulo = pulo
