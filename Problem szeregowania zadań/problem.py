import sys
import copy


class Problem:
    """Klasa odpowiedzialna za rozwiązanie części problemu"""
    def __init__(self, problem_size, tab, cores):
        """Funkcja inicjalizująca
        :parameter problem_size - liczba zadań do rozłożenia na rdzenie
        :parameter tab - tablica wielkości poszczególnych zadań
        :parameter cores - liczba rdzeni procesora
        """
        self.problem_size = problem_size
        self.tab = copy.deepcopy(tab)
        self.best_solution = []
        self.actual_solution_result = 0
        self.size = []
        for i in range(cores):
            self.size.append(0)
        self.cores = copy.deepcopy(cores)
        self.minimum_difference = sys.maxsize
        self.minimum_length = sys.maxsize
        self.work_range = None

    def set_work_range(self, work_range):
        """Procedura służąca do ustawienia zakresu kombinacji, jakie ma sprawdzić proces"""
        self.work_range = work_range

    def execute_brute_force(self):
        """Funkcja sprawdzająca wszystkie zadane kombinacje i zwracająca kombinacje zapewniające najkrótszy czas trwania zadań
        oraz najbardziej równomierne ich rozłożenie"""
        actual = self.work_range[0]     #Początkowa kombinacja
        stop = self.work_range[1]       #Kombinacja końcowa
        while True:
            for i in range(self.cores):  # Wyzerowanie tablic
                self.size[i] = 0
            for i in range(self.problem_size):  #Obliczenie obciążenia każdego rdzenia
                self.size[actual[i] - 1] += self.tab[i]
            minimum = min(self.size)    #Minimalny czas pracy - najkrócej pracujący rdzeń
            maximum = max(self.size)    #Maksymalny czas pracy - najdłużej pracujący rdzeń
            if maximum < self.minimum_length:   #Sprawdzenie, czy czas wykonania wszystkich zadań będzie krótszy niż obecnie najkrótszy
                self.minimum_length = maximum
                self.minimum_difference = maximum - minimum
                tab1 = copy.deepcopy(actual)
                self.best_solution.clear()
                self.best_solution.append(tab1)
            elif maximum == self.minimum_length:    #Sprawdzenie, czy czas wykonania wszystkich zadań jest taki sam, jak obecnie najkrótszy
                actual_difference = maximum - minimum
                tab1 = copy.deepcopy(actual)
                if actual_difference < self.minimum_difference: #Sprawdzenie, czy zadania są bardziej równomiernie rozłożone
                    self.minimum_difference = maximum - minimum
                    self.best_solution.clear()
                    self.best_solution.append(tab1)
                elif actual_difference == self.minimum_difference:
                    self.best_solution.append(tab1)
            if actual == stop:  #Weryfikacja, czy wszystkie kombinacje zostały sprawdzone
                if len(self.best_solution) > 0:
                    dictionary = {"Minimalny czas": self.minimum_length,
                                  "Minimalne odchylenie": self.minimum_difference}
                    self.best_solution.append(dictionary)
                break

            for i in range(self.problem_size - 1, -1, -1):    #Przejście do kolejnego obiegu
                if actual[i] == self.cores:
                    actual[i] = 1
                else:
                    actual[i] += 1
                    break
        return self.best_solution   #Zwrócenie wyniku


if __name__ == "__main__":
    pass
