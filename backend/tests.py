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
        self.headers = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNRVVoxWmh5MlE1bmNYemdXOTBnNCJ9.eyJpc3MiOiJodHRwczovL3Byb21wdGx5MC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTY0MDc3ODAwMDE3NTA0MTQzNzQiLCJhdWQiOiJwcm9tcHRzIiwiaWF0IjoxNjkxNTcxMDc0LCJleHAiOjE2OTE2NTc0NzQsImF6cCI6IlhzQU5QV3VRVUNRRTZJbFR5UHR4cFZOZGNjblBFRXk5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6cHJvbXB0IiwiZGVsZXRlOnByb21wdCIsInVwZGF0ZTpwcm9tcHQiXX0.1E4PRzTwWGGYEusEP5sLMaTXHgq0_EPGHdPn5D5HeVtZp0Decr3FqtT5RKzkdLqiyHGYFCchWgS2d9AG5yKfZ7cAJtE-Xlyie4cuS1aueIFTPgha2BIt3LcMKTplBj8qA8bVFhzFJ9_CpQKhT9jO3iLTnx1q1ZpjK1rKQaCV-uRVg9xnyCaaJsmdVDI8dQPt16vTfMwkpCzhKv5ZCmj_c0_CtLoANOBpZOL6YFZe1LFuXOlk2f0UEEtVa8CE3E6NlDU-cJwZCKSdiA0yV-HXjf2se7wF1KzrMvoiAtIx70vWd9J-gVJz9_ZVzwp1T3DUiHxpY6yI3DnlGPMSab2ZNA',
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
        }, headers=self.headers)
        

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_prompt_by_id(self):
        res = self.client().get('/prompts/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_delete_prompt_by_id(self):
        res = self.client().delete('/prompts/15', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_update_prompt_by_id(self):
        res = self.client().patch('/prompts/14', json={
            'title': 'Updated Title',
            'content': 'Updated Content',
            'genre_id': 2
        }, headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_404_get_all_prompts(self):
        res = self.client().get('/prompts?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    
    def test_400_add_prompt(self):
        res = self.client().post('/prompts', json={}, headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    def test_404_get_prompt_by_id(self):
        res = self.client().get('/prompts/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_404_delete_prompt_by_id(self):
        res = self.client().delete('/prompts/1000', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_400_update_prompt_by_id(self):
        res = self.client().patch('/prompts/18', json={}, headers=self.headers)
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
        }, headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_genre_by_id(self):
        res = self.client().get('/genres/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_delete_genre_by_id(self):
        res = self.client().delete('/genres/6', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_update_genre_by_id(self):
        res = self.client().patch('/genres/4', json={
            'name': 'Updated Name',
            'description': 'Updated Description'
        }, headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_404_get_all_prompts(self):
        res = self.client().get('/genres?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_422_add_genre(self):
        res = self.client().post('/genres', json={}, headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    def test_404_get_genre_by_id(self):
        res = self.client().get('/genres/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_404_delete_genre_by_id(self):
        res = self.client().delete('/genres/1000', headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_400_update_genre_by_id(self):
        res = self.client().patch('/genres/7', json={}, headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])




if __name__ == "__main__":
    unittest.main()