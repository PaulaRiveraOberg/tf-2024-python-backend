from django.db import models

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    codigo_curso = models.CharField(unique=True)
    cantidad_estudiantes = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    id_programa = models.ForeignKey('Programa', models.DO_NOTHING, db_column='id_programa')
    estudiantes = models.ManyToManyField('Estudiante', through='CursoEstudiante')

    def __str__(self):
        return f"{self.codigo_curso} - {self.id_programa}"


class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    rut_estudiante = models.CharField(unique=True, blank=True, null=True)
    nombre_estudiante = models.CharField()
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(blank=True, null=True)
    correo = models.CharField(blank=True, null=True)
    telefono = models.CharField(blank=True, null=True)

    def __str__(self):
        return f"{self.rut_estudiante} - {self.nombre_estudiante}"


class Relator(models.Model):
    id_relator = models.AutoField(primary_key=True)
    rut_relator = models.CharField(unique=True, blank=True, null=True)
    nombre_relator = models.CharField()
    titulo_relator = models.CharField(blank=True, null=True)
    anios_experiencia = models.IntegerField(blank=True, null=True)
    valor_hora = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.rut_relator} - {self.nombre_relator}"

class Modulo(models.Model):
    id_modulo = models.AutoField(primary_key=True)
    nombre_modulo = models.CharField()
    cantidad_horas = models.IntegerField()
    id_programa = models.ForeignKey('Programa', models.DO_NOTHING, db_column='id_programa')
    relatores = models.ManyToManyField(Relator, through='ModuloRelator')

    def __str__(self):
        return f"{self.nombre_modulo} - {self.id_programa}"

class Programa(models.Model):
    id_programa = models.AutoField(primary_key=True)
    nombre_programa = models.CharField()
    cantidad_horas = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_programa}"

class CursoEstudiante(models.Model):
    id_estudiante = models.ForeignKey('Estudiante', models.DO_NOTHING, db_column='id_estudiante')
    id_curso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='id_curso')

class ModuloRelator(models.Model):
    id_modulo = models.ForeignKey('Modulo', models.DO_NOTHING, db_column='id_modulo')
    id_relator = models.ForeignKey('Relator', models.DO_NOTHING, db_column='id_relator')
