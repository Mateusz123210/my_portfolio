import random
import math


class Generator:
    """Klasa pomocnicza"""
    @staticmethod
    def generate(nb_elements):
        """Funkcja zwraca listę losowych liczb naturalnych z przedziału <1, 1000000>"""
        tab = []
        for i in range(nb_elements):
            tab.append(random.randint(1, 1000001))
        return tab

    @staticmethod
    def get_division(nb_elements, nb_threads, nb_cores):
        """Funkcja zwraca listę podziałow kombinacji dla poszczególnych procesów"""
        all_combinations = math.pow(nb_cores, nb_elements)
        division = math.floor(all_combinations / nb_threads)
        rest = all_combinations - division * (nb_threads - 1)

        threads_tasks_ranges = []
        value = 0
        for i in range(nb_threads - 1):
            temp_tab = (Generator.convert_from_string_to_int_table(Generator.convert_to_fourth_system(value, nb_elements)),
                        Generator.convert_from_string_to_int_table(Generator.convert_to_fourth_system(value + division - 1, nb_elements)))
            threads_tasks_ranges.append(temp_tab)
            value += division

        temp_tab = (Generator.convert_from_string_to_int_table(Generator.convert_to_fourth_system(value, nb_elements)),
                    Generator.convert_from_string_to_int_table(
                        Generator.convert_to_fourth_system(value + rest - 1, nb_elements)))
        threads_tasks_ranges.append(temp_tab)
        return threads_tasks_ranges

    @staticmethod
    def convert_to_fourth_system(number: int, nb_elements: int):
        """Funkcja zwraca reprezentację czwórkową liczby dziesiętnej
        >>> [Generator.convert_to_fourth_system(4,4)]
        ['0010']
        >>> [Generator.convert_to_fourth_system(5,4)]
        ['0011']
        >>> [Generator.convert_to_fourth_system(9,4)]
        ['0021']
        >>> [Generator.convert_to_fourth_system(16,4)]
        ['0100']
        >>> [Generator.convert_to_fourth_system(19,4)]
        ['0103']
        >>> [Generator.convert_to_fourth_system(73,4)]
        ['1021']
        """
        tmp = ""
        result = ""
        while number > 0:
            temp = chr(int(number % 4) + 48)
            tmp += temp
            number /= 4

        for i in range(len(tmp), nb_elements):
            tmp += '0'

        for i in range(nb_elements, 0, -1):
            result += tmp[i - 1]

        return result

    @staticmethod
    def convert_from_string_to_int_table(string: str):
        """
        Fukncja konwertuje listę elementów zapisaną przy pomocy typu string na
        zwykłą listę zawierającą dane o typie integer(powiększone o 1)
        >>> Generator.convert_from_string_to_int_table("1111")
        [2, 2, 2, 2]
        >>> Generator.convert_from_string_to_int_table("1321")
        [2, 4, 3, 2]
        >>> Generator.convert_from_string_to_int_table("2222")
        [3, 3, 3, 3]
        >>> Generator.convert_from_string_to_int_table("3221")
        [4, 3, 3, 2]
        >>> Generator.convert_from_string_to_int_table("1011")
        [2, 1, 2, 2]
        >>> Generator.convert_from_string_to_int_table("1331")
        [2, 4, 4, 2]
        """
        l_strings = list(string)
        l_integers = [eval(x) + 1 for x in l_strings]

        return l_integers


if __name__ == "__main__":
    import doctest
    doctest.testfile("generator.py")
