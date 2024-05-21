from database impot db

class Dulce(db.Model):
    __tablename__="dulces"

    id= db.Column(db.Integer, primary_key=True)
    titulo =db.Column(db.String(100), nullable=False)
    autor= db.Column(db.String(100), nullable=False )
    edicion=db.Column(db.String(100), nullable=False)
    disponibilidad=db.Column(db.boolean, nullable=False)
