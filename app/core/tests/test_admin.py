from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@londonappdev.com",
            password="password123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@londonappdev.com",
            password="password123",
            name="Test user full name"
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        #this will generate the url for our user page
        #we use reverse so that if we change our
        #url we can still use this name to refer to the
        #url
        res = self.client.get(url)
        #perform a http get
        #this client checks the content of the output
        #and make assertion that the page contains these
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        #/admin/core/user/
        res = self.client.get(url)

        self.assertEqual(res.status_code,200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        """core_user_add is for adding new user"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
