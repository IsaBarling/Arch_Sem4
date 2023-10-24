    package Providers;
    import Data.BankAccount;
    import Repositories.CashRepository;
    
    class CashProvider:
        CashRepository cashRepository;
    
        def CashProvider():
            self.cashRepository = new CashRepository();
        }
    
        def createAccount(long cardNumber, double balance):
            BankAccount account = new BankAccount(cardNumber, balance);
            self.cashRepository.setAccount(account);
        }
    
        def updateAccount(long cardNumber, double balance):
            for (BankAccount account : self.cashRepository.getAccounts()) {
                if (account.getCardNumber() == cardNumber) {
                    account.setBalance(balance);
                    break;
                }
            }
        }
    
        def deleteAccount(long cardNumber):
            self.cashRepository.deleteAccount(cardNumber);
        }
    
        def readAccount(long cardNumber):
            return self.cashRepository.getAccount(cardNumber);
        }
    }
    
