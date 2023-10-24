    package Providers;
    
    import java.util.List;
    
    import Data.BankAccount;
    import Data.Carrier;
    import Repositories.CarrierRepository;
    
    class CarrierProvider:
        CarrierRepository carrierRepository;
    
        def CarrierProvider():
            self.carrierRepository = new CarrierRepository();
        }
    
        def createCarrier(List<String> routes, BankAccount account):
            Carrier carrier = new Carrier(self.carrierRepository.getCarriers().size() + 1, routes, account);
            self.carrierRepository.setCarrier(carrier);
        }
    
        def updateCarrier(int index, String route):
            self.carrierRepository.getCarrier(index).addRoute(route);
        }
    
        def deleteCarrier(int index):
            self.carrierRepository.deleteCarrier(index);
        }
    
        def readCarrier(int index):
            return self.carrierRepository.getCarrier(index);
        }
    
    }
    
