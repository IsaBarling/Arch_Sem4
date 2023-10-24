    package Data;
    class User:
        protected int id;
        protected String userName;
        protected int hashPassword;
        protected BankAccount account;
    
        def User(int id, String userName, int hashPassword, BankAccount account):
            self.id = id;
            self.userName = userName;
            self.hashPassword = hashPassword;
            self.account = account;
        }
    
        def getId():
            return self.id;
        }
    
        def setId(int id):
            self.id = id;
        }
    
        def getUserName():
            return self.userName;
        }
    
        def setUserName(String userName):
            self.userName = userName;
        }
    
        def getHashPassword():
            return self.hashPassword;
        }
    
        def setDateTime(int hashPassword):
            self.hashPassword = hashPassword;
        }
    
        def getAccount():
            return self.account;
        }
    
        def setIsValid(BankAccount account):
            self.account = account;
        }
    }
    
