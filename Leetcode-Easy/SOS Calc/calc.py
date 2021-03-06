class SOS_Calc:
    def __init__(self):
        self.min1 = [9284]
        self.min5 = [16086, 7136]
        self.hour1 = [2393, 1659]
        self.hour3 = [223]
        self.hour8 = [98]
        
        self.total = 0
        
        self.power = 134
        self.time_to_train = 36 # in seconds (was 34. idk why it went up after upgrading training camps)
        self.patriot = True
        self.state_buff = True
        self.points_in_event = 75 # 75 in SvS
        
        # 5/23 - 357,400 minutes total | 1,701,904 total troops | 228,055,238 possible power
        # 5/27 - 362,886 minutes total | 1,728,028 total troops | 231,555,828 possible power
        # 6/02 - 372,510 minutes total | 1,773,857 total troops | 237,696,857 possible power
        # 6/02 - 381,429 minutes total | 1,816,328 total troops | 243,388,028 possible power | 136,224,642 possible points in event
        # 6/21 - 407,642 minutes total | 1,941,152 total troops | 260,114,419 possible power | 145,586,428 possible points in event
        # 6/27 - 423,621 minutes total | 2,017,242 total troops | 270,310,542 possible power | 151,293,214 possible points in event
        # 6/30 - 429,121 minutes total | 2,043,433 total troops | 273,820,066 possible power | 153,257,500 possible points in event
        # 7/4 (After Crates) 455,694 minutes total | 2,169,971 total troops | 290,776,171 possible power | 162,747,857 possible points in event
        
    def run_calc(self):
        self.sum(self.min1)
        self.sum(self.min5)
        self.sum(self.hour1)
        self.sum(self.hour3)
        self.sum(self.hour8)
        
        numbers1 = "{:,}".format(self.total)
        print(f'{numbers1} minutes total')
        
        if not self.patriot and not self.state_buff:
            temp_train = self.time_to_train
        elif self.patriot and self.state_buff:
            temp_train = (self.time_to_train * .5) * .7
        elif self.patriot:
            temp_train = self.time_to_train * .5
        elif self.state_buff:
            temp_train = self.time_to_train * .7
            
        temp = (self.total * 60)/temp_train
        temp1 = "{:,}".format(int(temp))
        power_total = temp * 134
        numbers = "{:,}".format(int(power_total))
        
        print(f'{temp1} total troops')
        print(f'{numbers} possible power')
        
        total_points = temp * self.points_in_event
        temp_total_points = "{:,}".format(int(total_points))
        print(f'{temp_total_points} possible points in event')

    def sum(self, list_eval):
        if list_eval is self.min1:
            for i in list_eval:
                self.total += self.calculate(1, i)
        elif list_eval is self.min5:
            for i in list_eval:
                self.total += self.calculate(5, i)
        elif list_eval is self.hour1:
            for i in list_eval:
                self.total += self.calculate(60, i)
        elif list_eval is self.hour3:
            for i in list_eval:
                self.total += self.calculate(180, i)
        elif list_eval is self.hour8:
            for i in list_eval:
                self.total += self.calculate(480, i)
        else:
            print("Unknown list used")
                
    @staticmethod
    def calculate(multiply_by, num_to_multiply):
        total = multiply_by * num_to_multiply
        return total

calc = SOS_Calc()
calc.run_calc()
