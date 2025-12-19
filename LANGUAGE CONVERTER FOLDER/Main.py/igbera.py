igbera_dict = {'come':'ve', 'take':'si', 'see':'le', 'go':'re', 'eat':'ri','house':'uyi', 'sleep':'hi', 'walk':'ino', 'work':'iteche', 'play':'ise', 'ask': 'vi', 'food':'eje', 'water':'ani',  'eyes':'anyi', 'make':'che', 'name':'eve', 'like':'ye', 'good':'dede'}
print('welcome to ur igbera_dict')
word= input('pick a word').lower()
if word in igbera_dict:
    print(igbera_dict[word])
else:print('please pick from the available words')
