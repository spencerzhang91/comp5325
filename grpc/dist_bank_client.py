# dist_bank_client.py
"""
The Python implementation of the gRPC dist bank client.
"""
import random
import time
import grpc
import dist_bank_pb2
import dist_bank_pb2_grpc
import dist_bank_resources

from dist_bank_exceptions import *


def bank_lookup_account(stub, request):
    """
    Client side method to request a lookup operation.

       stub: stub
    request: <class 'dist_bank_pb2.LookupRequest'
     return:
    """
    print("In method bank_lookup_account:")
    result = stub.LookUpAccount(request) # <-- remember to check whether port is occupied!
    # from line 26 to 28 seem never gonna be reached!
    if result is None:
        print("Unable to find record")
        raise AccountNotExistError
    print(result.uid, result.index, result.balance)
    return result


def bank_withdraw_money(stub, request):
    """
    Client side method to request a withdraw operation.

       stub: stub
    request: <class 'dist_bank_pb2.WithdrawRequest'
     return:
    """
    print("In method bank_withdraw_money:")
    result = stub.Withdraw(request)
    print(result)
    return result


def bank_save_money(stub, request):
    """
    Client side method to request a save operation.

       stub: stub
    request: <class 'dist_bank_pb2.SaveRequest'
     return:
    """
    print("In method bank_withdraw_money:")
    result = stub.Save(request)
    print(result)
    return result




def run():
    """
    Simple client runability tests.
    """
    channel = grpc.insecure_channel('localhost:50051')
    stub = dist_bank_pb2_grpc.DistBankStub(channel)


    print("-------------- LookupAccount --------------")
    bank_lookup_account(stub, dist_bank_pb2.LookUpRequest(uid="5a221afc35b38f9a0ba44b2c"))


    print("-------------- withdraw --------------")
    bank_withdraw_money(stub, dist_bank_pb2.WithdrawRequest(uid="5a221afc35b38f9a0ba44b2c", with_amount=100.0))


    print("-------------- save --------------")
    bank_save_money(stub, dist_bank_pb2.SaveRequest(uid="5a221afc35b38f9a0ba44b2c", save_amount=100.0))


if __name__ == '__main__':
    run()


"""
The target test data:
{

    "balance": "62415.24",
    "index": 66,
    "uid": "5a221afc35b38f9a0ba44b2c"
  }
"""