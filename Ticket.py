    package Data;
    import java.time.LocalDateTime;
    
    class Ticket:
        private int id;
        private double price;
        private LocalDateTime dateTime;
        private boolean isValid;
    
        def Ticket(int id, double price, LocalDateTime dateTime, boolean isValid):
            self.id = id;
            self.price = price;
            self.dateTime = dateTime;
            self.isValid = isValid;
        }
    
        def getId():
            return self.id;
        }
    
        def setId(int id):
            self.id = id;
        }
    
        def getPrice():
            return self.price;
        }
    
        def setPrice(double price):
            self.price = price;
        }
    
        def getDateTime():
            return self.dateTime;
        }
    
        def setDateTime(LocalDateTime dateTime):
            self.dateTime = dateTime;
        }
    
        def getIsValid():
            return self.isValid;
        }
    
        def setIsValid(boolean isValid):
            self.isValid = isValid;
        }
    }
    
