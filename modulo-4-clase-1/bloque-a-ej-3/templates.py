import os

# Directorio donde se almacenan los archivos de plantillas
TEMPLATES_DIR = "templates"

def render_template(template_name):
    """
    Carga y devuelve el contenido de un archivo de plantilla.
    
    Esta función busca un archivo de plantilla en el directorio de templates
    y retorna su contenido como una cadena de texto.

    Args:
        template_name (str): Nombre del archivo de plantilla a cargar

    Returns:
        str: Contenido del archivo de plantilla si existe,
             "Template not found" si el archivo no se encuentra

    Raises:
        FileNotFoundError: Si el archivo de plantilla no existe en el directorio
    """
    try:
        with open(os.path.join(TEMPLATES_DIR, template_name), "r") as template_file:
            return template_file.read()
    except FileNotFoundError:
        return "Template not found"