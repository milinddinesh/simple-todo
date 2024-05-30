from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def createUser(request):
    username = request['username']
    email = request['email']
    password = request['password']

    user = User.objects.create_user(username, email , password)
    user.save()

# def login(reqeust):
#     user = authenticate(username="john", password="secret")
    
# # 