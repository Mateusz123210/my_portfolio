"""
Program obliczający czas rozwiązania problemu szeregowania zadań na procesorze
czterordzeniowym w zależności od liczby użytych procesów. Chodzi o to, aby tak ułożyć zadania, aby każdy procesor
pracował przez tą samą długość czasu (rozbieżność pomiędzy czasem pracy rdzenia pracującego najkrócej oraz
rdzenia pracującego najdłużej powinna być jak najmniejsza).
"""
from problem import Problem as p
from generator import Generator as g
import time
import ray


class Algorithm:
    """Klasa główna """
    def __init__(self, choice, tasks, processes):
        """Funkcja inicjalizująca
        :parameter choice - tryb pracy
        :parameter tasks - liczba zadań
        :parameter processes - liczba procesów"""
        self.tasks = tasks
        self.processes = processes
        self.problem = []
        self.choice = choice
        self.start_algorithm()


    @staticmethod
    @ray.remote
    def execute_brute_force(problem, i):
        """Funkcja uruchamiana osobno dla każdego procesu"""
        return problem[i].execute_brute_force()

    def start_algorithm(self):
        """Funkcja główna algorytmu"""
        if self.choice == 1:                #Pobranie danych wejściowych z konsoli
            x = int(input("Podaj, ile zadań jest do wykonania: "))
            y = int(input("Podaj, na ile procesów chcesz podzielić pracę: "))
        else:
            x = self.tasks
            y = self.processes

        if x < 1 or y < 1:
            print("Podano nieprawidłowe parametry początkowe!")
            exit()
        cores = 4
        tasks_sizes = g.generate(x)     #Wygenerowanie losowych rozmiarów zadań

        if y == 1:  #Wykonanie sekwencyjne
            start_time = time.time()                            #Rozpoczęcie pomiaru czasu
            problem = p(x, tasks_sizes, cores)                  #Stworzenie obiektu klasy Problem
            threads_tasks_ranges = g.get_division(x, y, cores)  #Obliczenie pierwszej oraz ostatniej kombinacji do sprawdzenia
            problem.set_work_range(threads_tasks_ranges[0])     #Ustaweinie zakresu kombinacji algorytmu
            all_results = problem.execute_brute_force()         #Wykonanie algorytmu i zapisanie wyników
            all_results_length = len(all_results)
            minimum_length = all_results[all_results_length - 1].get("Minimalny czas")
            minimum_difference = all_results[all_results_length - 1].get("Minimalne odchylenie")
            all_results.pop(-1)
            stop_time = time.time()                             #Zakończenie pomiaru czasu
            all_time = stop_time - start_time                   #Obliczenie czasu wykonania
        else:   #Wykonanie przy użyciu wielu procesów
            start_time = time.time()                            #Rozpoczęcie pomiaru czasu
            for i in range(y):
                self.problem.append(p(x, tasks_sizes, cores))   #Stworzenie obiektu klasy Problem dla każdego procesu
            threads_tasks_ranges = g.get_division(x, y, cores)  #Obliczenie zakresów kombinacji dla każdego procesu
            for i in range(y):
                self.problem[i].set_work_range(threads_tasks_ranges[i])     #Przypisanie każdemu procesowi zakresu jego pracy
            futures = [self.execute_brute_force.remote(self.problem, a) for a in range(y)]  #Równoległe wykonanie procesów
            all_results = ray.get(futures)  #Pobranie wyników procesów
            first_length = len(all_results[0])
            minimum_length = all_results[0][first_length - 1].get("Minimalny czas")
            minimum_difference = all_results[0][first_length - 1].get("Minimalne odchylenie")
            temp = all_results[0]
            temp.pop(-1)
            actual_minimum = temp
            temp2 = len(all_results)
            for a0 in range(1, temp2):          #Łączenie wyników ze wszystkich procesów
                temp3 = len(all_results[a0])
                temp = all_results[a0]
                temp_length = all_results[a0][temp3 - 1].get("Minimalny czas")
                temp_difference = all_results[a0][temp3 - 1].get("Minimalne odchylenie")
                temp.pop(-1)
                if temp_length < minimum_length:
                    actual_minimum.clear()
                    actual_minimum.extend(temp)
                    minimum_length = temp_length
                    minimum_difference = temp_difference
                elif temp_length == minimum_length:
                    if temp_difference < minimum_difference:
                        actual_minimum.clear()
                        actual_minimum.extend(temp)
                        minimum_difference = temp_difference
                    elif temp_difference == minimum_difference:
                        actual_minimum.extend(temp)
            all_results.clear()
            all_results = actual_minimum
            stop_time = time.time()                 #Zakończenie pomiaru czasu
            all_time = stop_time - start_time       #Obliczenie czasu wykonania
        print("==================")
        print("Rozmiary zadań: " + str(tasks_sizes))
        print("Liczba procesów: " + str(y))
        print("Czas pracy algorytmu: " + str(stop_time - start_time))
        print("------------------")
        print("Rozwiązania: " + str(all_results))
        print("Minimalny czas " + str(minimum_length))
        print("Minimalna różnica wynosi: " + str(minimum_difference))

        with open("results.csv", "a") as f:         #Zapisanie wyników do pliku csv
            f.write(str(x) + ";" + str(y) + ";" + str(all_time) + '\n\n')


if __name__ == "__main__":
    print("--------------")
    print("Witaj w programie obliczającym czas rozwiązania problemu szeregowania zadań!")
    print("Jeżeli chcesz wybrać liczbę zadań i procesów - wpisz 1.")
    print("Jeżeli chcesz wykonać serię obliczeń - wpisz coś innego.")
    choice = int(input("Wybór: "))
    if choice == 1:
        Algorithm(1, 1, 1)
    else:
        for i in range(5):
            for j in range(3, 13):
                print("iteration: "+str(i)+" tasks: " + str(j))
                for k in range(1, 50):
                    Algorithm(2, j, k)
                print(50)
                for k in range(50, 101, 5):
                    Algorithm(2, j, k)


