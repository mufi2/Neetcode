class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        def f_deri(X):
            f_deri_out = 2 * X
            return f_deri_out

        Back_log = []
        for i in range(1, iterations + 1, 1):
            f = f_deri(init)
            init = init - (learning_rate * f)
            Back_log.append(init)
        return round(init, 5)
