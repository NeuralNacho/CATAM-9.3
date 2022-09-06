from unittest import result
import random_sequence
import q8_vgap
import time
import numpy as np


class vgap_estimator:
    def __init__(self, u, p, n, runtime):
        self.u = u
        self.p = p
        self.n = n
        self.runtime = runtime
        self.no_tests = 1000**2 / n**2
        # no_tests is an alternative to runtime

    
    def generate_estimate(self):
        score_list = []
        t_end = time.time() + self.runtime
        # Will run for seconds of runtime
        while time.time() < t_end:
            U_n = random_sequence.random_sequence(self.p,
                                    self.n).get_sequence()
            V_n = random_sequence.random_sequence(self.p,
                                    self.n).get_sequence()
            test = q8_vgap.q8_vgap(U_n, V_n, self.u)
            score = test.get_score()
            score_list.append(score)
        
        self.estimate = (sum(score_list) / len(score_list)) \
                        / self.n


    def get_estimate(self):
        self.generate_estimate()
        return self.estimate


if __name__ == '__main__':
    # For first part of Question 8

    def return_estimate(n, runtime):
        # Finds error of the estimate
        # runtime in seconds
        estimate_list = []
        no_estimates = 2
        # 10 tests will give good idea of error of standard  
        # deviation especially considering each item of 
        # estimate_list involves 1000s of tests itself
        for _ in range(no_estimates):
            estimator = vgap_estimator(-3, 1/2, n, 
                                runtime / no_estimates)
            estimate_list.append(estimator.get_estimate())
        
        print(estimate_list)
        estimate_mean = sum(estimate_list) / \
                        len(estimate_list)
        estimate_error = max(estimate_list) - \
                        min(estimate_list)
        std_dev = np.std(estimate_list)

        return estimate_mean, estimate_error, std_dev

    n = 4000
    initial_runtime = 1
    result1 = return_estimate(n, initial_runtime)
    # Want a standard deviation of 0.05 / 3 since then 
    # 99.7% chance that result lies within 0.05 of mean
    time_multiplier = 2 * result1[2] / (0.05 / 3)
    # Increase time by certain amount for more accuracy
    # Assume time and error are approximately proportional
    # but *2 to make sure enough accuracy
    time_remaining = time_multiplier * initial_runtime
    print('Time remaining: ', time_remaining, '\n')
    result2 = return_estimate(n, time_remaining)


    print('v_gap estimate: ', result2[0])
    print('v_gap standard deviation: ', result2[2])
    print('v_gap error: ', result2[1])



