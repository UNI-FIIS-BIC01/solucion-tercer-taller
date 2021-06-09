import io
import sys
from typing import Dict

from dominios import obtener_dominio, mostrar_valores, registrar_dominio, actualizar_dominio, generar_pais_por_dominio
from pruebabase import PruebaBase


class DominiosTest(PruebaBase):

    def test_obtener_dominio(self):
        dominios: Dict[str, str] = {"Peru": "pe"}

        self.assertEqual("pe", obtener_dominio(dominios, "Peru"))
        self.assertEqual(None, obtener_dominio(dominios, "Chile"))

    def test_mostrar_valores_vacio(self):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        dominios: Dict[str, str] = {}

        mostrar_valores(dominios)
        self.assert_over_list(resultado_test, ["No hay valores que mostrar."])

    def test_mostrar_valores(self):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        dominios: Dict[str, str] = {"Peru": "pe", "Brasil": "br", "Chile": "cl"}

        mostrar_valores(dominios)
        self.assert_over_file(resultado_test, "test/test_mostrar_valores.txt")

    def test_registrar_domino(self):
        dominios: Dict[str, str] = {}
        registrar_dominio(dominios, "Peru", "pe")

        self.assertEqual({"Peru": "pe"}, dominios)

    def test_registrar_dominio_existente(self):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test
        dominios: Dict[str, str] = {"Peru": "pe"}

        registrar_dominio(dominios, "Peru", "per")
        self.assertEqual({"Peru": "pe"}, dominios)
        self.assert_over_list(resultado_test, ["El pais Peru ya se encuentra registrado con el dominio pe."])

    def test_actualizar_dominio(self):
        dominios: Dict[str, str] = {"Peru": "per"}
        actualizar_dominio(dominios, "Peru", "pe")

        self.assertEqual({"Peru": "pe"}, dominios)

    def test_actualizar_dominio_ausente(self):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test
        dominios: Dict[str, str] = {}

        actualizar_dominio(dominios, "Peru", "pe")
        self.assertEqual({}, dominios)
        self.assert_over_list(resultado_test, ["El pais Peru no esta registrado."])

    def test_generar_pais_por_dominio(self):
        dominios: Dict[str, str] = {"Peru": "pe", "Brasil": "br", "Chile": "cl"}
        resultado_esperado = {"PE": "PERU",
                              "BR": "BRASIL",
                              "CL": "CHILE"}

        self.assertEqual(resultado_esperado, generar_pais_por_dominio(dominios))
