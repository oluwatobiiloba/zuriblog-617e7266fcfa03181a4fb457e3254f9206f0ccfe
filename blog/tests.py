from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.post = Post.objects.create(
            title ='A good title',
            body = 'Nice body content',
            author = self.user,
        )

    def test_string_representation(self):
        post = Post(title = 'A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}',
                        'A good title')
        self.assertEqual(f'{self.post.author}',
                        'testuser')
        self.assertEqual(f'{self.post.body}',
                        'Nice body content')


 

   
    
    def test_post_update_view(self): 
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)
    
    def test_post_delete_view(self):  
        response = self.client.post(
            reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)


class SignupPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'

    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
        self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                        [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                        [0].email, self.email)
