#
# class CreditCard:
#   """A consumer credit card."""
#
#   def __init__(self, customer, bank, acnt, limit):
#     """Create a new credit card instance.
#
#     The initial balance is zero.
#
#     customer  the name of the customer (e.g., 'John Bowman')
#     bank      the name of the bank (e.g., 'California Savings')
#     acnt      the acount identifier (e.g., '5391 0375 9387 5309')
#     limit     credit limit (measured in dollars)
#     """
#     self._customer = customer
#     self._bank = bank
#     self._account = acnt
#     self._limit = limit
#     self._balance = 0
#
#   def get_customer(self):
#     """Return name of the customer."""
#     return self._customer
#
#   def get_bank(self):
#     """Return the bank's name."""
#     return self._bank
#
#   def get_account(self):
#     """Return the card identifying number (typically stored as a string)."""
#     return self._account
#
#   def get_limit(self):
#     """Return current credit limit."""
#     return self._limit
#
#   def get_balance(self):
#     """Return current balance."""
#     return self._balance
#
#   def charge(self, price):
#     """Charge given price to the card, assuming sufficient credit limit.
#
#     Return True if charge was processed; False if charge was denied.
#     """
#     if price + self._balance > self._limit:  # if charge would exceed limit,
#       return False                           # cannot accept charge
#     else:
#       self._balance += price
#       return True
#
#   def make_payment(self, amount):
#     """Process customer payment that reduces balance."""
#     self._balance -= amount
#
# if __name__ == '__main__':
#   wallet = []
#   wallet.append(CreditCard('jorius', 'California Savings',
#                            '5391 0375 9387 5309', 2500) )
#   wallet.append(CreditCard('John Bowman', 'California Federal',
#                            '3485 0399 3395 1954', 3500) )
#   wallet.append(CreditCard('pumpkin', 'California Finance',
#                            '5391 0375 9387 5309', 5000) )
#
#   for val in range(1, 20):
#     wallet[0].charge(val)
#     wallet[1].charge(2*val)
#     wallet[2].charge(3*val)
#
#   for c in range(0,3):
#     print('Customer =', wallet[c].get_customer())
#     print('Bank =', wallet[c].get_bank())
#     print('Account =', wallet[c].get_account())
#     print('Limit =', wallet[c].get_limit())
#     print('Balance =', wallet[c].get_balance())
#     while wallet[c].get_balance() > 100:
#       wallet[c].make_payment(100)
#       print('New balance =', wallet[c].get_balance())
#     print()


# def lcs(a, b):
#     lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
#     # row 0 and column 0 are initialized to 0 already
#     print(lengths)
#     for i, x in enumerate(a):
#         for j, y in enumerate(b):
#             if x == y:
#                 print(x,y)
#                 lengths[i+1][j+1] = lengths[i][j] + 1
#             else:
#                 lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
#     # read the substring out from the matrix
#     result = ""
#     x, y = len(a), len(b)
#     print(lengths)
#     while x != 0 and y != 0:
#         if lengths[x][y] == lengths[x-1][y]:
#             x -= 1
#         elif lengths[x][y] == lengths[x][y-1]:
#             y -= 1
#         else:
#             assert a[x-1] == b[y-1]
#             result = a[x-1] + result
#             x -= 1
#             y -= 1
#     return result

def lcs(A, L):
    sequence = []
    for i in range(len(A)):
        for k in range(len(L)):
            if A[i]==L[k]:
                sequence.append(L[k])
                break
    return sequence

print(lcs('squirrel', 'square'))

# thisisatest
# testing123testing