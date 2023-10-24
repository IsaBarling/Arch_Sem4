    package Data;
    
    import java.util.List;
    
    class Carrier:
        private int id;
        private List<String> routes;
        private BankAccount account;
    
        def Carrier(int id, List<String> routes, BankAccount account):
            self.id = id;
            self.routes = routes;
            self.account = account;
        }
    
        def getId():
            return self.id;
        }
    
        def setId(int id):
            self.id = id;
        }
    
        def geAccount():
            return self.account;
        }
    
        def setAccount(BankAccount account):
            self.account = account;
        }
    
        def addRoute(String route):
            self.routes.add(route);
        }
    
        def deleteRoute(int index):
            self.routes.remove(index);
        }
    }
    
