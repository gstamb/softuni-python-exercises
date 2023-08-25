from django.test import TestCase, Client
from django.urls import reverse

from django101.testing.models import Profile


class PersonViewsTests(TestCase):
    def setUp(self) -> None:
        self.test_client = Client()

    def test_getIndex_whenNoProfiles_shouldRenderEmpty(self):
        response = self.test_client.get(reverse('profiles'))
        self.assertTemplateUsed(response, 'testing/index.html')
        profiles = response.context['profiles']
        self.assertEqual(0, len(profiles))
        form = response.context['form']
        self.assertIsNotNone(form)

    def test_getIndex_whenTw0Profiles_shouldRenderTemplateWithProfiles(self):
        profiles = (
            Profile(name='d', age=1, egn='1234567890'),
            Profile(name='e', age=1, egn='0234567890')

        )
        [profile.save() for profile in profiles]
        response = self.test_client.get(reverse('profiles'))
        self.assertTemplateUsed(response, 'testing/index.html')
        profiles = response.context['profiles']
        self.assertEqual(2, len(profiles))
        form = response.context['form']
        self.assertIsNotNone(form)

    def test_postIndex_whenValidEgn_shouldRedirectToIndex(self):
        egn = '1234567890'
        name = "Pesho"
        age = 19
        data = {'name': name,
                'age': age,
                'egn': egn}

        response = self.test_client.post(reverse('profiles'), data=data)
        self.assertRedirects(response, reverse('profiles'))

    def test_postIndex_EgnContainsLetter_renderIndexWithErrors(self):
        egn = '1234567a90'
        name = "Pesho"
        age = 19
        data = {'name': name,
                'age': age,
                'egn': egn}

        response = self.test_client.post(reverse('profiles'), data=data)

        self.assertTemplateUsed(response, 'testing/index.html')
        profiles = response.context['profiles']
        self.assertEqual(0, len(profiles))

        form = response.context['form']
        self.assertIsNotNone(form.errors['egn'])
