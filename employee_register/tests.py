from django.test import TestCase
from employee_register.models import Employee, Position
class TestURL(TestCase):

    def test(self):
        
        response = self.client.get('/employee/')
        self.assertEqual(response.status_code, 200)
        
    def test_entry(self):
        emplo = Employee()
        p = Position()
        p.title='DEV'
        p.save()
        emplo.fullname = 'test'
        emplo.mobile = '123455789'
        emplo.emp_code = '123'
        emplo.position= p
        emplo.save()
        rec = Employee.objects.get(pk=emplo.id)
        self.assertEqual(rec,emplo)
        self.assertEqual(emplo.check_code, True)
        
