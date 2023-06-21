import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
from flask import abort, render_template, Flask
import logging
import db

APP = Flask(__name__)

# Start page
@APP.route('/')
def index():
    cat = db.execute ('''Select Count(Nome) Num from Categoria''').fetchone()
    menu = db.execute ('''Select Count(Nome) Num from Menu''').fetchone()
    ingre = db.execute ('''Select Count(Nome) Num from Ingredientes''').fetchone()
    stats = db.execute('''Select Categoria.CategoriaId Id,Categoria.Nome, count(ComidaId) Num
                          from Categoria
                          left join Comida using (CategoriaId)
                          group by Categoria.Nome''').fetchall()
    return render_template('index.html',stats=stats,cat=cat,menu=menu,ingre=ingre)

# Menu
@APP.route('/menu/')
def menu():
    menu = db.execute(
      '''
      SELECT MenuId as Id, Menu.Nome, Count(ComidaId) as Cont, NBebidas as NBeb
      FROM Menu
      natural join Menu_Comida
      where ComidaId not in(
        select ComidaId
        where ComidaId > 63 AND ComidaId < 68
        )
      Group by Id,Nome
      ORDER BY Id
      ''').fetchall()
    return render_template('menu-list.html', menu=menu)


@APP.route('/menu/<int:id>/')
def get_menu(id):
  menu = db.execute(
      '''
      SELECT Nome
      FROM Menu 
      WHERE MenuId = %s
      ''', id).fetchone()

  if menu is None:
     abort(404, 'Comida id {} does not exist.'.format(id))
  comida = []
  cat = db.execute('''Select CategoriaId from Categoria''').fetchall()
  for x in cat:
    comidasub = db.execute(
      '''
      SELECT Categoria.Nome cat, Comida.ComidaId id, Comida.Nome 
      FROM Menu_Comida NATURAL JOIN Comida
      left join Categoria using (CategoriaId) 
      WHERE MenuId = %s 
      And CategoriaId = %s
      ORDER BY CategoriaId desc,ComidaId
      ''' %(id,x["CategoriaId"])).fetchall()
    print(comidasub)
    comida.append(comidasub)
    print(comida)
 

  return render_template('menu.html',comida=comida,menu=menu)

# Actors
@APP.route('/comida/')
def list_prod():
    comida = db.execute('''
      SELECT Comida.ComidaId as Id, Comida.Nome as Nome, Categoria.Nome as cat
      FROM Comida
      left join Categoria using (CategoriaId)
      Where Categoria.Nome != "Bebida"
      ORDER BY Comida.Nome
    ''').fetchall()
    return render_template('comida-list.html', comida=comida)


@APP.route('/comida/<int:id>/')
def comida_especifica(id):
  comida = db.execute(
    '''
    SELECT ComidaId Id, Comida.Nome Nome, EnerJ EJ, Lip, Sat, Hidr, Acucar, Prot, Sal
    FROM  Comida
    WHERE ComidaId = %s
    ''', id).fetchone()

  if comida is None:
     abort(404, 'Comida id {} does not exist.'.format(id))

  
  ingre = db.execute(
    '''
    SELECT Nome ing
    FROM Ingredientes NATURAL JOIN Contem
    WHERE ComidaId = %s
    ORDER BY Nome
    ''', id).fetchall()

  print(ingre)
  return render_template('prod.html', 
           comida=comida, ingre=ingre)

@APP.route('/cat/<int:id>/')
def categorias(id):
    nome = db.execute('''SELECT Nome from Categoria where CategoriaId = %s''',id).fetchone()
    cat = db.execute('''SELECT ComidaId Id, Comida.Nome Name 
                      from Categoria
                      left join Comida using (CategoriaId)
                      where Categoria.CategoriaId = "%s"''',id).fetchall()
    return render_template('cat.html',cat=cat,nome=nome)
            