"""
  @author: yigit.yildirim@boun.edu.tr
"""
import time
import random
from producer import Producer
from customer import Customer


class Market:
    def __init__(self):
        self.max_production_capacity = 1000
        self.max_request = 500

        self.max_time = 100
        self.current_time = 0

        self.producers = []
        for i in range(2):
            self.producers.append(Producer(self.max_production_capacity))

        self.customers = []
        for i in range(3):
            self.customers.append(Customer(self.max_time, self.max_request))

        self.inventory = random.randint(0, 100)

    def run(self):
        while self.current_time < self.max_time:
            print("Day " + str(self.current_time) + ":")
            for customer in self.customers:
                if self.current_time == customer.request_time:
                    self.make_request(customer)
            time.sleep(1)
            self.current_time += 1

    def make_request(self, customer):
        if self.inventory < customer.order:
            # add to queue
            # queue.enqueue(customer)
            print("added to queue")


m = Market()
m.run()
