import graphene
from graphene_django import DjangoObjectType
from todo.models import Todo, Project
from django.contrib.auth.models import User


"""
    GraphQL     
    Graphene-Python
    Graphene-Django 
    Mutation
"""

"""
{
  allTodo {
    id
    task
    status
    deadline
    user {
      id
      username
      isSuperuser,
      isStaff
    }
  }
}
"""


"""
{
  allUsers {
    id
    username
  }
  userAgain:allUsers {
    id
    username
  }
}
"""

""" 
{
  allProjects {
    name
    todoSet {
      id
    }
  }
}
"""


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "is_superuser",
            "is_staff",
        )


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = "__all__"


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = "__all__"


class Query(graphene.ObjectType):
    all_todo = graphene.List(TodoType)
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))
    user_by_username = graphene.List(UserType, name=graphene.String(required=True))
    project_by_name = graphene.List(ProjectType, name=graphene.String(required=True))

    def resolve_all_todo(root, info):
        return Todo.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    """
    {
        userById(id: 1) {
            id
            username
        }
    }
    """

    def resolve_user_by_id(self, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    """
    {
        allUsers {
            id
            username
        }
    }
    """

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_user_by_username(self, info, name=None):
        users = User.objects.all()
        if name:
            users = users.filter(username__contains=name)
        return users

    """
    {
	    projectByName(name:"Poro") {
            id
            name
        }
    }
    """

    def resolve_project_by_name(self, info, name=None):
        project = Project.objects.all()
        if name:
            project = project.filter(name__contains=name)
        return project


"""
mutation updateTodo {
  updateTodo(task: "New task GraphQL", id: 1) {
    todo {
      id
      task
      project {
        id
        name
      }
      user {
        username
      }
    }
  }
}
"""


class TodoMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        task = graphene.String()

    todo = graphene.Field(TodoType)

    @classmethod
    def mutate(cls, root, info, task, id):
        todo = Todo.objects.get(pk=id)
        todo.task = task
        todo.save()
        return TodoMutation(todo=todo)


class Mutation(graphene.ObjectType):
    update_todo = TodoMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
