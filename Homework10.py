




# Assignment 1____________________________________________________________
from sqlalchemy import create_engine, MetaData, Table, Integer, Column, String, Float
from sqlalchemy import delete, update, select, insert

meta = MetaData()

engine = create_engine('sqlite:///goods.sqlite', echo=True)
conn = engine.connect()

products = Table('products', meta,
                 Column('id', Integer, primary_key=True),
                 Column('title', String),
                 Column('price', Float),
                 Column('amount', Integer),
                 Column('comment', String)
                 )

meta.create_all(engine)


def Insert():
    ins = products.insert().values(
        title=input("Write product title: "),
        price=float(input("insert price: ")),
        amount=int(input("insert amount: ")),
        comment=input("Write a comment: "),
    )
    result = conn.execute(ins)


def View():
    conn = engine.connect()
    selectt = select([products])
    result = conn.execute(selectt)
    print(result.fetchall())


def Delete():
    id = int(input("Enter id to delete: "))
    delet = delete(products).where(
        products.c.id.like(id)
    )
    result = conn.execute(delet)


def Update():
    id = int(input("Enter product id to update: "))
    # title = input("Write product title"),
    # new_price = input("insert price"),
    # amount = int(input("insert amount")),
    # comment = input("Write a comment"),
    change = products.update().where(products.c.id.like(id)).values(title=input("Write product title: "),
                                                                    price=float(input("Insert price: ")),
                                                                    amount=int(input("Insert amount: ")),
                                                                    comment=input("Write a comment: "))
    result = conn.execute(change)


while True:
    print(
        " enter 1 for Insert\n",
        "enter 2 for Delete\n",
        "enter 3 for View\n",
        "enter 4 for Update\n",
        "enter 0 for Quit\n",
    )

    choice = int(input("Enter the choice: "))
    if choice == 0:
        break
    else:
        {1: Insert, 2: Delete, 3: View, 4: Update}.get(choice)()


#  Assignment 2_________________________________________________________________
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///vehicles.db', echo=True)
Base = declarative_base()


class Brand(Base):
    __tablename__ = "BRAND"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Car(Base):
    __tablename__ = "CAR"
    id = Column(Integer, primary_key=True)
    model = Column(String)
    release_year = Column(Integer)
    brand = Column(String, ForeignKey('BRAND.name'))
    brand_name = relationship("Brand", back_populates="CAR")


Brand.CAR = relationship("Car", order_by=Car.id, back_populates="brand_name")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def Insert_Brand():
    ins = Brand(name=input("Write a brand name: "))
    session.add(ins)
    session.commit()


def Insert_Car():
    ins = Car(model=input("Write a model: "),
              release_year=int(input("Write a release year: ")),
              brand=input("Write a brand: "))
    session.add(ins)
    session.commit()


def View():
    result1 = session.query(Brand).all()
    for row in result1:
        print("id:", row.id, "Brand:", row.name)
    result2 = session.query(Car).all()
    for row2 in result2:
        print("id:", row2.id, "Model:", row2.model, "Issue year:", row2.release_year, "Brand:", row2.brand)


def Delete_Brand():
    x = session.query(Brand).get(int(input("Enter id to delete: ")))
    session.delete(x)
    session.commit()


def Delete_Car():
    x = session.query(Car).get(int(input("Enter id to delete: ")))
    session.delete(x)
    session.commit()


def Update_Brand():
    x = session.query(Brand).get(int(input("Enter id to update: ")))
    x.name = input("Enter a brand")
    session.commit()


def Update_Car():
    x = session.query(Car).get(int(input("Enter id to update: ")))
    x.model = input("Enter a model")
    x.release_year = int(input("Write a release year: "))
    x.brand = input("Write a brand: ")
    session.commit()


while True:
    print(
        " enter 1 for Insert a car brand\n",
        "enter 2 for Insert a car data\n",
        "enter 3 for Delete a brand\n",
        "enter 4 for Delete a data\n",
        "enter 5 for View\n",
        "enter 6 for Update a brand\n",
        "enter 7 for Update a car data\n",
        "enter 0 for Quit\n",
    )

    choice = int(input("Enter the choice: "))
    if choice == 0:
        break
    else:
        {1: Insert_Brand, 2: Insert_Car, 3: Delete_Brand, 4: Delete_Car, 5: View, 6: Update_Brand, 7: Update_Car}.get(
            choice)()
