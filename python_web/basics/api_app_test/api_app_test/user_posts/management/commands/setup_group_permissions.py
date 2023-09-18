from io import StringIO
import logging

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    # Usage create a new group by running
    # `python manage.py setup_group_permissions --groups user_add_delete_trip --models trip --permissions add delete`
    # or 
    #  `python manage.py setup_group_permissions --groups user_view_change_trip --models trip --permissions view change`

    help = 'Creates read-only default permission groups for users'

    def add_arguments(self, parser):
        parser.add_argument('--groups', nargs='+', type=str,
                            help='List of group names')
        parser.add_argument('--models', nargs='+', type=str,
                            help='List of model names')
        parser.add_argument('--permissions', nargs='+',
                            type=str, help='List of permission types')

    def handle(self, *args, **options):
        groups = options['groups']
        models = options['models']
        permissions = options['permissions']

        for group_name in groups:
            new_group, created = Group.objects.get_or_create(name=group_name)
            for model in models:
                for permission in permissions:
                    name = f'Can {permission} {model}'
                    print(f'Creating {name}')

                    try:
                        model_add_perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        logging.warning(
                            f"Permission not found with name '{name}'.")
                        continue

                    new_group.permissions.add(model_add_perm)

        print('Created default groups and permissions.')
