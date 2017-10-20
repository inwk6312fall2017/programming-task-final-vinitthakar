import weather

class myForecast():


    def __init__(self, metrocity):
        self.metrocity = metrocity
        self.weather_change = weather.Weather()

    
    def find_minm_index(in_list):
        respond = 0
        minm = 100
        for i in range(len(in_list)):
            if int(in_list[i]) < minm:
                minm = int(in_list[i])
                respond = i
            i += 1
        return respond

    
    def find_maxm_index(in_list):
        respond = 0
        maxm = 0
        for i in range(len(in_list)):
            if int(in_list[i]) > maxm:
                maxm = int(in_list[i])
                respond = i
            i += 1
        return respond

    def test(self):
        weather_change = weather.Weather()
        mylocation = self.weather_change.lookup_by_mylocation(self.metrocity)
        mycondition = mylocation.mycondition()
        print(mycondition['text'])

         
        myforecastslist = mylocation.myforecast()[:5]
        for myforecasts in myforecastslist:
            print(myforecasts['text'])
            print(myforecasts['date'])
            print(myforecasts['high'])
            print(myforecasts['low'])