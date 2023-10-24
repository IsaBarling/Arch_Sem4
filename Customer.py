    import java.util.ArrayList;
    import java.util.List;
    
    import Data.BankAccount;
    import Data.Ticket;
    import Data.User;
    
    public class Customer extends User {
        private List<Ticket> tickets;
    
        def Customer(int id, String userName, int hashPassword, BankAccount account):
            super(id, userName, hashPassword, account);
            self.tickets = new ArrayList<>();
        }
    
        def addTicket(Ticket ticket):
            self.tickets.add(ticket);
        }
    
        def refundTicket(int index):
            Ticket ticket = self.tickets.get(index);
            self.tickets.remove(index);
            return ticket;
        }
    
    }
    
