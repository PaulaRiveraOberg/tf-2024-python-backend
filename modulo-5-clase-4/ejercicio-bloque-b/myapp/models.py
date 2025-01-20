from django.db import models

# Create your models here.

class Estudiante(models.Model):
    rut_estudiante = models.CharField(max_length=10, unique=True)
    nombre_estudiante = models.CharField(max_length=100, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)

    cursos = models.ManyToManyField("Curso", through="EstudianteCurso")

    def __str__(self):
        return f"{self.rut_estudiante} - {self.nombre_estudiante}"

class Programa(models.Model):
    nombre_programa = models.CharField(max_length=100, null=False, blank=False)
    cantidad_horas = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.nombre_programa}"

class Modulo(models.Model):
    nombre_modulo = models.CharField(max_length=100, null=False, blank=False)
    cantidad_horas = models.IntegerField(null=False, blank=False)
    programa = models.ForeignKey("Programa", on_delete=models.PROTECT)

    relatores = models.ManyToManyField("Relator", through="RelatorModulo")

    def __str__(self):
        return f"{self.nombre_modulo} - {self.programa}"

class Relator(models.Model):
    rut_relator = models.CharField(max_length=10, unique=True)
    nombre_relator = models.CharField(max_length=100, null=False, blank=False)
    titulo_relator = models.CharField(max_length=100, null=True, blank=True)
    anios_experiencia = models.IntegerField(null=True, blank=True)
    valor_hora = models.IntegerField(null=True, blank=True)

    modulos = models.ManyToManyField("Modulo", through="RelatorModulo")

    def __str__(self):
        return f"{self.rut_relator} - {self.nombre_relator}"
    
class Curso(models.Model):
    codigo_curso = models.CharField(max_length=20, unique=True)
    cantidad_estudiantes = models.IntegerField(null=False, blank=False)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_termino = models.DateField(null=False, blank=False)
    
    programa = models.ForeignKey("Programa", on_delete=models.PROTECT)

class EstudianteCurso(models.Model):
    estudiante = models.ForeignKey("Estudiante", on_delete=models.CASCADE)
    curso = models.ForeignKey("Curso", on_delete=models.CASCADE)

class RelatorModulo(models.Model):
    relator = models.ForeignKey("Relator", on_delete=models.CASCADE)
    modulo = models.ForeignKey("Modulo", on_delete=models.CASCADE)
