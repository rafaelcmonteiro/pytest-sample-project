from src.wallet import Wallet

if __name__ == "__main__": 
    wallet = Wallet(10)
    rest = wallet.mult_cash(10)
    print(rest)