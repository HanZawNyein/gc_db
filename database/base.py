from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import declarative_base, DeclarativeMeta

ENV = {}

engine = create_engine("sqlite://", echo=True)

# Declarative base class
Base = declarative_base()


class CustomMeta(DeclarativeMeta):
    def __new__(cls, name, bases, dct):
        # Check if _name and _inherit are in the class dictionary
        model_name = dct.get('_name', None)
        inherit_class_name = dct.get('_inherit', None)

        # If _inherit is specified and exists in ENV, adjust the bases
        if inherit_class_name and inherit_class_name in ENV:
            inherit_class = ENV[inherit_class_name]
            bases = (inherit_class,)
            if not model_name:
                dct['__table_args__'] = {'extend_existing': True}
                # dct['inherit_condition']= (cls.id == Base.__table__.c.id)

            # print(bases)

        # Create the new class
        instance = super().__new__(cls, name, bases, dct)

        # Register the new class in ENV
        if model_name:
            instance.__tablename__ = model_name
            ENV[model_name] = instance

        # If _inherit is specified but no _name, register under inherited name
        if inherit_class_name and not model_name:
            instance.__tablename__ = inherit_class_name
            ENV[inherit_class_name] = instance

        return instance


class Model(Base,metaclass=CustomMeta):
    __abstract__ = True
    id = Column(String(50), primary_key=True)

    def search(self):
        return "search method from Model."


class IcaUsers(Model):
    # __tablename__ = 'ica_users'
    _name = 'ica_users'

    name = Column(String(30))
    username = Column(String(30))


class IcaUsers2(IcaUsers):
    # __tablename__ = 'ica_users2'
    # _name = 'ica_users2'
    _inherit = 'ica_users'

    email = Column(String(30))


if __name__ == '__main__':
    tables = []
    for key, value in ENV.items():
        tables.append(value.__table__)
        print(f"{key}: {value.__tablename__}")

    # Create tables for all registered models
    Base.metadata.create_all(bind=engine)
    #, tables=[], checkfirst=False)

    users = ENV['ica_users']
    print(users)
    print(users().search())
    # Base.metadata.create_all(bind=engine)

