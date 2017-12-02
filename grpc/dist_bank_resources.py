# dist_bank_resources.py
"""
The balance data json utiliztion code.
"""

import json
import dist_bank_pb2
from dist_bank_exceptions import *

_SUCCESS_MODIFIED = 0
_MODIFICATION_ERR = 1
_NOT_ENOUGH_MONEY = 2


def read_dist_bank_database():
    """
    Reads the dist bank database.

    Returns:
        he full contents of the dist bank database as a sequence of
        dist_bank_pb2.BalanceRecord.
    """
    record_list = []
    with open("dist_bank_db.json") as dist_bank_db_file:
        for item in json.load(dist_bank_db_file):
            record = dist_bank_pb2.BalanceRecord(
                uid=item["uid"],
                index=item["index"],
                # Balance field is a string in json, so change to float:
                balance=float(item["balance"]))
            record_list.append(record)
    return record_list


def modify_dist_bank_database_withdraw(request): # NOT DONE YET!
    """
    Modifies dist bank database upon withdraw operation.

    # Remark: Do we need to keep track of the modifications?
    request: <class 'dist_bank_pb2.WithdrawRequest'> or <class 'dist_bank_pb2.SaveRequest'>
    returns: bool
    """
    with open("dist_bank_db.json") as dist_bank_db_file:
        db = json.load(dist_bank_db_file)
        for item in db:
            if item["uid"] == request.uid:
                if float(item["balance"]) >= request.with_amount:
                    print("Before withdraw operation:")
                    print(item)
                    print("After withdraw operation:")
                    item.update({"balance": str(float(item["balance"]) - request.with_amount)})
                    print(item)
                else:
                    return _NOT_ENOUGH_MONEY

            else:
                return _MODIFICATION_ERR

def modify_dist_bank_database_save(request): # NOT DONE YEt!
    """
    Modifies dist bank database upon save operation.

    # Remark: Do we need to keep track of the modifications?
    request: <class 'dist_bank_pb2.WithdrawRequest'> or <class 'dist_bank_pb2.SaveRequest'>
    returns: bool
    """
    try:
        dist_bank_db_file = open("dist_bank_db.json", "r")
        db = json.load(dist_bank_db_file)
        print('bf-->', db[0])
        for i in range(len(db)):
            if db[i]["uid"] == request.uid:
                db[i].update({"balance": str(float(db[i]["balance"]) + request.save_amount)})
                # print(new_db[i])
        print('af-->', db[0])
        dist_bank_db_file.close()
        dist_bank_db_file = open("dist_bank_db.json", "w")
        json.dump(db, dist_bank_db_file)
    finally:
        dist_bank_db_file.close()


if __name__ == "__main__":

    #modify_dist_bank_database_withdraw(dist_bank_pb2.WithdrawRequest(uid="5a221afc4fcb9e8932acaf8b", with_amount=94274.05))
    print('\n\n')
    modify_dist_bank_database_save(dist_bank_pb2.SaveRequest(uid="5a221afc4fcb9e8932acaf8b", save_amount=94274.05))
