import locust
import random
import time

class User(locust.HttpUser):
    host = "http://localhost:8000"

    @locust.task
    def get_cursos(self):
        # visita 10 veces la página de cursos
        for i in range(1, 10):
            self.client.get(f"/cursos/?page={i}")
            # espera 1 segundo
            time.sleep(1)
        
        # visita 10 veces la página de detalle del curso
        for i in range(1, 10):
            curso_id = f"{random.randint(1, 100):04d}"
            self.client.get(f"/cursos/CUR-{curso_id}/")
            # espera entre 1 y 5 segundos
            time.sleep(random.randint(1, 5))
