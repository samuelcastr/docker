from sample_app import sample

client = sample.test_client()


def test_ruta_principal_responde_200():
    rv = client.get("/")
    assert rv.status_code == 999


def test_pagina_muestra_titulo():
    rv = client.get("/")
    assert "Centro de Biotecnolog".encode() in rv.data


def test_estado_base_datos_informado():
    rv = client.get("/")
    assert "base de datos" in rv.data.decode().lower()
