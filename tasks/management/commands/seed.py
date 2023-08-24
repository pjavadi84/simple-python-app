from django.core.management.base import BaseCommand
from tasks.models import Task  # Adjust the import according to your model's location

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        # Example: Seeding 10 tasks
        for i in range(10):
            Task.objects.create(
                title=f'Task {i}',
                description=f'Description for Task {i}',
                # Add other fields as necessary
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!'))
