import csv
import os
from datetime import datetime

from django.db import migrations


def load_initial_data(apps, schema_editor):
    # Obtener los modelos
    Autor = apps.get_model("myapp", "Autor")
    Editorial = apps.get_model("myapp", "Editorial")
    Categoria = apps.get_model("myapp", "Categoria")
    Libro = apps.get_model("myapp", "Libro")

    # Función auxiliar para cargar datos desde CSV
    def load_csv(model, filename, date_fields=None):
        file_path = os.path.join(os.path.dirname(__file__), "../..", "data", filename)
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if date_fields:
                    for field in date_fields:
                        if row[field]:
                            row[field] = datetime.strptime(
                                row[field], "%Y-%m-%d"
                            ).date()
                print(row)
                model.objects.create(**row)

    # Cargar datos
    load_csv(Autor, "autores.csv", ["fecha_nacimiento"])
    load_csv(Editorial, "editoriales.csv")
    load_csv(Categoria, "categorias.csv")
    load_csv(Libro, "libros.csv", ["fecha_publicacion"])

    # Cargar relaciones muchos a muchos
    def load_m2m_csv(model, filename, field1, field2, related_field):
        file_path = os.path.join(os.path.dirname(__file__), "../..", "data", filename)
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                instance = model.objects.get(id=row[field1])
                related_model = getattr(instance, related_field).model
                related_instance = related_model.objects.get(id=row[field2])
                getattr(instance, related_field).add(related_instance)

    load_m2m_csv(Libro, "libros_autores.csv", "libro_id", "autor_id", "autores")
    load_m2m_csv(
        Libro, "libros_categorias.csv", "libro_id", "categoria_id", "categorias"
    )


def reverse_load_initial_data(apps, schema_editor):
    # Eliminar todos los datos
    Autor = apps.get_model("myapp", "Autor")
    Editorial = apps.get_model("myapp", "Editorial")
    Categoria = apps.get_model("myapp", "Categoria")
    Libro = apps.get_model("myapp", "Libro")

    Libro.objects.all().delete()
    Autor.objects.all().delete()
    Editorial.objects.all().delete()
    Categoria.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(load_initial_data, reverse_load_initial_data),
    ]
