# Input packets as a string, S=Standard, P=Priority, E=Economy
input_packets = ["S Mary", "P Dee", "P Dee", "E Eileen",
                 "E Mike", "E Joe", "P Dee", "E Vicky", "E George",
                 "P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
                 "P Dee", "S Bill", "S Chase", "E Price", "P Dee",
                 "E Sue"]

# Create three queues for priority levels:
premium_queue = []
standard_queue = []
economy_queue = []

# Enqueue packets into respective queues:
for packet in input_packets:
    if packet.startswith('P'):
        premium_queue.append(packet)
    if packet.startswith('S'):
        standard_queue.append(packet)
    if packet.startswith('E'):
        economy_queue.append(packet)


# Function to dequeue print packets based on WFQ
def wfq(premium_queue, standard_queue, economy_queue):
    while premium_queue or standard_queue or economy_queue:
        # Print 3 Premium packets if available:
        for packet in range(3):
            if premium_queue:
                print(premium_queue.pop(0))

        # Print 2 Standard packets if available:
        for packet in range(2):
            if standard_queue:
                print(standard_queue.pop(0))

        # Print 1 Economy packet if available
        if economy_queue:
            print(economy_queue.pop(0))


# Execute WFQ
wfq(premium_queue, standard_queue, economy_queue)
