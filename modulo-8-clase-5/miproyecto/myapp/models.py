from django.contrib.auth.models import User
from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name_plural = "Autores"


class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(blank=True)
    sitio_web = models.URLField(blank=True)
    correo = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Editoriales"


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorías"


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.ManyToManyField(Autor, related_name="libros")
    editorial = models.ForeignKey(
        Editorial, on_delete=models.CASCADE, related_name="libros"
    )
    categorias = models.ManyToManyField(Categoria, related_name="libros")
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    descripcion = models.TextField(blank=True)
    paginas = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to="libros/", blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Libros"


class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="resenas")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="resenas")
    puntuacion = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.usuario.username} para {self.libro.titulo}"

    class Meta:
        verbose_name_plural = "Reseñas"
        unique_together = ["libro", "usuario"]


class CarritoCompra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carritos")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

    @property
    def total(self):
        return sum(item.subtotal for item in self.items.all())


class ItemCarrito(models.Model):
    carrito = models.ForeignKey(
        CarritoCompra, on_delete=models.CASCADE, related_name="items"
    )
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} x {self.libro.titulo}"

    @property
    def subtotal(self):
        return self.libro.precio * self.cantidad


class Pedido(models.Model):
    ESTADO_CHOICES = [
        ("pendiente", "Pendiente"),
        ("procesando", "Procesando"),
        ("enviado", "Enviado"),
        ("entregado", "Entregado"),
        ("cancelado", "Cancelado"),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pedidos")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    direccion_envio = models.TextField()
    estado = models.CharField(
        max_length=20, choices=ESTADO_CHOICES, default="pendiente"
    )
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="items")
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.libro.titulo} en Pedido #{self.pedido.id}"

    @property
    def subtotal(self):
        return self.precio_unitario * self.cantidad
