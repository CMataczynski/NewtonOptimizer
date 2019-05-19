from parse import *
from math import sqrt
import matplotlib.pyplot as plt

class HistoryOfOptimization:
    def __init__(self,n = 1000):
        self.history = []
        self.current_size = 0
        self.max_size = n

    def get_last_entry(self):
        return self.history[-1]

    def get_whole_history(self):
        return self.history

    def __getitem__(self, item):
        return self.history[item]

    def append(self,value):
        self.history.append(value)
        if self.current_size == self.max_size:
            self.history = self.history[1:]
            return -1
        return None



class NewtonOptimizer:
    def __init__(self, fcn, x0, epsilon, epsilon1, epsilon2, n, initial_step, beta):
        self.iterator = 0
        self.goldstein_iterator = 0
        self.ending_criterion = None
        # punkt startowy
        self.x0 = x0
        #Macierz kierunków poszukiwań
        self.epsilon = epsilon
        self.epsilon1 = epsilon1
        self.epsilon2 = epsilon2
        self.maxsteps = n
        self.initial_step_direction = initial_step
        self.beta = beta
        # funkcja do optymalizacji
        self.function = fcn
        self.f0 = fcn.evaluate_expression(x0)
        self.g0 = fcn.evaluate_gradient(x0)
        self.h0 = fcn.evaluate_hessian(x0)
        self.history = HistoryOfOptimization(1000)
        self.history.append({
            'x': self.x0,
            'g': self.g0,
            'f': self.f0,
            'h': self.h0,
            'starting_point': True
        })

        self.x = self.x0
        self.g = self.g0
        self.h = self.h0
        self.f = self.f0
        self.criterion1 = 0
        self.criterion2 = 0
        self.criterion3 = 0
        self.error_flag = False
        self.error_message = None
        self.error_no = None
        self.min_lok = False

    def __str__(self):
        message = "punkt: ["
        for key in self.x:
            message += str(self.x[key])
            message += ', '
        message = message[:-2]+']\n'
        message += 'gradient: ' + str(self.g) + '\n'
        message += 'hesjan: ' + str(self.h) + '\n'
        message += 'wartosc: ' + str(self.f) +'\n'
        message += 'kryterium 1: ' + str(self.criterion1) +'\n'
        message += 'kryterium 2: ' + str(self.criterion2) +'\n'
        message += 'kryterium 3: ' + str(self.criterion3) +'\n'
        if self.error_flag:
            print("Error" + str(self.error_no) + ": " + self.error_message)
        return message

    def result(self):
        return self.x

    def why(self):
        if self.min_lok:
            return "Punkt siodlowy, zakonczono przez " + self.ending_criterion
        return self.ending_criterion

    def __len__(self):
        return self.iterator

    def show_image(self,resolution = 256):
        result = self.result()
        start = self.history[0]["x"]
        resolution = resolution
        multiplicator = 0.15
        x1_list = []
        x2_list = []
        for i in self.history:
            x1_list.append(i["x"]["x1"])
            x2_list.append(i["x"]["x2"])
        x1_min = min(x1_list)
        x1_max = max(x1_list)
        x2_min = min(x2_list)
        x2_max = max(x2_list)
        xl = x1_min - multiplicator * abs(x1_min - x1_max)
        xr = x1_max + multiplicator * abs(x1_min - x1_max)
        if abs(xl-xr) < 0.2:
            xl = xl - 0.5
            xr = xr + 0.5

        yl = x2_min - multiplicator * abs(x2_max - x2_min)
        yr = x2_max + multiplicator * abs(x2_max - x2_min)
        if abs(yl-yr) < 0.2:
            yl = yl - 0.5
            yr = yr + 0.5

        x = np.linspace(xl, xr, resolution)
        y = np.linspace(yl, yr, resolution)
        outer = np.zeros([len(x), len(y)])
        for i in range(len(x)):
            for j in range(len(y)):
                outer[i,j] = self.function.evaluate_expression({"x1": x[i], "x2": y[j]})
        outer = np.rot90(outer)
        x = []
        y = []
        for i, item in enumerate(self.history):
            x.append(item["x"]["x1"])
            y.append(item["x"]["x2"])
        return {
            "imshow": [outer, [xl, xr, yl, yr], abs(xr - xl) / abs(yr - yl)],
            "plot1": [x, y],
            "plot2": [[result["x1"]],[result["x2"]]]
        }

    def point_dict_to_list(self,point):
        return [point[key] for key in point]

    def point_list_to_dict(self,point):
        x_new = dict()
        for i in range(len(point)):
            x_new['x' + str(i + 1)] = point[i]
        return x_new

    def measure(self,x1,x2):
        sum = 0
        for i in range(len(x1)):
            sum+=abs(x1[i]-x2[i])
        return sum


    def minimize_in_direction(self, x0, d):
        beta = self.beta
        d = np.array(d)
        x0 = np.array(x0)
        self.goldstein_iterator = 0
        grad = np.array(self.function.evaluate_gradient(self.point_list_to_dict(x0)))
        p = np.dot(grad,d)
        f0 = self.function.evaluate_expression(self.point_list_to_dict(x0))
        tr = self.initial_step_direction
        while f0 <= self.function.evaluate_expression(self.point_list_to_dict(x0 + tr*d)):
            tr = tr/2
        return self.goldstein_algo(x0,d,0,tr,beta,p,f0)

    def goldstein_algo(self,x0, d, tl, tr, beta, p, f0):
        t = (tl+tr)/2
        if self.goldstein_iterator >= 1000:
            return t
        new_point = self.point_list_to_dict(x0+t*d)
        f_new = self.function.evaluate_expression(new_point)
        if f_new < f0 + (1-beta)*p*t:
            self.goldstein_iterator += 1
            return self.goldstein_algo(x0, d, t, tr, beta, p, f0)
        elif f_new > f0 + beta*p*t:
            self.goldstein_iterator += 1
            return self.goldstein_algo(x0, d, tl, t, beta, p, f0)
        else:
            return t

    def compute_integrity_ctiterion(self,x1, f1, g1, x2, f2, g2):
        criterion1 = abs(np.dot(g1,g2.T))

        criterion2 = 0
        for key in x1:
            criterion2 += (x1[key]-x2[key])**2
        criterion2 = sqrt(criterion2)

        func = self.function
        criterion3 = abs(f1-f2)

        return criterion1, criterion2, criterion3

    def check_integrity_criterions(self):
        if self.criterion1 < self.epsilon:
            self.ending_criterion = "Kryterium 1"
            return False

        if self.criterion2 < self.epsilon1:
            self.ending_criterion = "Kryterium 2"
            return False

        if self.criterion3 < self.epsilon2:
            self.ending_criterion = "Kryterium 3"
            return False
        return True

    def optimize_step(self):
        #Sprawdzanie liczby iteracji
        if self.iterator > self.maxsteps:
            self.error_flag = True
            self.error_message = "Przekroczono maksymalną liczbę iteracji({})".format(self.maxsteps)
            self.error_no = 1
            return False

        #Sprawdzanie wyznacznika hesjanu
        wyznacznik = np.linalg.det(self.h)
        if wyznacznik == 0:
            self.error_flag = True
            self.error_message = "Wyznacznik hesjanu równy {}. Podaj nowy punkt początkowy".format(wyznacznik)
            self.error_no = 2
            return False

        if wyznacznik < 0:
            self.min_lok = True
        else:
            self.min_lok = False

        #Wyznaczanie kierunku poszukiwań
        dk = -1 * np.dot(np.linalg.inv(self.h), self.g)
        x_act = self.point_dict_to_list(self.x)
        #Wyznaczanie alfy minimalizacją w kierunku
        alfa = self.minimize_in_direction(x_act, dk)
        #Utworzenie nowej wartosci x
        x_new = x_act+alfa*dk
        x_new = self.point_list_to_dict(x_new)
        #Wyznaczenie parametrów do kolejnego kroku algorytmu
        f_new = self.function.evaluate_expression(x_new)
        g_new = self.function.evaluate_gradient(x_new)
        h_new = self.function.evaluate_hessian(x_new)
        criterions = self.compute_integrity_ctiterion(self.x, self.f, self.g, x_new, f_new, g_new)
        self.history.append({
            'x': x_new,
            'g': g_new,
            'h': h_new,
            'f': f_new,
            'criterion1': criterions[0],
            'criterion2': criterions[1],
            'criterion3': criterions[2],
            'starting_point': False
            })
        self.x = x_new
        self.g = g_new
        self.h = h_new
        self.f = f_new
        self.criterion1 =criterions[0]
        self.criterion2 =criterions[1]
        self.criterion3 =criterions[2]
        self.iterator += 1
        return self.check_integrity_criterions()


if __name__ == "__main__":

    # fcn = FunctionParse("x1^3 + (x2-2)^2 + (x3 - 8)^2 + x4^2 + 2")
    # point = {"x1": 1, "x2": 5, "x3": 7, "x4": 1}

    # fcn = FunctionParse("(x1-2)**2 + (x1-x2**2)**2")
    # point = {"x1": 1, "x2": 5}

    # 4 minima lokalne
    # fcn = FunctionParse("x1**4 + x2 **4 - 0.62*x1**2 - 0.62*x2**2")
    # point = {"x1": 4, "x2": 0.2}

    # Rosenbrock
    fcn = FunctionParse("100*(x2-x1**2)**2+(1-x1)**2")
    point = {"x1": -1.2, "x2": 1.0}

    # Zangwill
    # fcn = FunctionParse("(x1 - x2 + x3)**2 + (-x1 + x2 + x3)**2 + (x1 + x2 - x3)**2")
    # point = {"x1": 100, "x2": -1, "x3": 2.5}

    # Goldstein-Price
    # fcn = FunctionParse("(1 + ((x1 + x2 + 1)**2)*(19-14*x1+3*x1**2-14*x2+6*x1*x2 + 3*x2**2))*((30+(2*x1-3*x2)**2)*(18-32*x1+12*x1**2+48*x2-36*x1*x2+27*x2**2))")
    # point = {"x1": -0.4, "x2": -0.6}

    # print(fcn.evaluate_expression(point))
    # print(fcn.evaluate_gradient(point))
    # print(fcn.evaluate_hessian(point))
    optimizer = NewtonOptimizer(fcn, point, 1e-8, 1e-8, 1e-8, 1000, 10, 3/5)
    print(optimizer)
    while(optimizer.optimize_step()):
        print('krok: ' + str(len(optimizer)))
        print(optimizer)
    print('krok: ' + str(len(optimizer)))
    print(optimizer)
    print(optimizer.why())
    optimizer.show_image()


#Wyznacznik hesjanu > 0
#W innym przypadku podać inny punkt startowy
#Metoda gradientowa minimum w kierunku