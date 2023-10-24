    package Repositories;
    import java.util.ArrayList;
    import java.util.List;
    
    import Data.User;
    
    class UserRepository:
        private List<User> users;
    
        def UserRepository():
            self.users = new ArrayList<>();
        }
    
        def getUser(int index):
            return self.users.get(index);
        }
    
        def setUser(User user):
            self.users.add(user);
        }
    
        def deleteUser(int index):
            self.users.remove(index);
        }
    
        public List<User> getUsers() {
            return self.users;
        }
    }
    
