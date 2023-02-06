# Exercises: Level 1
# 01 - Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
class Statistics:
    def __init__(self, data):
        self.data = data
    
    def count(self):
        return len(self.data)
    
    def sum(self):
        return sum(self.data)
    
    def mean(self):
        return self.sum() / self.count()
    
    def median(self):
        sorted_data = sorted(self.data)
        mid = self.count() // 2
        if self.count() % 2 == 0:
            return(sorted_data[mid - 1] + sorted_data[mid] / 2)
        else:
            return sorted_data[mid]
    
    def mode(self):
        freq = {}
        for i in self.data:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        max_freq = max(freq.values())
        mode = [k for k, v in freq.items() if v == max_freq]
        return{'mode':mode,'count':max_freq}
    
    def range(self):
        return self.max() - self.min()

    def var(self):
        mean = self.mean()
        variance = sum((x-mean)**2 for x in self.data) / self.count()
        return round(variance,1)

    def std(self):
        variance = self.var()
        return round(variance ** 0.5,1)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def freq_dist(self):
        freq_dist = {}
        for value in self.data:
            if value not in freq_dist:
                freq_dist[value] = 1
            else:
                freq_dist[value] += 1
        freq_list = [(count, value) for value, count in freq_dist.items()]
        freq_list.sort(reverse=True)
        freq_dist = [(100*count/len(self.data), value) for count, value in freq_list]
        return freq_dist

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]


# 02 - Exercises: Level 2
# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.
print('''
------ Exercise 2 ------''')
class PersonAccount:
    def __init__(self, firstname, lastname,):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, monto, descrip):
        self.incomes.append((monto, descrip))

    def add_expense(self, monto, descrip):
        self.expenses.append((monto, descrip))

    def account_info(self):
        return{
            'Nombre': self.firstname,
            'Apellido': self.lastname,
            'Ingresos': self.incomes,
            'Gastos': self.expenses
        }

    def total_incomes(self):
        return sum([inc[0] for inc in self.incomes])

    def total_expenses(self):
        return sum([exp[0] for exp in self.expenses])

    def account_balance(self):
        return self.total_incomes() - self.total_expenses()

p1 = PersonAccount('Sofi','D.')
p1.add_income(1000,'Sueldo')
p1.add_income(500,'Inversión')
p1.add_expense(200,'Comida')
p1.add_expense(300,'Alquiler')
print('Account Info: ', p1.account_info())
print('Total incomes: ', p1.total_incomes())
print('Total expenses: ', p1.total_expenses())
print('Account Balance: ', p1.account_balance())

p1.add_income(500,'Ventas')
p1.add_expense(50,'Helado')
print('--- después de agregar más gastos e ingresos ---')
print('Total incomes: ', p1.total_incomes())
print('Total expenses: ', p1.total_expenses())
print('Account Balance: ', p1.account_balance())
        