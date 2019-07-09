from django.test import TestCase
from tickets.models import Ticket, TicketComment
from registration.models import User
from accounts.models import Profile, Institute
import datetime as dt


class TicketModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='sample_test_user1',
                                        first_name='sample',
                                        last_name='user',
                                        email='sampleuser1@test.com'
                                        )

        self.institute = Institute.objects.create()

        self.profile = Profile.objects.create(user=self.user,
                                              college=self.institute,
                                              phone_number='+991234567890'
                                              )

        self.ticket = Ticket.objects.create(title='Sample Ticket1',
                                            description='Some sample description',
                                            opened_by=self.profile,
                                            )

    def test_model_creation(self):
        self.assertTrue(Ticket.objects.filter(opened_by=self.profile).exists())

    def test_default_public_ticket(self):
        self.assertTrue(self.ticket.is_public)

    def test_self_opening_date(self):
        self.assertEqual(self.ticket.opening_date, dt.date.today())


class TicketCommentModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='sample_test_user1',
                                        first_name='sample',
                                        last_name='user',
                                        email='sampleuser1@test.com'
                                        )

        self.user1 = User.objects.create(username='sample_test_user2',
                                         first_name='sample',
                                         last_name='user1',
                                         email='sampleuser2@test.com'
                                         )

        self.institute = Institute.objects.create()

        self.profile = Profile.objects.create(user=self.user,
                                              college=self.institute,
                                              phone_number='+991234567890'
                                              )

        self.profile1 = Profile.objects.create(user=self.user1,
                                               college=self.institute,
                                               phone_number='+991234567891'
                                               )

        self.ticket = Ticket.objects.create(title='Sample Ticket1',
                                            description='Some sample description',
                                            opened_by=self.profile
                                            )

        self.ticket_comment = TicketComment.objects.create(ticket=self.ticket,
                                                           commenter=self.profile1,
                                                           text='Comment Text')

    def test_model_creation(self):
        self.assertTrue(TicketComment.objects.filter(ticket=self.ticket, commenter=self.profile1).exists())

    def test_posting_date(self):
        self.assertGreaterEqual(self.ticket_comment.posting_date, dt.datetime.now(tz=self.ticket_comment.posting_date.tzinfo)
                         - dt.timedelta(0, 5, 0))

    def test_comments_for_ticket(self):
        self.assertTrue(self.ticket.comments.filter(commenter=self.profile1).exists())

