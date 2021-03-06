import pytest
from django.contrib.sites.models import Site
from django_dynamic_fixture import G

from blog.models import Post
from users.models import User
from courses.tests.factories import CourseFactory, MaterialFactory


@pytest.fixture
def user():
    return G(User)


@pytest.fixture
def post(user):
    return G(Post, author=user, body="正文")


@pytest.fixture
def course():
    return CourseFactory(description="**教程**")


@pytest.fixture
def material():
    return MaterialFactory()


@pytest.fixture
def site():
    return Site.objects.get(name="example.com")
