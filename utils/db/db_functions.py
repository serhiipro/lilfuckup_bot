from utils.db.db_mapping import MemesBase
from utils.db.db_config import session
from logger import logger


def commit():
    session.commit()
    session.close()


def add_image_info(img):
    img_info = MemesBase(file_id=img.file_id, file_unique_id=img.file_unique_id, associated_text='')
    session.add(img_info)
    commit()


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


# @close_session
# def get_all_users():
#     resp = session.query(MemesBase).all()
#     session.close()
#     return resp





#
# if __name__ == '__main__':
#     c1 = MemesBase(file_id='Ravi Kumar', file_unique_id='Station Road Nanded', associated_text='ravi@gmail.com')
#
#     session.add(c1)
#     session.commit()