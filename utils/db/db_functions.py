from db_config import session
from db_mapping import User
from logger import logger


def commit():
    session.commit()
    session.close()


def close_session(func):
    def wrapper(*args, **kwargs):
        try:
            if not session.is_active:
                session.begin()
            response = func(*args, **kwargs)
            close = kwargs.get('need_close')
            if close is None or close is True:
                session.close()
            return response
        except Exception as err:
            logger.error(f"SQL error: {err}")
            session.rollback()
            session.close()

    return wrapper


@close_session
def get_all_users():
    resp = session.query(User).all()
    session.close()
    return resp
