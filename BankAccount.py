    package Data;
    class BankAccount:
        private long cardNumber;
        private double balance;
    
        def BankAccount(long cardNumber, double balance):
            self.cardNumber = cardNumber;
            self.balance = balance;
        }
    
        def getCardNumber():
            return self.cardNumber;
        }
    
        def setCardNumber(long cardNumber):
            self.cardNumber = cardNumber;
        }
    
        def getBalance():
            return self.balance;
        }
    
        def setBalance(double balance):
            self.balance = balance;
        }
    }
    
