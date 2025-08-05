import unittest
import actF as device_manager


class TestDeviceManager(unittest.TestCase):

    def test_add_device(self):
        device = {"title": "Switch-01", "body": "Network Switch", "userId": 1}
        response = device_manager.add_device(device)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json())

    def test_list_devices(self):
        response = device_manager.list_devices()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_update_device(self):
        updated_device = {"title": "Switch-01-Upgraded", "body": "Core Switch", "userId": 1}
        response = device_manager.update_device(1, updated_device)
        self.assertEqual(response.status_code, 200)
        self.assertIn('json', response.json())

    def test_delete_device(self):
        response = device_manager.delete_device(1)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
