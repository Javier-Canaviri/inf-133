def render_libro_list(libros):
    
    #representa una lista de libros como una lista de diccionarios
    return [
        {
            "id":libro.id,
            "titulo":libro.titulo,
            "autor":libro.autor,
            "edicion":libro.edicion,
            "disponibilidad":libro.disponibilidad,
        }
        for libro in libros
    ]
    
def render_libro_detail(libro):
    #represeta los detalles de un Libro como un diccionario
    return{
        "id":libro.id,
        "titulo":libro.titulo,
        "autor":libro.autor,
        "edicion":libro.edicion,
        "disponibilidad":libro.disponibilidad,
    
    }