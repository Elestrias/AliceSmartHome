from models import *
from app import DEVICE_NOT_FOUND


def is_user_exists(user_id):
    return User.query.filter_by(user_id=user_id).first() is not None


def create_user(user_id):
    user = User(user_id=user_id)
    db.session.add(user)
    db.session.commit()


def is_device_exists(name, user_id):
    device = Device.query.filter_by(user_name=name, user_id=user_id).first()
    if device is None:
        return DEVICE_NOT_FOUND
    return device
