    package Providers;
    import java.time.LocalDateTime;
    
    import Data.Ticket;
    import Repositories.TicketRepository;
    
    class TicketProvider:
        TicketRepository ticketRepository;
    
        def TicketProvider():
            self.ticketRepository = new TicketRepository();
        }
    
        def createTicket(double price, LocalDateTime dateTime):
            Ticket ticket = new Ticket(self.ticketRepository.getTickets().size() + 1, price, dateTime, true);
            self.ticketRepository.setTicket(ticket);
        }
    
        def updateTicket(int index, boolean isValid):
            self.ticketRepository.getTicket(index).setIsValid(isValid);
        }
    
        def deleteTicket(int index):
            self.ticketRepository.deleteTicket(index);
        }
    
        def readTicket(int index):
            return self.ticketRepository.getTicket(index);
        }
    }
    
