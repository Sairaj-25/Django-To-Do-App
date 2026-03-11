from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from .models import Task


class TaskModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword123"
        )

        # Create a test task
        self.task = Task.objects.create(
            title="Finish CI/CD pipeline",
            description="Write GitHub Actions YAML file",
            due_date="2026-12-31",
            create_time=now(),
            user=self.user,
        )

    def test_task_creation(self):
        """Test that a task is correctly created and linked to the user."""
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(self.task.title, "Finish CI/CD pipeline")
        self.assertEqual(self.task.user.username, "testuser")

    def test_task_string_representation(self):
        """Test the __str__ method of the Task model."""
        self.assertEqual(str(self.task), "Finish CI/CD pipeline")


class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")

        # Pre-create a user for login tests
        self.user = User.objects.create_user(
            username="existinguser", email="exist@example.com", password="password123"
        )

    def test_user_registration_success(self):
        """Test successful user registration."""
        response = self.client.post(
            self.register_url,
            {
                "uname": "newuser",
                "uemail": "new@example.com",
                "upass1": "securepass123",
                "upass2": "securepass123",
            },
        )
        # Should redirect to home upon successful registration and login
        self.assertRedirects(response, reverse("home"))
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_user_registration_password_mismatch(self):
        """Test registration fails if passwords do not match."""
        response = self.client.post(
            self.register_url,
            {
                "uname": "newuser",
                "uemail": "new@example.com",
                "upass1": "securepass123",
                "upass2": "differentpass",
            },
        )
        self.assertEqual(response.status_code, 200)  # Re-renders form
        self.assertFalse(User.objects.filter(username="newuser").exists())
        self.assertContains(response, "Passwords are not macthing!")

    def test_user_login_success(self):
        """Test successful login with valid credentials."""
        # Using email as identifier since your view supports it
        response = self.client.post(
            self.login_url, {"uemail": "exist@example.com", "upass": "password123"}
        )
        self.assertRedirects(response, reverse("home"))

    def test_user_login_failure(self):
        """Test login fails with incorrect password."""
        response = self.client.post(
            self.login_url, {"uemail": "exist@example.com", "upass": "wrongpassword"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid username or password")

    def test_user_logout(self):
        """Test user logout functionality."""
        self.client.login(username="existinguser", password="password123")
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, reverse("home"))


class TaskViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="taskuser", email="task@example.com", password="password123"
        )

        # Create initial task
        self.task = Task.objects.create(
            title="Initial Task",
            description="Just a test",
            due_date="2026-01-01",
            create_time=now(),
            user=self.user,
        )

    def test_home_view_unauthenticated(self):
        """Test that unauthenticated users are redirected to login when accessing home."""
        response = self.client.get(reverse("home"))
        self.assertRedirects(response, reverse("login"))

    def test_home_view_authenticated(self):
        """Test that authenticated users can see their tasks on the home page."""
        self.client.login(username="taskuser", password="password123")
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Initial Task")

    def test_add_task_view(self):
        """Test adding a new task via POST request."""
        self.client.login(username="taskuser", password="password123")
        response = self.client.post(
            reverse("add_task"),
            {
                "title": "New POST Task",
                "description": "Created via test client",
                "due_date": "2026-10-10",
            },
        )
        self.assertRedirects(response, reverse("home"))
        self.assertEqual(Task.objects.count(), 2)
        self.assertTrue(Task.objects.filter(title="New POST Task").exists())

    def test_remove_task_view(self):
        """Test removing an existing task."""
        self.client.login(username="taskuser", password="password123")
        # Call the remove_task URL with the task's primary key
        response = self.client.get(reverse("remove_task", args=[self.task.pk]))
        self.assertRedirects(response, reverse("home"))
        self.assertEqual(Task.objects.count(), 0)

    def test_search_task_view(self):
        """Test searching for tasks by title."""
        self.client.login(username="taskuser", password="password123")
        # Add a second task to test filtering
        Task.objects.create(
            title="Learn Django Testing",
            description="Write some tests",
            due_date="2026-02-02",
            create_time=now(),
            user=self.user,
        )

        # Search for 'Django'
        response = self.client.get(reverse("search_task"), {"query": "Django"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Learn Django Testing")
        self.assertNotContains(
            response, "Initial Task"
        )  # Ensure the other task is filtered out
