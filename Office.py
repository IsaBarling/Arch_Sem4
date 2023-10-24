    import Data.Ticket;
    import Providers.CarrierProvider;
    import Providers.CashProvider;
    import Providers.TicketProvider;
    import Providers.UserProvider;
    
    class Office:
        TicketProvider ticketProvider;
        UserProvider userProvider;
        CarrierProvider carrierProvider;
        CashProvider cashProvider;
    
        def Office():
            self.ticketProvider = new TicketProvider();
            self.userProvider = new UserProvider();
            self.carrierProvider = new CarrierProvider();
            self.cashProvider = new CashProvider();
        }
    
        def saleTicket(Customer customer, int index):
            Ticket ticket = self.ticketProvider.readTicket(index);
            double restBalance = self.cashProvider.readAccount(customer.getAccount().getCardNumber()).getBalance() - ticket.getPrice();
            if (restBalance >= 0) {
                customer.getAccount().setBalance(restBalance);
                customer.addTicket(ticket);
            } else {
                throw new RuntimeException("Imposible to buy the ticket");
            }
        }
    
        def refundTicket(Customer customer, int index):
            Ticket ticket = customer.refundTicket(index);
            customer.getAccount().setBalance(customer.getAccount().getBalance() + ticket.getPrice());
            self.ticketProvider.createTicket(ticket.getPrice(), ticket.getDateTime());
        }
    }
    
