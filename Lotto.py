# Zach Walden
# w989j327
################### Lottery Scheduling ###################

### Features: ###
"""
# Process class that throws an error for non-unique PIDs,
starting with 0 tickets until assigned.

# Scheduler class that handles scheduling of the lottery. 
Including adding processes, allocating a given amount of tickets,
and choose the winning process.
- Random number generator is used to choose the winning ticket number.

"""

import random

# Process Class
class Process():
    # Store a list of used PIDS to prevent duplicate PIDs
    used_pids = set()

    # Each process will hold it's tickets assigned & PID number
    def __init__(self, pid):
        if pid in Process.used_pids:
            raise ValueError(f"Pid {pid} is already assigned.")
        self.tickets = 0
        self.pid = pid
        Process.used_pids.add(pid)

# Lottery Scheduling Class  
class LottoScheduler():

    # Initialize process list & total ticket number to empty
    def __init__(self):
        self.processes = []
        self.ticket_total = 0
    
    # Add Proccess to the lotto scheduler
    def add_process(self, process):

        # Handle lists of processes to append
        if type(process) is list:
            for item in process:
                #Verify non-duplicate PIDs for each process
                if item.pid in self.processes:
                    raise ValueError(f"PID {process.pid} is already scheduled!")
                self.processes.append(item)
            return


        #Verify non-duplicate PIDs
        if process.pid in self.processes:
            raise ValueError(f"PID {process.pid} is already scheduled!")
        
        # Handle single process to append
        if type(process) is Process:
            self.processes.append(process)
            return

    
    #Takes in process & total tickets to be allotted to the process.
    def allocate_tickets(self, process, tickets):
        if process in self.processes:
            process.tickets = self.ticket_total + tickets
            self.ticket_total += tickets
        else:
             raise ValueError("Process not assigned to scheduler.")

    # Choose the winning ticket
    def choose_process(self):
        # Total tickets will be the final ticket number
        total_tickets = self.processes[-1].tickets

        # Generate winning number
        winning_num = random.randint(0, total_tickets)

        for p in self.processes:
            # If within the range of tickets assigned to process, they are chosen
            if winning_num < p.tickets or p.tickets == self.ticket_total:
                return p
            
        raise ValueError("wow")

# Create Scheduler object
Lotto = LottoScheduler()

# Add all processes to lottery scheduler
Lotto.add_process([Process(1), Process(2), Process(3), Process(4), Process(5)])

# Allocate tickets to each process in lotto.
# Process one, the first list item will be more likely than
# the other processes to be picked.

# Process = list position + 1
Lotto.allocate_tickets(Lotto.processes[0], 50)  # < 50
Lotto.allocate_tickets(Lotto.processes[1], 10)  # < 60
Lotto.allocate_tickets(Lotto.processes[2], 10)  # < 70
Lotto.allocate_tickets(Lotto.processes[3], 10)  # < 80
Lotto.allocate_tickets(Lotto.processes[4], 20)  # < 80

#Find the chosen process, and print the winner
chosen_process = Lotto.choose_process()
print(f"Process {chosen_process.pid} wins the lottery!")