from django.contrib.contenttypes.models import ContentType
from django.db import migrations


def crear_roles(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")
    roles = {
        "Editor": [
            "add_post",
            "change_post",
            "delete_post",
            "view_post",
            "add_comment",
            "delete_comment",
        ],
        "Autor": ["add_post", "change_own_post", "delete_own_post", "view_post"],
        "Lector": ["view_post", "add_comment", "delete_own_comment"],
    }
    for role, permisos in roles.items():
        group, _ = Group.objects.get_or_create(name=role)
        for permiso in permisos:
            model_name = permiso.split("_")[-1]
            content_type, _ = ContentType.objects.get_or_create(
                app_label="miapp", model=model_name
            )
            permission, _ = Permission.objects.get_or_create(
                codename=permiso, content_type_id=content_type.id
            )
            group.permissions.add(permission)


def eliminar_roles(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name__in=["Editor", "Autor", "Lector"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("miapp", "0001_initial"),
        # para que funcione el get_or_create
        ("contenttypes", "0002_remove_content_type_name"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]
    operations = [
        migrations.RunPython(crear_roles, eliminar_roles),
    ]
