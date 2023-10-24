    package Repositories;
    import java.util.ArrayList;
    import java.util.List;
    
    import Data.Ticket;
    
    class TicketRepository:
        private List<Ticket> tickets;
    
        def TicketRepository():
            self.tickets = new ArrayList<>();
        }
    
        def getTicket(int index):
            return self.tickets.get(index);
        }
    
        def setTicket(Ticket ticket):
            self.tickets.add(ticket);
        }
    
        def deleteTicket(int index):
            self.tickets.remove(index);
        }
    
        public List<Ticket> getTickets() {
            return self.tickets;
        }
    }
    
