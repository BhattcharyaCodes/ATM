import mongoengine


def global_init():
    mongoengine.connect(alias='core', name='atm')
