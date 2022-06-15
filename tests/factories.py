import factory
# from factory.django import DjangoModelFactory
#
# from core.models import User
# from goals.models import GoalCategory

#
# class UserFactory(DjangoModelFactory):
#     class Meta:
#         model = User
#
#     # username = factory.Faker("test_username")
#     password = "password"
#     email = factory.Faker("email")
#     first_name = factory.Faker("first_name")
#     last_name = factory.Faker("last_name")
#     is_active = True


# class CategoryFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = GoalCategory
#
#     title = factory.Faker("title")

#
# class AdsFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Ads
#
#     name = "name_number_1"
#     author_id = factory.SubFactory(UserFactory)
#     category_id = factory.SubFactory(CategoryFactory)
#     price = 20