def test_index(self):
	"""Ensure flask was set up correctly."""
	response = self.app.get('/', content_type='html/text')
	self.assertEqual(response.status_code, 200)