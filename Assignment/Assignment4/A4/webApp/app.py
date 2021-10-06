from flask import Flask, render_template, request

app = Flask(__name__)


class MyMath:
    """
    this class use to do some math operation
    """

    def __init__(self, list_num):
        super().__init__()
        self.list_num = list_num

    def avg_cal(self):
        """
        this function calculate average of list of number and return the average value
        """
        aver = 0
        sum_of_num = 0
        for item in self.list_num:
            sum_of_num += item
        aver = sum_of_num/len(self.list_num)
        return aver

    def stand_diviation(self):
        """
        this function calculate and return standar diviation of list of number
        """
        result = 0
        cont_num = 0
        leng = len(self.list_num)
        for item in range(0, leng):
            cont_num += (self.list_num[item] - self.avg_cal()) ** 2
        result = (cont_num/(leng-1))**0.5
        return result

    def find_max(self):
        """
        this function returns max value of a list of number
        """
        max_val = 0
        for item in self.list_num:
            if item > max_val:
                max_val = item
        return max_val


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=["POST"])
def calculated():
    val = request.form["nums"].rsplit(',')
    new_list = [int(item) for item in val]
    num_list = MyMath(new_list)
    max_val = num_list.find_max()
    avg_val = num_list.avg_cal()
    std_val = num_list.stand_diviation()
    return render_template('index.html', max_val=max_val, avg_val=avg_val, std_val=std_val)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
