from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
#Database conexionn local
DATABASE_URI = 'postgres+psycopg2://david:admin@localhost:5432/nqueens'
db = create_engine(DATABASE_URI)  
base = declarative_base()
"""

# Database conexionn docker
DATABASE_URI = "postgres+psycopg2://postgres:p4ssw0rd@172.17.0.2:5432/nqueens"
DATABASE_URI = "postgres+psycopg2://postgres:p4ssw0rd@0.0.0.0:5431/nqueens"
db = create_engine(DATABASE_URI)
base = declarative_base()


class SolutionsNumber(base):
    __tablename__ = "solutions_number"
    id = Column(Integer, primary_key=True)
    n_value = Column(Integer)
    solutions_number = Column(Integer)


# Table that stores all the solutions
class Solutions(base):
    __tablename__ = "solutions"
    id = Column(Integer, primary_key=True)
    n_value = Column(Integer)
    column_values = Column(String)


# Create
def setSolutionNumber(value, number):
    Session = sessionmaker(db)
    session = Session()
    prueba1 = SolutionsNumber(n_value=value, solutions_number=number)
    session.add(prueba1)
    session.commit()
    # print("Well created")
    session.close()
    # recreate_database()
    return True


def getSolutionNumber(value):
    # Read
    # Filter by n and return the solutionNumber
    Session = sessionmaker(db)
    session = Session()
    solutions = session.query(SolutionsNumber).filter_by(n_value=value).first()
    return solutions


def setSolution(value, sol_in):
    # print(value, sol_in)
    Session = sessionmaker(db)
    session = Session()
    prueba1 = Solutions(n_value=value, column_values=sol_in)
    session.add(prueba1)
    session.commit()
    # print("Well added")
    session.close()
    # recreate_database()
    return True


def getAllSolutions(value):
    Session = sessionmaker(db)
    session = Session()
    solutions = session.query(Solutions).filter_by(n_value=value)
    session.close()
    return solutions


if __name__ == "__main__":

    """
	try:
		res = setSolutionNumber(28, 5)
	except:
		print(("This N value ({0}) was previously calculated").format(28))
	try:
		res = getSolutionNumber(28)
		print("Respuesta: ", res.solutions_number)
	except:
		print(("The value: {0} has not been calculated, please run NQueens({0}) to get and store the solution.").format(28))
	try:
		res = setSolution(29, "[11,0,5,6,7,8,15,19,21,0,20,15,14,13,12,15,10,8]")
	except:
		print(("This N value ({0}) was previously calculated").format(28))
	res = getAllSolutions(29)
	print("solutions", res)
	for sol in res: 
		print(sol.column_values)
	# except:
	# print(("The value: {0} has not been calculated, please run NQueens({0}) to get and store the solution.").format(29))
	print("Continuar", (1+1))
	"""
