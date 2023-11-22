import pygame
from constantes import*
from funciones import*


class Pregunta:
    def __init__(self, pantalla, fuente:str, texto:str, color:str, dimensiones:int, y:int,x:int) -> None:
        self.pantalla = pantalla
        self.fuente = fuente
        self.texto = texto
        self.color = color
        self.dimensiones = dimensiones
        self.y = y
        self.x = x

        
    def mostrar_pregunta(self):
        tipo_letra = pygame.font.SysFont(self.fuente,self.dimensiones)
        superficie = tipo_letra.render(self.texto,True,self.color)
        self.pantalla.blit(superficie,(self.y,self.x))
        
    def optener_respuesta_correcta(lista_recibida:list,posicion:int,elegido:str):
            if elegido == lista_recibida[posicion]["correcta"]:
                respuesta = True
            else:
                respuesta = False
            return respuesta
    
    def mostrar_rectangulo(pantalla,color):
        pygame.draw.rect(pantalla,color,(100,435,180,50))
        pygame.draw.rect(pantalla,color,(300,435,180,50))
        pygame.draw.rect(pantalla,color,(500,435,180,50))
    
    def pintar_rectangulo(pantalla,color,opcion):
        pygame.draw.rect(pantalla,color,opcion)

           
           
           

                        