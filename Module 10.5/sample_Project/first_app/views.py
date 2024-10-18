from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    d = {'author' : 'rahim', 'age' : 20,
          'list' : ['python','is','best'], 
         'birthday' : datetime.datetime.now(), 
         'val' : '',
         'myself' : "I'm pial.",
         'courses' : [
        {
            'id' : 1,
            'name' : 'Python',
            'fee' : 5000,
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fee' : 10000,
        },
        {
            'id' : 3,
            'name' : 'C',
            'fee' : 1000,
        },
    ],
        'NAME' : [
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
        ],
    'ammount' : 22,
    'another_list' : [['one'],['two'],['three']],
    'Title' : 'my name is pial.',
    'this_date' : datetime.datetime.now(),
    'des01' : 'I love dogs'
    
    }
    # return render(request, 'home.html',context=d)
    return render(request, 'home.html', d)