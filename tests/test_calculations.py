# import pytest
# from app.calculations import add, mutiply, substract, dicide, BankAccount

# @pytest.fixture
# def zero_bank_account():
#     return BankAccount()

# @pytest.fixture
# def bank_account():
#     return BankAccount(50)

# @pytest.mark.parametrize("n1, n2, expected", [
#     (3, 2, 5),
#     (5, 5, 10)
# ])
# def test_add(n1, n2, expected):
#     print("test add function")
#     assert add(n1,n2) == expected

# def test_substract():
#     assert substract(3,1) == 2

# def test_multiply():
#     assert mutiply(3,1) == 3

# def test_divide():
#     assert dicide(4,2) == 2

# # def test_bankaccount_balance(): 
# #     account = BankAccount(30)
# #     assert account.balance == 30
# # we use fixture and we get :

# def test_bank_set_initial_amount(bank_account):
#     assert bank_account.balance == 50


# def test_bank_default_amount(zero_bank_account):
#     print("testing my bank account")
#     assert zero_bank_account.balance == 0


# def test_withdraw(bank_account):

#     bank_account.withdraw(20)
#     assert bank_account.balance == 30


# def test_deposit(bank_account):

#     bank_account.deposit(30)
#     assert bank_account.balance == 80


# def test_collect_interest(bank_account):

#     bank_account.collect_interest()
#     assert round(bank_account.balance, 6) == 55


# @pytest.mark.parametrize("deposited, withdrew, expected", [
#     (200, 100, 100),
#     (50, 10, 40),
#     (1200, 200, 1000)

# ])
# def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
#     zero_bank_account.deposit(deposited)
#     zero_bank_account.withdraw(withdrew)
#     assert zero_bank_account.balance == expected


# def test_insufficient_funds(bank_account):
#     with pytest.raises(InsufficientFunds):
#         bank_account.withdraw(200)