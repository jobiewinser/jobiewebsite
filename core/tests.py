from django.test import TestCase
from django.contrib import admin, auth
from core.models import Technology, TechnologyType, Language, ProjectImage, Project
from django.core.files.base import File
class TechnologyTypeTestCase(TestCase):
    def setUp(self):
        TechnologyType.objects.create(name='Payment Option')
        TechnologyType.objects.create(name='Web Framework')

    def test_technology_types_are_created(self):
        """TechnologyTypes are created successfully"""
        techtype1 = TechnologyType.objects.get(name='Payment Option')
        techtype2 = TechnologyType.objects.get(name='Web Framework')

        self.assertEqual(techtype1.__str__(), 'Payment Option')
        self.assertEqual(techtype2.__str__(), 'Web Framework')

class LanguageTestCase(TestCase):
    def setUp(self):
        Language.objects.create(name='Javascript')
        Language.objects.create(name='Python')

    def test_languages_are_created(self):
        """Languages are created successfully"""
        language1 = Language.objects.get(name='Javascript')
        language2 = Language.objects.get(name='Python')

        self.assertEqual(language1.__str__(), 'Javascript')
        self.assertEqual(language2.__str__(), 'Python')

class TechnologyTestCase(TestCase):
    def setUp(self):
        TechnologyType.objects.create(name='Payment Option')
        TechnologyType.objects.create(name='Web Framework')
        Language.objects.create(name='Javascript')
        Language.objects.create(name='Python')

        techtype = TechnologyType.objects.get(name='Web Framework')
        language = Language.objects.get(name='Python')


        technology1 = Technology.objects.create(
                                    name='DjangoTest1', 
                                    priority=1, 
                                    image='testing/testimage.jpg',
                                    htmldescription='<p>Test</p>')
        technology1.type.add(techtype)
        technology1.language.add(language)
        technology1.save()

        technology2 = Technology.objects.create(
                                    name='DjangoTest2', 
                                    priority=1, 
                                    image='testing/testimage.jpg')
        technology2.type.add(techtype)
        technology2.language.add(language)
        technology2.save()

        technology3 = Technology.objects.create(
                                    name='DjangoTest3', 
                                    priority=1, )
        technology3.type.add(techtype)
        technology3.language.add(language)
        technology3.save()

        technology4 = Technology.objects.create(
                                    name='DjangoTest4')
        technology4.type.add(techtype)
        technology4.language.add(language)
        technology4.save()

        technology5 = Technology.objects.create(
                                    name='DjangoTest5')
        technology5.type.add(techtype)
        technology5.save()

        technology6 = Technology.objects.create(
                                    name='DjangoTest6')

    def test_technologys_are_created(self):
        """Technologies are created successfully"""
        self.assertEqual(Technology.objects.all().count(), 6)

        fulltechnology = Technology.objects.get(htmldescription='<p>Test</p>')
        self.assertEqual(fulltechnology.name, 'DjangoTest1')
        self.assertEqual(fulltechnology.priority, 1)
        self.assertEqual(type(fulltechnology.image.file), File)
        self.assertEqual(fulltechnology.htmldescription, '<p>Test</p>')
