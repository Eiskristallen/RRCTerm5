"""
  this module contain a math class
"""


class MyMath:
    """
    this class use to do some math operation
    """

    def __init__(self, list_num):
        try:
            super().__init__()
            self.list_num = list_num
        except Exception as e:
            print('An exception occurred')

    def avg_cal(self):
        """
        this function calculate average of list of number and return the average value
        """
        try:
            aver = 0
            sum_of_num = 0
            for item in self.list_num:
                sum_of_num += item
            aver = sum_of_num/len(self.list_num)
            return aver
        except Exception as e:
            print('An exception occurred')

    def stand_diviation(self):
        """
        this function calculate and return standar diviation of list of number
        """
        try:
            result = 0
            cont_num = 0
            leng = len(self.list_num)
            for item in range(0, leng):
                cont_num += (self.list_num[item] - self.avg_cal()) ** 2
            result = (cont_num/(leng-1))**0.5
            return result
        except Exception as e:
            print('An exception occurred')

    def find_max(self):
        """
        this function returns max value of a list of number
        """
        max_val = 0
        for item in self.list_num:
            if item > max_val:
                max_val = item
        return max_val


num_list = MyMath([])
while len(num_list.list_num) < 15:
    val = input("Enter list of your value: ")
    val = val.rsplit(',')
    new_list = [int(item) for item in val]
    num_list.list_num = num_list.list_num + new_list
    print(num_list.find_max())
    print(num_list.stand_diviation())
    print(num_list.avg_cal())
