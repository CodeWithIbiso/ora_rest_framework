from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from datetime import datetime

from .serializers import GroupSerializer, UserSerializer, CommentSerializer
# from ora_api.quickstart.serializers import GroupSerializer, UserSerializer

# Rather than write multiple views we're grouping together all the common behavior into classes called ViewSets.
# We can easily break these down into individual views if we need to, but using viewsets keeps the view logic nicely organized as well as being very concise.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

class GroupViewSet(viewsets.ModelViewSet):
    comment = Comment(email='leila@example.com', content='foo bar')
    print('comment ',comment)
    print('serialized comment ', CommentSerializer(comment))
    print('serialized comment data', CommentSerializer(comment).data)
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



