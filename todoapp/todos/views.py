from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from todos.models import Todo
from todos.permissions import UserIsOwnerTodo
from todos.serializers import TodoSerializer


class TodoListCreateAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        import pdb;pdb.set_trace()
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        import pdb;pdb.set_trace()
        serializer.save(user=self.request.user)
        
    def post(self, request, *args, **kwargs):
        import pdb;pdb.set_trace()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(
                
                status=status.HTTP_200_OK,
            )
class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = (IsAuthenticated, UserIsOwnerTodo)


