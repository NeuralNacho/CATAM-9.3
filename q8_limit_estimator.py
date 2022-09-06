import matplotlib.pyplot as plt
import time
import q8_vgap
import random_sequence


class limit_estimator:
    def __init__(self, u, p):
        self.u = u
        self.p = p
        self.x_list = []
        self.y_list = []


    def generate_estimate(self, n):
        score_list = []
        t_end = time.time() + 1
        # Will give 1 seconds for estimate at individual n
        # For any n in the 1000s this will only give
        # Enough time for 1 test
        while time.time() < t_end:
            U_n = random_sequence.random_sequence(self.p, n)\
                                            .get_sequence()
            V_n = random_sequence.random_sequence(self.p, n)\
                                            .get_sequence()
            test = q8_vgap.q8_vgap(U_n, V_n, self.u)
            score = test.get_score()
            score_list.append(score)
        
        estimate = sum(score_list) / (n * len(score_list))
        return estimate


    def generate_graph(self):
        n = 100
        self.x_list.append(n)
        self.y_list.append(self.generate_estimate(n))
        old_estimate = self.y_list[0]
        new_estimate = old_estimate + 3
        while n < 10000:
        #while abs(new_estimate - old_estimate) > 2:
            n = int(n*1.25)
            print(n)
            self.x_list.append(n)
            self.y_list.append(self.generate_estimate(n))
            old_estimate = new_estimate
            new_estimate = self.y_list[-1]
    

    def plot(self):
        self.generate_graph()
        plt.rc('font', size = 24)
        plt.figure(1)
        plt.grid(linestyle = '--', linewidth = 0.5)
        plt.plot(self.x_list, self.y_list, color = 'C0')
        plt.xlabel('$n$')
        plt.ylabel('$Estimate$') 

        plt.show()


if __name__ == '__main__':
    estimator = limit_estimator(-3, 1/2)
    estimator.plot()