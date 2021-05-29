from utils.db_api.sqlite import Database

db = Database()


def test():
    # conditions = db.select_all()
    # print({conditions})
    condition = db.select_blocking_condition(switchgear_id="1", element_id="2", component_id="3")
    print({condition})


test()
