    package Providers;
    import Data.BankAccount;
    import Data.User;
    import Repositories.UserRepository;
    
    class UserProvider:
        UserRepository userRepository;
    
        def UserProvider():
            self.userRepository = new UserRepository();
        }
    
        def createUser(String userName, int hashPassword, BankAccount account):
            User user = new User(self.userRepository.getUsers().size() + 1, userName, hashPassword, account);
            self.userRepository.setUser(user);
        }
    
        def updateUser(int index, String userName):
            self.userRepository.getUser(index).setUserName(userName);
        }
    
        def deleteUser(int index):
            self.userRepository.deleteUser(index);
        }
    
        def readUser(int index):
            return self.userRepository.getUser(index);
        }
    }
    
