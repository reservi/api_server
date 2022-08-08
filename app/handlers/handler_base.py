
class HandlerBase:
    def __init__(self, db, session):
        engine = session.get_bind()
        db.metadata.create_all(engine)