class Path:
    def __init__(self, pairs, indices=None):
        self.indices = indices
        self.pairs = []
        for i in indices:
            self.pairs.append(pairs[i]) # Crea una lista de pares a partir de los índices de la lista de pares

    def upper(self):
        # Devuelve una cadena que representa el camino A a través de la lista de pares
        return "".join([pair[0] for pair in self.pairs])

    def lower(self):
        # Devuelve una cadena que representa el camino B a través de la lista de pares
        return "".join([pair[1] for pair in self.pairs])

    def is_solution(self):
        return self.upper() == self.lower()

    def has_possible_solution(self):
        # Devuelve True si las cadenas superior e inferior tienen un prefijo común
        return self.upper().startswith(self.lower()) or self.lower().startswith(self.upper())


class P_:
    def __init__(self, pairs):
        self.pairs = pairs

        all_paths = []
        for i in range(len(pairs)):
            all_paths.append(Path(pairs, [i]))

        # Filtra los paths que tienen una solución posible
        self.possible_paths = []
        for path in all_paths:
            if path.has_possible_solution():
                self.possible_paths.append(path)


    def solve(self):
        # Intenta resolver el problema agregando un par a cada path posible hasta encontrar una solución o hasta que no haya rutas posibles
        if not self.possible_paths:
            print("No solution!")
            return None

        new_paths = []
        for path in self.possible_paths:
            for i in range(len(self.pairs)):
                new_path = Path(self.pairs, path.indices + [i]) # Agrega un par al path
                if new_path.is_solution():
                    return new_path
                    # Si el nuevo path es una solución, devuelve el nuevo path
                if new_path.has_possible_solution():
                    new_paths.append(new_path)
                    # Si el nuevo path tiene una solución posible, lo agrega a la lista de paths posibles
        self.possible_paths = new_paths
        # Actualiza la lista de paths posibles
        return self.solve()


if __name__ == "__main__":
    #pairs (A, B)
    pairs = [("aab", "a"), ("ab", "abb"), ("ab", "bab"), ("ba", "aab")]

    P = P_(pairs)
    solution = P.solve()
    print("A: {upper}".format(upper=solution.upper()))
    print("B: {lower}".format(lower=solution.lower()))
    print("Solution: {indices}".format(indices=solution.indices))
    print("Pairs needed: {pairs} ".format(
        pairs=len(solution.pairs)
    ))