#usuario: medico1
#contraseña: clave1
class Paciente:
    def __init__(self, documento, nombre, sexo, fecha_nacimiento):
        self.documento = documento  # Número de documento del paciente
        self.nombre = nombre  # Nombre completo del paciente
        self.sexo = sexo  # Género del paciente ("M" para masculino, "F" para femenino)
        self.fecha_nacimiento = fecha_nacimiento  # Fecha de nacimiento del paciente
        self.historia_clinica = HistoriaClinica()  # Inicialización de la historia clínica del paciente


class SignosVitales:
    def __init__(self, presion_arterial, temperatura, saturacion_O2, frecuencia_respiratoria):
        self.presion_arterial = presion_arterial  # Valor de la presión arterial
        self.temperatura = temperatura  # Temperatura corporal del paciente en grados Celsius
        self.saturacion_O2 = saturacion_O2  # Nivel de saturación de oxígeno en sangre
        self.frecuencia_respiratoria = frecuencia_respiratoria  # Frecuencia respiratoria del paciente


class HistoriaClinica:
    def __init__(self):
        self.signos_vitales = []  # Lista de registros de signos vitales del paciente
        self.notas_evolucion = []  # Lista de notas de evolución clínica del paciente
        self.imagenes_diagnosticas = []  # Lista de imágenes diagnósticas relacionadas al paciente
        self.resultados_examenes = []  # Lista de resultados de exámenes médicos del paciente
        self.medicamentos_formulados = []  # Lista de medicamentos formulados para el paciente

    def agregar_signos_vitales(self, signos_vitales):
        self.signos_vitales.append(signos_vitales)  # Agrega un registro de signos vitales a la historia clínica

    def agregar_nota_evolucion(self, nota):
        self.notas_evolucion.append(nota)  # Agrega una nota de evolución clínica a la historia clínica

    def agregar_imagen_diagnostica(self, imagen):
        self.imagenes_diagnosticas.append(imagen)  # Agrega una imagen diagnóstica a la historia clínica

    def agregar_resultado_examen(self, resultado):
        self.resultados_examenes.append(resultado)  # Agrega un resultado de examen médico a la historia clínica

    def agregar_medicamento(self, medicamento):
        self.medicamentos_formulados.append(medicamento)  # Agrega un medicamento formulado al paciente


class Hospital:
    def __init__(self):
        self.camas_disponibles = 300  # Cantidad total de camas disponibles en el hospital
        self.pacientes_atendidos = []  # Lista de pacientes atendidos en el hospital

    def registrar_paciente(self, paciente):
        if self.camas_disponibles > 0:
            self.pacientes_atendidos.append(paciente)  # Agrega un paciente a la lista de pacientes atendidos
            self.camas_disponibles -= 1  # Reduce la cantidad de camas disponibles
            print(f"Paciente {paciente.nombre} registrado con éxito. Camas disponibles: {self.camas_disponibles}")
        else:
            print("No hay camas disponibles. El paciente no puede ser registrado.")

    def generar_reporte_indicadores(self):  # reporte de indicadores del hospital
        total_camas = 300
        camas_ocupadas = total_camas - self.camas_disponibles
        porcentaje_ocupacion = (camas_ocupadas / total_camas) * 100 if total_camas > 0 else 0

        print("Reporte de Indicadores Hospitalarios: ")
        print(f"Total de camas disponibles: {total_camas}")
        print(f"Camas ocupadas: {camas_ocupadas}")
        print(f"Porcentaje de ocupación de camas: {porcentaje_ocupacion:.2f}%")

        if len(self.pacientes_atendidos) > 0:
            estancia_promedio = sum(
                len(paciente.historia_clinica.notas_evolucion) for paciente in self.pacientes_atendidos) / len(
                self.pacientes_atendidos)
            print(f"Estancia promedio de pacientes: {estancia_promedio:.2f} días")
        else:
            print("No hay pacientes registrados en el hospital.")


def buscar_paciente_por_documento(pacientes, documento):
    for paciente in pacientes:
        if paciente.documento == documento:
            return paciente
    return None


def mostrar_historia_clinica(paciente):
    print("\nHistoria Clínica de Paciente: ")
    print(f"Documento: {paciente.documento}")
    print(f"Nombre: {paciente.nombre}")
    print(f"Sexo: {paciente.sexo}")
    print(f"Fecha de Nacimiento: {paciente.fecha_nacimiento}")
    print("------------------------------")
    historia_clinica = paciente.historia_clinica
    print("\nSignos Vitales: ")
    for sv in historia_clinica.signos_vitales:
        print(f"Presión Arterial: {sv.presion_arterial}")
        print(f"Temperatura: {sv.temperatura} °C")
        print(f"Saturación de O2: {sv.saturacion_O2}")
        print(f"Frecuencia Respiratoria: {sv.frecuencia_respiratoria}")
        print("------------------------------")

    print("\nNotas de Evolucion: ")
    for nota in historia_clinica.notas_evolucion:
        print(nota)
        print("------------------------------")

    print("\nImágenes Diagnosticas: ")
    for imagen in historia_clinica.imagenes_diagnosticas:
        print(imagen)
        print("------------------------------")

    print("\nResultados de Exámenes de Laboratorio: ")
    for resultado in historia_clinica.resultados_examenes:
        print(resultado)
        print("------------------------------")

    print("\nMedicamentos Formulados: ")
    for medicamento in historia_clinica.medicamentos_formulados:
        print(medicamento)
        print("------------------------------")


import os


def autenticar():
    usuarios_autorizados = [
        {"usuario": "medico1", "contrasena": "clave1"},
        {"usuario": "medico2", "contrasena": "clave2"},
    ]

    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    for usuario_autorizado in usuarios_autorizados:
        if usuario_autorizado["usuario"] == usuario and usuario_autorizado["contrasena"] == contrasena:
            return True

    return False


def main():
    hospital = Hospital()
    if autenticar():
        os.system('cls')
        while True:
            # Muestra el menú principal.
            print("\nMenú Principal:")
            print("1. Registrar un nuevo paciente")
            print("2. Registrar signos vitales")
            print("3. Registrar notas de evolución")
            print("4. Registrar imágenes diagnósticas")
            print("5. Registrar resultados de exámenes de laboratorio")
            print("6. Prescribir medicamentos")
            print("7. Consultar historia clínica de un paciente")
            print("8. Generar reportes de indicadores")
            print("9. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                # Registro de un nuevo paciente.
                documento = input("Ingrese el número de documento del paciente: ")
                if documento.isdigit():
                    nombre = input("Ingrese el nombre del paciente: ")
                    sexo = input("Ingrese el sexo del paciente: ")
                    fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (en formato DD/MM/AAAA): ")

                    paciente = Paciente(documento, nombre, sexo, fecha_nacimiento)
                    hospital.registrar_paciente(paciente)
                else:
                    print("El número de documento debe ser un valor numérico.")

            elif opcion == "2":
                # Registro de signos vitales para un paciente existente.
                if hospital.pacientes_atendidos:
                    documento = input("Ingrese el número de documento del paciente: ")
                    paciente_encontrado = None
                    for paciente in hospital.pacientes_atendidos:
                        if paciente.documento == documento:
                            paciente_encontrado = paciente
                            break

                    if paciente_encontrado:
                        presion_arterial = input("Ingrese la presión arterial: ")
                        temperatura = input("Ingrese la temperatura (en °C): ")
                        saturacion_O2 = input("Ingrese la saturación de oxígeno: ")
                        frecuencia_respiratoria = input("Ingrese la frecuencia respiratoria: ")

                        signos_vitales = SignosVitales(presion_arterial, temperatura, saturacion_O2,
                                                       frecuencia_respiratoria)
                        paciente_encontrado.historia_clinica.agregar_signos_vitales(signos_vitales)
                        print("Signos vitales registrados con éxito.")
                    else:
                        print("Paciente no encontrado. Por favor, verifique el número de documento.")

            elif opcion == "3":
                # Registro de notas de evolución médica para un paciente existente.
                if hospital.pacientes_atendidos:
                    documento = input("Ingrese el número de documento del paciente: ")
                    paciente_encontrado = None

                    for paciente in hospital.pacientes_atendidos:
                        if paciente.documento == documento:
                            paciente_encontrado = paciente
                            break

                    if paciente_encontrado:
                        nota_evolucion = input("Ingrese una nota de evolución médica: ")
                        paciente_encontrado.historia_clinica.agregar_nota_evolucion(nota_evolucion)
                        print("Nota de evolución registrada con éxito.")
                    else:
                        print("Paciente no encontrado. Por favor, verifique el número de documento.")

            elif opcion == "4":
                if hospital.pacientes_atendidos:
                    documento = input("Ingrese el número de documento del paciente: ")
                    paciente_encontrado = None

                    for paciente in hospital.pacientes_atendidos:
                        if paciente.documento == documento:
                            paciente_encontrado = paciente
                            break

                    if paciente_encontrado:
                        imagen_diagnostica = input("Ingrese una imagen diagnóstica: ")
                        paciente_encontrado.historia_clinica.agregar_imagen_diagnostica(imagen_diagnostica)
                        print("Imagen diagnóstica registrada con éxito.")
                    else:
                        print("Paciente no encontrado. Por favor, verifique el número de documento.")

            elif opcion == "5":
                if hospital.pacientes_atendidos:
                    documento = input("Ingrese el número de documento del paciente: ")
                    paciente_encontrado = None

                    for paciente in hospital.pacientes_atendidos:
                        if paciente.documento == documento:
                            paciente_encontrado = paciente
                            break

                    if paciente_encontrado:
                        resultado_examen = input("Ingrese el resultado de un examen de laboratorio: ")
                        paciente_encontrado.historia_clinica.agregar_resultado_examen(resultado_examen)
                        print("Resultado de examen registrado con éxito.")
                    else:
                        print("Paciente no encontrado. Por favor, verifique el número de documento.")

            elif opcion == "6":
                if hospital.pacientes_atendidos:
                    documento = input("Ingrese el número de documento del paciente: ")
                    paciente_encontrado = None

                    for paciente in hospital.pacientes_atendidos:
                        if paciente.documento == documento:
                            paciente_encontrado = paciente
                            break

                    if paciente_encontrado:
                        medicamento = input("Ingrese un medicamento formulado: ")
                        paciente_encontrado.historia_clinica.agregar_medicamento(medicamento)
                        print("Medicamento formulado registrado con éxito.")
                    else:
                        print("Paciente no encontrado. Por favor, verifique el número de documento.")

            elif opcion == "7":
                # Consulta de la historia clínica de un paciente.
                documento = input("Ingrese el número de documento del paciente: ")
                paciente_encontrado = buscar_paciente_por_documento(hospital.pacientes_atendidos, documento)

                if paciente_encontrado:
                    mostrar_historia_clinica(paciente_encontrado)
                else:
                    print("Paciente no encontrado. Por favor, verifique el número de documento.")

            elif opcion == "8":
                # se genera reportes de indicadores.
                hospital.generar_reporte_indicadores()

            elif opcion == "9":
                print("Gracias por usar el Sistema de Información del Hospital San Vicente. ¡Hasta luego!")
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
