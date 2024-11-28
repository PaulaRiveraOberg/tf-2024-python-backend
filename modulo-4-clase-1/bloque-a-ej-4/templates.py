# template.py
from jinja2 import Environment, FileSystemLoader

# Configurar el entorno Jinja2
TEMPLATES_DIR = "templates"
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

def render_template(template_name, context=None):
    """Renderiza un template de Jinja2 con el contexto dado."""
    try:
        # Cargar el template desde el directorio de templates
        template = env.get_template(template_name)
        # Renderizar el template con el contexto
        return template.render(context or {})
    except FileNotFoundError:
        return "Template not found"