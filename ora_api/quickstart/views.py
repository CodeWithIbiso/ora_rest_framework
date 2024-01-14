from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .serializers import GroupSerializer, UserSerializer
# from ora_api.quickstart.serializers import GroupSerializer, UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Rather than write multiple views we're grouping together all the common behavior into classes called ViewSets.
# We can easily break these down into individual views if we need to, but using viewsets keeps the view logic nicely organized as well as being very concise.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] # Adding this line will enforce authentication

 

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



@api_view(['GET', 'POST'])
def test(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})



