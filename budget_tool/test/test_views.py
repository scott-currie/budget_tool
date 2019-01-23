from django.test import TestCase, Client
from  ..factories import UserFactory, BudgetFactory, TransactionFactory


class TestCategoryViews(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()
        self.c = Client()

    def test_denied_if_no_login(self):
        res = self.c.get('/budget', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'class="login-form container"', res.content)

    def test_view_list_when_logged_in(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        budget = BudgetFactory(user=self.user)
        res = self.c.get('/budget')

        self.assertIn(budget.name.encode(), res.content)

    def test_lists_only_owned_budgets(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        own_budget = BudgetFactory(user=self.user)
        other_category = BudgetFactory()

        res = self.c.get('/budget')

        self.assertIn(own_budget.name.encode(), res.content)
        self.assertNotIn(other_category.name.encode(), res.content)


# class TestCardViews(TestCase):
#     """
#
#     """
    # def setUp(self):
    #     self.user = UserFactory()
    #     self.user.set_password('secret')
    #     self.user.save()
    #     self.category = CategoryFactory(user=self.user)
    #     self.c = Client()
    #     self.card = CardFactory(category=self.category)
    #
    # def test_denied_if_no_login(self):
    #     res = self.c.get('/board/card/1', follow=True)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertIn(b'class="login-form container"', res.content)
    #
    # def test_view_card_when_logged_in(self):
    #     self.c.login(
    #         username=self.user.username,
    #         password='secret'
    #     )
    #
    #     res = self.c.get('/board/card/' + str(self.card.id))
    #     self.assertIn(self.card.title.encode(), res.content)
    #     self.assertIn(self.card.description.encode(), res.content)







