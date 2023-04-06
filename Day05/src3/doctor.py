import threading


def go_doc():
    docs_list = ["Doctor 9", "Doctor 10", "Doctor 11", "Doctor 12", "Doctor 13"]
    screw = [threading.Semaphore() for n in range(5)]  # инициализация массива отверток

    # here (i+1)%5 is used to get right and left screw circularly between 1-5
    doctors = [Doctor(docs_list[i], screw[i % 5], screw[(i + 1) % 5])
               for i in range(5)]
    Doctor.running = True
    for p in doctors:
        p.start()

    for p in doctors:
        p.join()

    Doctor.running = False
    # print("Now we're finishing.")


class Doctor(threading.Thread):
    running = True  # используется, чтобы проверить, все ли закончили "blast"

    def __init__(self, index, on_left, on_right):
        threading.Thread.__init__(self)
        self.index = index
        self.on_left = on_left
        self.on_right = on_right

    def run(self):
        while self.running:
            # print(f'Dpc {self.index} is hungry')
            self.blast()

    def blast(self):
        # если обе свободны, стреляет
        screw1, screw2 = self.on_left, self.on_right
        while self.running:
            screw1.acquire()  # ждать операции слева
            locked = screw2.acquire(False)
            if locked:  # если правая недоступна, оставить левую
                break
            screw1.release()
            # print(f'doc swaps forks{self.index}')
            screw1, screw2 = screw2, screw1
        else:
            return
        self.blasting()
        # отпустить обе
        screw2.release()
        screw1.release()

    def blasting(self):
        # print("Doctor {index}: BLAST!".format(index=self.index))
        print(f"{self.index}: BLAST!")
        self.running = False
        # print(f"ждет {self.index}")


if __name__ == "__main__":
    go_doc()
