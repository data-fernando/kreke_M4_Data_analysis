class Libro:

    libros=[]

    def __init__(self,titulo:str,autor:str,paginas:int):
        self.titulo=titulo
        self.autor=autor
        self.paginas=paginas
        ## la clase
        Libro.libros.append(self)

        

    def mostrar_info(self):
        muestra={
            "Titulo":self.titulo,
            "Autor":self.autor,
            "Paginas":self.paginas
        }   
        return muestra

    @staticmethod
    def es_grande(paginas:int):
        esgrande=False
        if (paginas>300):
            esgrande=True
        
        return esgrande
    
    @classmethod
    def total_libros(cls):
        return len(cls.libros)


