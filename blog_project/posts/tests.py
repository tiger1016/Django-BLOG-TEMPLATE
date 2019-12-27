from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User

from .models import Post

class BlogTests(TestCase):

    @classmethod
    def setUpClass(cls):

        testuser1 = User.objects.create_user(
            username = 'testuser1', password = 'abc123'
        )
        testuser1.save()

        test_post = Post.objects.create(
            auth = testuser1, title = "blog title", body = "body content..."
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Body content...')