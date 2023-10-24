    package Repositories;
    
    import java.util.ArrayList;
    import java.util.List;
    
    import Data.Carrier;
    
    class CarrierRepository:
        private List<Carrier> carriers;
    
        def CarrierRepository():
            self.carriers = new ArrayList<>();
        }
    
        def getCarrier(int index):
            return self.carriers.get(index);
        }
    
        def setCarrier(Carrier carrier):
            self.carriers.add(carrier);
        }
    
        def deleteCarrier(int index):
            self.carriers.remove(index);
        }
    
        public List<Carrier> getCarriers() {
            return self.carriers;
        }
    }
    
