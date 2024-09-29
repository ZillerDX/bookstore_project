# store/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Category
from .forms import BookForm, UserRegisterForm

# การทดสอบโมเดล (Model Tests)
class BookModelTest(TestCase):

    def setUp(self):
        # สร้าง Category สำหรับทดสอบ
        self.category = Category.objects.create(name="Fiction")
        # สร้าง Book สำหรับทดสอบ
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="This is a test description",
            price=99.99,
            category=self.category,
            stock=10
        )

    def test_book_creation(self):
        # ตรวจสอบการสร้าง Book
        self.assertTrue(isinstance(self.book, Book))
        self.assertEqual(self.book.__str__(), self.book.title)

    def test_category_creation(self):
        # ตรวจสอบการสร้าง Category
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.__str__(), self.category.name)

# การทดสอบฟอร์ม (Form Tests)
class BookFormTest(TestCase):

    def test_book_form_valid_data(self):
        # ทดสอบฟอร์มการสร้างหนังสือด้วยข้อมูลที่ถูกต้อง
        form = BookForm(data={
            'title': 'Test Book',
            'author': 'Test Author',
            'description': 'This is a test description',
            'price': 99.99,
            'category': Category.objects.create(name="Fiction").id,
            'stock': 10
        })
        self.assertTrue(form.is_valid())

    def test_book_form_invalid_data(self):
        # ทดสอบฟอร์มการสร้างหนังสือด้วยข้อมูลที่ไม่ครบถ้วน
        form = BookForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)  # มีฟิลด์ทั้งหมด 7 ฟิลด์ในฟอร์ม BookForm

# การทดสอบมุมมอง (View Tests)
class BookViewsTest(TestCase):

    def setUp(self):
        # สร้างผู้ใช้สำหรับการทดสอบการเข้าสู่ระบบ
        self.user = User.objects.create_user(username='testuser', password='12345')
        # สร้าง Category และ Book สำหรับทดสอบ
        self.category = Category.objects.create(name="Fiction")
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="This is a test description",
            price=99.99,
            category=self.category,
            stock=10
        )
        # ใช้ Client จำลองการเรียกใช้งาน HTTP Request
        self.client = Client()

    def test_book_list_view(self):
        # ทดสอบหน้าแสดงรายการหนังสือ
        response = self.client.get(reverse('store:book_list'))  # ใช้ 'store:book_list'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/book_list.html')

    def test_book_create_view(self):
        # ทดสอบหน้าเพิ่มหนังสือ ต้องล็อกอินก่อนถึงจะเพิ่มได้
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('store:book_create'), {
            'title': 'New Book',
            'author': 'New Author',
            'description': 'This is a new book',
            'price': 199.99,
            'category': self.category.id,
            'stock': 5
        })
        self.assertEqual(response.status_code, 302)  # Redirect หลังจากเพิ่มหนังสือสำเร็จ
        self.assertEqual(Book.objects.count(), 2)  # หนังสือควรมีทั้งหมด 2 เล่มในฐานข้อมูล

    def test_book_update_view(self):
        # ทดสอบหน้าแก้ไขหนังสือ ต้องล็อกอินก่อนถึงจะแก้ไขได้
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('store:book_update', args=[self.book.id]), {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'description': 'Updated Description',
            'price': 150.00,
            'category': self.category.id,
            'stock': 8
        })
        self.book.refresh_from_db()  # โหลดข้อมูลใหม่จากฐานข้อมูล
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.book.title, 'Updated Book')

    def test_book_delete_view(self):
        # ทดสอบการลบหนังสือ ต้องล็อกอินก่อนถึงจะลบได้
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('store:book_delete', args=[self.book.id]))  # ใช้ 'store:book_delete'
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.count(), 0)  # ควรลบหนังสือจนเหลือ 0 เล่มในระบบ

    def test_user_registration_view(self):
        # ทดสอบการสมัครสมาชิก
        response = self.client.post(reverse('store:register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect หลังจากสมัครสมาชิกสำเร็จ
        self.assertEqual(User.objects.count(), 2)  # ควรมีผู้ใช้ทั้งหมด 2 คน (รวม testuser)

    def test_user_login_view(self):
        # ทดสอบการเข้าสู่ระบบ
        response = self.client.post(reverse('store:login'), {
            'username': 'testuser',
            'password': '12345'
        })
        self.assertEqual(response.status_code, 302)  # Redirect หลังจากล็อกอินสำเร็จ

    def test_user_logout_view(self):
        # ทดสอบการออกจากระบบ
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('store:logout'))
        self.assertEqual(response.status_code, 302)  # Redirect หลังจากออกจากระบบสำเร็จ
