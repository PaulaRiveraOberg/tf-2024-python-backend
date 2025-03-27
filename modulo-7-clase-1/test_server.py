import unittest
from unittest.mock import MagicMock, patch

import distance_unary_pb2 as pb2
import distance_unary_pb2_grpc as pb2_grpc
import grpc
from server import DistanceServicer


class TestDistanceServicer(unittest.TestCase):
    def setUp(self):
        self.servicer = DistanceServicer()
        self.context = MagicMock(spec=grpc.ServicerContext)

    def test_valid_distance_km(self):
        # Crear una solicitud válida en kilómetros
        request = pb2.SourceDest(
            source=pb2.Position(
                latitude=-33.0351516, longitude=-71.5955963, altitude=100.0
            ),
            destination=pb2.Position(
                latitude=-33.0348327, longitude=-71.5980458, altitude=100.0
            ),
            unit="km",
        )

        response = self.servicer.geodesic_distance(request, self.context)

        self.assertGreater(response.distance, 0)
        self.assertEqual(response.method, "geodesic")
        self.assertEqual(response.unit, "km")

    def test_valid_distance_nm(self):
        # Crear una solicitud válida en millas náuticas
        request = pb2.SourceDest(
            source=pb2.Position(latitude=-33.0351516, longitude=-71.5955963),
            destination=pb2.Position(latitude=-33.0348327, longitude=-71.5980458),
            unit="nm",
        )

        response = self.servicer.geodesic_distance(request, self.context)

        self.assertGreater(response.distance, 0)
        self.assertEqual(response.method, "geodesic")
        self.assertEqual(response.unit, "nm")

    def test_invalid_unit(self):
        # Probar con una unidad inválida
        request = pb2.SourceDest(
            source=pb2.Position(latitude=-33.0351516, longitude=-71.5955963),
            destination=pb2.Position(latitude=-33.0348327, longitude=-71.5980458),
            unit="invalid_unit",
        )

        response = self.servicer.geodesic_distance(request, self.context)

        self.assertEqual(response.distance, -1)
        self.assertEqual(response.method, "geodesic")
        self.assertEqual(response.unit, "invalid")

    def test_invalid_coordinates(self):
        # Probar con coordenadas inválidas
        request = pb2.SourceDest(
            source=pb2.Position(
                latitude=91.0, longitude=-71.5955963  # Latitud fuera de rango
            ),
            destination=pb2.Position(latitude=-33.0348327, longitude=-71.5980458),
            unit="km",
        )

        response = self.servicer.geodesic_distance(request, self.context)

        self.assertEqual(response.distance, -1)
        self.assertEqual(response.method, "geodesic")
        self.assertEqual(response.unit, "invalid")
        self.context.set_code.assert_called_once_with(grpc.StatusCode.INVALID_ARGUMENT)

    def test_default_unit(self):
        # Probar sin especificar unidad (debería usar km por defecto)
        request = pb2.SourceDest(
            source=pb2.Position(latitude=-33.0351516, longitude=-71.5955963),
            destination=pb2.Position(latitude=-33.0348327, longitude=-71.5980458),
        )

        response = self.servicer.geodesic_distance(request, self.context)

        self.assertGreater(response.distance, 0)
        self.assertEqual(response.method, "geodesic")
        self.assertEqual(response.unit, "km")

    def test_error_handling(self):
        # Probar el manejo de errores generales
        with patch("server.Distance") as mock_distance:
            mock_distance.side_effect = Exception("Error de prueba")

            request = pb2.SourceDest(
                source=pb2.Position(latitude=-33.0351516, longitude=-71.5955963),
                destination=pb2.Position(latitude=-33.0348327, longitude=-71.5980458),
                unit="km",
            )

            response = self.servicer.geodesic_distance(request, self.context)

            self.assertEqual(response.distance, -1)
            self.assertEqual(response.method, "geodesic")
            self.assertEqual(response.unit, "invalid")
            self.context.set_code.assert_called_once_with(grpc.StatusCode.INTERNAL)


if __name__ == "__main__":
    unittest.main()
