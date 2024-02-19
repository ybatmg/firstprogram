from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request,'index.html')

def random_num():
    return random.randint(1,1000)

def blog(request):

    data=[{
    'image_url': f'https://loremflickr.com/320/240?random={random_num()}',
    'created_date': '06 July 2016',
    'title': 'Finding Best Places to Visit in California',
    'views': 62,
    'likes': 90,
    'comment': 41},
    {'image_url': f'https://loremflickr.com/320/240?random={random_num()}',
    'created_date': '22 January 2017',
    'title': 'Exploring the Hidden Gems of New York City',
    'views': 121,
    'likes': 46,
    'comment': 96},
    {'image_url': f'https://loremflickr.com/320/240?random={random_num()}',
    'created_date': '10 August 2017',
    'title': 'A Guide to the Most Beautiful Beaches in Hawaii',
    'views': 352,
    'likes': 128,
    'comment': 14},
    {'image_url': f'https://loremflickr.com/320/240?random={random_num()}',
    'created_date': '26 February 2018',
    'title': 'Discovering the Ancient Ruins of Greece',
    'views': 97,
    'likes': 75,
    'comment': 39},
    {'image_url': f'https://loremflickr.com/320/240?random={random_num()}',
    'created_date': '14 September 2018',
    'title': 'The Ultimate Foodie Tour of Italy',
    'views': 358,
    'likes': 26,
    'comment': 81},
    {'image_url': f'https://loremflickr.com/320/240?random={random_num()}',
    'created_date': '02 April 2019',
    'title': 'Adventure Awaits: Hiking the Rockies',
    'views': 416,
    'likes': 186,
    'comment': 99},
    {'image_url': f'https://loremflickr.com/320/240?random={random_num()}',
    'created_date': '19 October 2019',
    'title': "Cultural Wonders of Japan: A Traveler's Guide",
    'views': 162,
    'likes': 134,
    'comment': 85},
    {'image_url': f'https://loremflickr.com/320/240?random={random_num()}',
    'created_date': '06 May 2020',
    'title': 'Safari in Kenya: A Journey Through the Wild',
    'views': 464,
    'likes': 21,
    'comment': 30},
    {'image_url': f'https://loremflickr.com/320/240?random={random_num()}',
    'created_date': '22 November 2020',
    'title': 'The Magic of Northern Lights in Iceland',
    'views': 224,
    'likes': 91,
    'comment': 29},
    {'image_url': f'https://loremflickr.com/320/240?random={random_num()}',
    'created_date': '10 June 2021',
    'title': 'Paris: A Love Affair with the City of Lights',
    'views': 440,
    'likes': 106,
    'comment': 23
    }]
    return render(request,'indexblogs.html',{'data':data})

def blogdetail(request,blog_id):
    pass

def login(request):
    return render(request,'login.html')
