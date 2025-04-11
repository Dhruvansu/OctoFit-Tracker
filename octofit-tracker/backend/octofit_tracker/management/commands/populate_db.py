from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting to populate the database...')
        # Create test users
        user1 = User.objects.create(email='john.doe@example.com', name='John Doe', age=30)
        user2 = User.objects.create(email='jane.smith@example.com', name='Jane Smith', age=25)
        self.stdout.write('Test users created.')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha', members=[user1.id, user2.id])
        self.stdout.write('Test teams created.')

        # Create test activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30)
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45)
        self.stdout.write('Test activities created.')

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)
        self.stdout.write('Test leaderboard entries created.')

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
