class Node:
    def __init__(self, id, dish_name):
        self.id = id
        self.dish_name = dish_name
        self.next = None

class RestaurantQueue:
    def __init__(self):
        self.head = None

    def add_order(self, id, dish_name):
        new_order = Node(id, dish_name)
        
        if not self.head:
            self.head = new_order
            print(f"Order #{id} ({dish_name}) added.")
            return

        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_order
        print(f"Order #{id} ({dish_name}) added to the queue.")

    def show_orders(self):
        if not self.head:
            print("Order queue is empty.")
            return

        print("\nactive orders")
        current = self.head
        while current:
            print(f"Order #{current.id}: {current.dish_name}")
            current = current.next

if __name__ == "__main__":
    manager = RestaurantQueue()
    counter = 1

    while True:
        print("ORDER SYSTEM")
        print("1. Add Order")
        print("2. Show Queue")
        print("3. Exit")
        
        choice = input("Select an option (1-3):")

        if choice == "1":
            dish = input("Enter dish name:")
            manager.add_order(counter, dish)
            counter += 1
        elif choice == "2":
            manager.show_orders()
        elif choice == "3":
            print("Exiting")
            break
        else:
            print("Invalid choice")