    package Repositories;
    import java.util.ArrayList;
    import java.util.List;
    
    import Data.BankAccount;
    
    class CashRepository:
        private List<BankAccount> accounts;
    
        def CashRepository():
            self.accounts = new ArrayList<>();
        }
    
        def getAccount(long cardNumber):
            for (BankAccount account : self.accounts) {
                if (account.getCardNumber() == cardNumber) {
                    return account;
                }
            }
            return null;
        }
    
        def setAccount(BankAccount account):
            self.accounts.add(account);
        }
    
        def deleteAccount(long cardNumber):
            for (int i = 0; i < self.accounts.size(); i++) {
                if (self.accounts.get(i).getCardNumber() == cardNumber) {
                    self.accounts.remove(i);
                    break;
                }
            }
        }
    
        public List<BankAccount> getAccounts() {
            return self.accounts;
        }
    }
    
