import threading


class Doctor(threading.Thread):
    def __init__(self, number, left_fork, right_fork, lock):
        threading.Thread.__init__(self)
        self.number = number
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.lock = lock

    def run(self):
        while True:
            self.lock.acquire()
            self.left_fork.acquire()
            self.right_fork.acquire()
            print(f"Doctor {self.number}: BLAST!")
            self.right_fork.release()
            self.left_fork.release()
            self.lock.release()


if __name__ == "__main__":
    n_doctors = 5
    forks = [threading.Lock() for i in range(n_doctors)]
    lock = threading.Lock()
    doctors = [Doctor(i, forks[i], forks[(i+1)%n_doctors], lock) for i in range(n_doctors)]
    for doctor in doctors:
        doctor.start()