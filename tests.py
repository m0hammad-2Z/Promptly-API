import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import db
from app import app





class TriviaTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.db = db
        self.admin_headers = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNRVVoxWmh5MlE1bmNYemdXOTBnNCJ9.eyJpc3MiOiJodHRwczovL3Byb21wdGx5MC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDg1NTU3Nzk5MTM0MTE1MzcwOTAiLCJhdWQiOiJwcm9tcHRzIiwiaWF0IjoxNjkxNjU5OTg2LCJleHAiOjE2OTE3NDYzODYsImF6cCI6IlhzQU5QV3VRVUNRRTZJbFR5UHR4cFZOZGNjblBFRXk5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6Z2VucmUiLCJhZGQ6cHJvbXB0IiwiZGVsZXRlOmdlbnJlIiwiZGVsZXRlOnByb21wdCIsInVwZGF0ZTpnZW5yZSIsInVwZGF0ZTpwcm9tcHQiXX0.N-U4nYOPKKt1mfYGwGcFHMwEjJh0LnKeG1VK54IstOINsoXj52N5ksZfX0Mf-8wRiZaTWc6mYqNPpMzTVB0CQe-WFmIWpPzywnFR2UkqkoN1at1A0ueLi_mEJ8vxWYAgO-ZXjeQ9vljmbVLCx-kHYGCf3ItEloFSPx3qsZAWHzkV4yfi9Zakn00Q4sG_xWlD-pFqhG_CPvx3VkzCxMEIHfipvhJ5ovgXPJtbkmm-poWIIhMfKfScubfDsTJuqx_9klwHCfSiFHHEpFwOfeZf7vLUQQie4sTfMc31T-gSGUKFAsaha6dbVcqC3BbSwyJzxMCdYOi-SbBcZHh4xb8XhA',
            'Content-Type': 'application/json'
        }
        self.user_headers = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNRVVoxWmh5MlE1bmNYemdXOTBnNCJ9.eyJpc3MiOiJodHRwczovL3Byb21wdGx5MC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTY0MDc3ODAwMDE3NTA0MTQzNzQiLCJhdWQiOiJwcm9tcHRzIiwiaWF0IjoxNjkxNjYwMDc0LCJleHAiOjE2OTE3NDY0NzQsImF6cCI6IlhzQU5QV3VRVUNRRTZJbFR5UHR4cFZOZGNjblBFRXk5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6cHJvbXB0IiwiZGVsZXRlOnByb21wdCIsInVwZGF0ZTpwcm9tcHQiXX0.RwA_Jl7HOXjbdWXhPZAaBtJZ4rqFIitZ6-cZnuG13FsJLcV5vJsxOYM3fAAkqOy6iC7GqKPb44P44FboNq-bSXBDFsxY66-h55hM6FaTOmmwK9l87jbn4lRixRlOcp3x-3NHqHkdJMLKihIdqe1sWrhaSHdM08Y7Z62-kROBVftuxAxp1uVGgWllOJtfOGzRqcRpeAmBrABUFSWvfQIYhHFFUzhHKKFkdv0WlAtsUPiA4_qkMB8Gyel-ZZGD3NaZlOlH1Bpm1o9dMBk1YWL03JU4GzhK6sy2DNXUsloLG84ebp7vHx9nkoUo2YXOEqmv7Pw5DNVfpFsNScD--5azoA',
            'Content-Type': 'application/json'
        }
    

    def test_get_all_prompts(self):
        res = self.client().get('/prompts')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_add_prompt(self):
        res = self.client().post('/prompts', json={
            'title': 'Test Title',
            'content': 'Test Content',
            'genre_id': 1
        }, headers=self.user_headers)
        

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_prompt_by_id(self):
        res = self.client().get('/prompts/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_delete_prompt_by_id(self):
        res = self.client().delete('/prompts/16', headers=self.user_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_update_prompt_by_id(self):
        res = self.client().patch('/prompts/14', json={
            'title': 'Updated Title',
            'content': 'Updated Content',
            'genre_id': 2
        }, headers=self.user_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_404_get_all_prompts(self):
        res = self.client().get('/prompts?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    
    def test_400_add_prompt(self):
        res = self.client().post('/prompts', json={}, headers=self.user_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    def test_404_get_prompt_by_id(self):
        res = self.client().get('/prompts/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_404_delete_prompt_by_id(self):
        res = self.client().delete('/prompts/1000', headers=self.user_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_422_update_prompt_by_id(self):
        res = self.client().patch('/prompts/10', json={}, headers=self.user_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])




    def test_get_all_genres(self):
        res = self.client().get('/genres')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_add_genre(self):
        res = self.client().post('/genres', json={
            'name': 'Test Name',
            'description': 'Test Description'
        }, headers=self.admin_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_genre_by_id(self):
        res = self.client().get('/genres/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_delete_genre_by_id(self):
        res = self.client().delete('/genres/8', headers=self.admin_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_update_genre_by_id(self):
        res = self.client().patch('/genres/4', json={
            'name': 'Updated Name',
            'description': 'Updated Description'
        }, headers=self.admin_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_404_get_all_prompts(self):
        res = self.client().get('/genres?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_422_add_genre(self):
        res = self.client().post('/genres', json={}, headers=self.admin_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    def test_404_get_genre_by_id(self):
        res = self.client().get('/genres/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_404_delete_genre_by_id(self):
        res = self.client().delete('/genres/1000', headers=self.admin_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_400_update_genre_by_id(self):
        res = self.client().patch('/genres/4', json={}, headers=self.admin_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
    

    # RBAC (Error tests)
    def test_401_add_prompt(self):
        res = self.client().post('/prompts', json={
            'title': 'Test Title',
            'content': 'Test Content',
            'genre_id': 1
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_403_add_genre(self):
        res = self.client().post('/genres', json={
            'name': 'Test Name',
            'description': 'Test Description'
        }, headers=self.user_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])

    def test_401_delete_prompt(self):
        res = self.client().delete('/prompts/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_403_delete_genre(self):
        res = self.client().delete('/genres/1', headers=self.user_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])

    def test_update_401_prompt(self):
        res = self.client().patch('/prompts/14', json={
            'title': 'Updated Title',
            'content': 'Updated Content',
            'genre_id': 2
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_403_update_genre(self):
        res = self.client().patch('/genres/1', json={
            'name': 'Updated Name',
            'description': 'Updated Description'
        }, headers=self.user_headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])


if __name__ == "__main__":
    unittest.main()