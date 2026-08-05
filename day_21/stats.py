class stats:
    def __init__ (self, lst_data):
        self.data = lst_data

    def count (self):
        return len(self.data)

    def sum (self):
        result = 0
        for i in range(len(self.data)):
            result += self.data[i]
        return result

    def min (self):
        actual_min = self.data[0]
        for i in range(1, len(self.data)):
            if self.data[i] < actual_min:
                actual_min = self.data[i]
        return actual_min

    def max (self):
            actual_max = self.data[0]
            for i in range(1, len(self.data)):
                if self.data[i] > actual_max:
                    actual_max = self.data[i]
            return actual_max

    def range (self):
        return self.max() - self.min()

    def mean (self):
        return self.sum() / self.count()

    def median (self):
        data_sorted = sorted(self.data)
        if self.count() % 2 == 0:
            return (data_sorted[(self.count() // 2) + 1] + data_sorted[self.count() // 2]) / 2
        else:
            return data_sorted[self.count() // 2]

    def mode (self):
        data_set = set(self.data)
        count = 0
        for number in data_set:
            if self.data.count(number) > count:
                count = self.data.count(number)
                mode_rslt = number
        return {"mode" : mode_rslt, "count" : count}

    def var (self):
        mean = self.mean()
        var_rslt = 0
        for i in range(self.count()):
            var_rslt += (mean - self.data[i])**2
        var_rslt /= self.count()
        return var_rslt

    def std (self):
        return self.var() ** 0.5

    def freq_dist (self):
        data_set = set(self.data)
        result = []
        for number in data_set:
            result.append((self.data.count(number) / self.count() * 100, number))
        result = sorted(result, key= lambda x : x[0], reverse=True)
        return result


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = stats(ages)

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
