from ejemplo.models import Familiar

Familiar(nombre="Anibal", direccion="Gabrieles 98-4b", numero_pasaporte=12172548, fecha_nacimiento="26/08/1974").save()
Familiar(nombre="Carmen", direccion="Gabrieles 98-4b", numero_pasaporte=3660032, fecha_nacimiento="08/09/1947").save()
Familiar(nombre="Barbara", direccion="Gabrieles 98-4b", numero_pasaporte=10785673, fecha_nacimiento="31/06/1975").save()
Familiar(nombre="Clara", direccion="Gabrieles 98-4b", numero_pasaporte=3289657, fecha_nacimiento="31/03/1943").save()

print("Se cargo con exito los usuarios de pruebas")