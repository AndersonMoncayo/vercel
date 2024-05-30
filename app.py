from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Configurar la clave de API
API_KEY = 'AIzaSyDtan70L7kfUnKxNL2o4YnFY1J9xmY7qXk'
genai.configure(api_key=API_KEY)

# Configurar el modelo
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 0,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Definir los prompts y respuestas
prompt_parts = [
   "input: modalidades de ingreso, ingreso, como ingresar",
"output: Las modalidades de ingreso incluyen: estudiante nuevo, en continuidad de los ciclos propedéuticos, de reingreso, de transferencia interna o externa, y de articulación."

"input: Inscripción del Estudiante, inscripción, inscribirse",
"output: Las modalidades de ingreso incluyen: estudiante nuevo, en continuidad de los ciclos propedéuticos, de reingreso, de transferencia interna o externa, y de articulación."

"input: Vision, visión, Visión",
"output: El Instituto Tecnológico del Putumayo, se consolidará como una Institución de Educación superior, acreditada y líder en procesos tecnológicos, socioeconómicos, culturales y ambientales a través de la investigación, la docencia y la proyección social, en la región andino-amazónica y en el país.."

"input: Principios, que principios",
"output: Ética - Autonomía - democracia - Participativa - Idoneidad - Compromiso social - Integración - Universalidad - Racionalida -   Pertinencia -   Sostenibilidad -    Sustentabilidad"

"input: Valores, que valores",
"output: Participación - Solidaridad y Tolerancia - Respeto - Sentido de Pertenencia - Honestidad - Libertad - Liderazgo"

"input: Proceso de Inscripción, inscripción, proceso de inscripcion",
"output: La inscripción es el acto mediante el cual el aspirante manifiesta su voluntad de vincularse a uno de los programas ofrecidos por el Instituto. Puede hacerse personalmente, por terceros, por correo certificado, o por medios electrónicos que el Instituto disponga."

"input: Proceso de Selección y Admisión, selección, admisión",
"output: El proceso de selección y admisión evalúa los conocimientos, aptitudes y actitudes del aspirante. El Consejo Académico define los mecanismos y pruebas de selección y admisión."

"input: Prueba de Admisión, prueba, examen de ingreso",
"output: La prueba de admisión es aplicada a quienes aspiran ingresar a un programa académico y es definida y reglamentada por el Consejo Académico. Los resultados son válidos solo para el período y programa para el cual se presentan."

"input: Matrícula Inicial, matrícula, inscribirse",
"output: La matrícula inicial es el acto personal que cumple todo aspirante admitido dentro de las fechas establecidas, adquiriendo los derechos y deberes como estudiante regular. La renovación de matrícula es similar y debe realizarse cada período académico."

"input: Requisitos de Matrícula, requisitos, inscripción",
"output: Para matricularse por primera vez se requiere haber sido admitido, pagar los derechos correspondientes y presentar la documentación exigida. Existen dos tipos de matrícula: ordinaria y extraordinaria."

"input: Liquidación de Derechos de Matrícula, liquidación, derechos de matrícula",
"output: La liquidación de derechos de matrícula y otros servicios académicos es realizada por la Vicerrectoría Administrativa. El registro de unidades de formación se realiza después de efectuar la matrícula financiera, dentro de las fechas establecidas."

"input: Categorías de Estudiantes, categorías, tipos de estudiantes",
"output: Las categorías de estudiantes incluyen estudiantes de pregrado, de especialización, en articulación, de programas de educación para el trabajo y desarrollo humano, y de educación continuada."

"input: Calidad de Estudiante, calidad, ser estudiante",
"output: La calidad de estudiante se adquiere mediante la matrícula y se puede ser estudiante regular, por convenio, de reingreso, de transferencia, y de articulación."

"input: POLÍTICA DE CALIDAD, politica de calidad",
"output: El Instituto Tecnológico del Putumayo declara la calidad compromiso permanente, con el fin de satisfacer las necesidades de sus usuarios, fortaleciendo la docencia, la investigación y proyección social; garantizando el mejoramiento continuo de los procesos académicos y administrativos, con base en el compromiso de su talento humano y la gestión y optimización de sus recursos, dentro del marco legal que le aplica."

"input: Derechos de los Estudiantes, derechos, derechos del estudiante",
"output: Todo estudiante tiene derecho a recibir una educación de calidad, a participar en los órganos de gobierno del Instituto, y a recibir servicios de bienestar, entre otros derechos."

"input: Deberes de los Estudiantes, deberes, responsabilidades del estudiante",
"output: Los estudiantes deben cumplir con las normas establecidas, asistir regularmente a las clases y actividades programadas, respetar la convivencia y los bienes del Instituto, y mantener un rendimiento académico adecuado."

"input: ESLOGAN, eslogan",
"output: El saber como arma de vida"

"input: Programa Académico, programa, estructura académica",
"output: Un programa académico es un conjunto de unidades de formación articuladas coherentemente, con objetivos y competencias definidos. La estructura curricular incluye formación técnica profesional, tecnológica, profesional, y de especialización."

"input: Componentes de la Formación, componentes, formación académica",
"output: Esta formación incluye componentes teóricos y prácticos, diseñados para desarrollar competencias específicas en el área de estudio del estudiante."

"input: Prácticas Empresariales y Pasantías, prácticas, pasantías",
"output: Las prácticas empresariales y pasantías son componentes importantes de la formación académica, permitiendo a los estudiantes aplicar sus conocimientos en entornos reales."

"input: Unidades de Formación, unidades, cursos académicos",
"output: Las unidades de formación son módulos o cursos que componen un programa académico. Cada unidad de formación tiene objetivos específicos y contribuye al desarrollo de competencias del estudiante."

"input: Clasificación de los Programas Curriculares, clasificación, programas curriculares",
"output: Los programas curriculares se clasifican en niveles y ciclos, y cada programa tiene especificaciones en términos de duración, créditos, y competencias a desarrollar."

"input: Crédito Académico, crédito, medida académica",
"output: Un crédito académico es una unidad de medida del trabajo académico del estudiante, equivalendo a 48 horas de actividades académicas. Este tiempo incluye horas de clase y trabajo independiente del estudiante."

"input: Cancelación de Unidades de Formación, cancelación, unidades de formación",
"output: La cancelación de unidades de formación debe tramitarse ante el docente de apoyo y la Vicerrectoría Académica. La adición de unidades de formación también requiere aprobación y debe realizarse dentro de las fechas establecidas."

"input: Cursos Intensivos, cursos intensivos, cursos cortos",
"output: Los cursos intensivos son aquellos que se desarrollan en un período más corto que el regular. Estos cursos deben cumplir con los mismos requisitos y objetivos que los cursos regulares."

"input: Calendario Académico, calendario, período académico",
"output: El período académico es el tiempo en el que se desarrollan las actividades académicas y se evalúa el rendimiento de los estudiantes. El año académico está compuesto por varios períodos."

"input: Asistencia a las Actividades Académicas, asistencia, actividades académicas",
"output: Los estudiantes deben asistir regularmente a todas las actividades académicas programadas. La asistencia es registrada y puede influir en la evaluación final del estudiante."

"input: Evaluación de los Estudiantes, evaluación, calificaciones",
"output: La evaluación de los estudiantes se realiza a través de diferentes métodos, incluyendo exámenes, trabajos prácticos, y proyectos. Las calificaciones deben ser registradas oficialmente y los estudiantes tienen derecho a conocer y revisar sus resultados."

"input: Evaluación por Competencias, evaluación por competencias, criterios de evaluación",
"output: La evaluación por competencias implica valorar el desarrollo de habilidades y conocimientos específicos en los estudiantes. Este tipo de evaluación se basa en criterios definidos y objetivos medibles."

"input: Rendimiento Académico, rendimiento, desempeño académico",
"output: El rendimiento académico se mide a través de las calificaciones obtenidas en las unidades de formación. Los estudiantes deben mantener un promedio mínimo para permanecer en el programa y evitar sanciones académicas."

"input: Trabajo de Grado, trabajo de grado, proyecto de investigación",
"output: El trabajo de grado es un requisito para la titulación. Los estudiantes deben desarrollar un proyecto de investigación bajo la supervisión de un tutor y cumplir con los requisitos establecidos por el programa académico."

"input: Otorgamiento de Títulos, otorgamiento de títulos, titulación",
"output: Para obtener un título, los estudiantes deben haber cumplido con todos los requisitos académicos y administrativos del programa, incluyendo la aprobación del trabajo de grado y la presentación de exámenes finales."

"input: Constancias y Certificados de Estudio, constancias, certificados",
"output: Las constancias y certificados de estudio se solicitan a través de la dependencia de Admisiones Registro y Control Académico, y deben cumplir con los requisitos y procedimientos establecidos por el Instituto."

"input: Reconocimientos y Estímulos, reconocimientos, estímulos",
"output: El Instituto otorga reconocimientos y estímulos a los estudiantes que se destacan en su rendimiento académico, deportivo, cultural, o en servicios a la comunidad. Estos estímulos incluyen matrículas de excelencia, menciones de honor, y premios a la innovación."

"input: Servicios de Bienestar, servicios, bienestar estudiantil",
"output: El Instituto ofrece servicios de bienestar que incluyen asistencia médica, psicológica, odontológica, y programas culturales, artísticos, y deportivos. Estos servicios están orientados al desarrollo integral de los estudiantes."

"input: Régimen Disciplinario, régimen disciplinario, normas disciplinarias",
"output: Las normas disciplinarias establecen las conductas prohibidas y las sanciones aplicables en caso de incumplimiento. El régimen disciplinario busca mantener el orden y el respeto en la comunidad educativa."

"input: Sanciones, sanciones, medidas disciplinarias",
"output: Las sanciones pueden incluir amonestaciones, suspensiones, y expulsiones, dependiendo de la gravedad de la falta. Los procedimientos disciplinarios garantizan el derecho a la defensa y el debido proceso."

"input: Procedimiento Disciplinario, procedimiento disciplinario, proceso disciplinario",
"output: Los procedimientos disciplinarios incluyen la investigación de las faltas, la notificación al estudiante implicado, y la resolución del caso por parte de las autoridades competentes del Instituto."

"input: Vigencia del Estatuto, vigencia, estatuto estudiantil",
"output: El estatuto estudiantil entra en vigencia a partir de su aprobación y puede ser modificado por el Consejo Directivo del Instituto."

"input: Misión del Instituto, misión,mision, objetivo del instituto",
"output: Ofrecer educación superior de calidad, orientada al desarrollo integral de sus estudiantes y a la proyección social."

"input: Objetivos Generales, objetivos, metas del instituto",
"output: Orientar la gestión de programas académicos, establecer políticas para la docencia e investigación, y diseñar una estructura presupuestal efectiva."

"input: Proceso de Inscripción, proceso de inscripción, manifestación de voluntad",
"output: Manifestación de la voluntad del aspirante de vincularse al Instituto, pago de derechos de inscripción, y presentación de la documentación requerida."

"input: Ciclo Tecnológico, ciclo tecnológico, ciclo académico",
"output: Requisito: Título de bachiller y haber completado satisfactoriamente el ciclo Técnico Profesional."

"input: Matrícula Inicial, matricula inicial ",
"output: Acto personal que cumple el aspirante admitido dentro de las fechas establecidas, adquiriendo los derechos y deberes como estudiante regular."

"input: Derechos de los Estudiantes de Pregrado, derechos de pregrado, derechos académicos",
"output: Recibir una educación de calidad, participar en los órganos de gobierno del Instituto, y acceder a servicios de bienestar."

"input: Deberes Fundamentales de los Estudiantes, deberes fundamentales, responsabilidades académicas",
"output: Cumplir con las normas establecidas, asistir regularmente a clases, respetar la convivencia y los bienes del Instituto, y mantener un rendimiento académico adecuado."

"input: Programa Académico, programa académico, estructura de formación",
"output: Estructura en unidades de formación articuladas coherentemente, con objetivos y competencias definidos."

"input: Formación Técnica Profesional, formación técnica, educación técnica",
"output: Incluye componentes teóricos y prácticos, diseñados para desarrollar competencias específicas en el área de estudio del estudiante."

"input: Prácticas Empresariales y Pasantías, prácticas empresariales, pasantías",
"output: Permiten a los estudiantes aplicar sus conocimientos en entornos reales y facilitan su integración al mundo laboral."

"input: Unidad de Formación, unidad de formación, módulo académico",
"output: Módulo o curso que compone un programa académico. Se clasifica en niveles y ciclos, y tiene especificaciones en términos de duración, créditos y competencias a desarrollar."

"input: Créditos Académicos, créditos, unidad de medida académica",
"output: Un crédito académico es una unidad de medida del trabajo académico del estudiante, equivalendo a 48 horas de actividades académicas."

"input: Cancelación de Unidades de Formación, cancelación de unidades, retirada de cursos",
"output: La cancelación de unidades de formación debe tramitarse ante el docente de apoyo y la Vicerrectoría Académica."

"input: Cursos Intensivos, cursos intensivos, programas cortos",
"output: Los cursos intensivos son aquellos que se desarrollan en un período más corto que el regular y deben cumplir con los mismos requisitos y objetivos que los cursos regulares."

"input: Calendario Académico, calendario académico, períodos académicos",
"output: El período académico es el tiempo en el que se desarrollan las actividades académicas y se evalúa el rendimiento de los estudiantes."

"input: Asistencia a Actividades Académicas, asistencia a actividades, asistencia académica",
"output: Los estudiantes deben asistir regularmente a todas las actividades académicas programadas. La asistencia es registrada y puede influir en la evaluación final del estudiante."

"input: Evaluación de los Estudiantes, evaluación de estudiantes, métodos de evaluación",
"output: La evaluación de los estudiantes se realiza a través de diferentes métodos, incluyendo exámenes, trabajos prácticos, y proyectos."
"input: Evaluación por Competencias, evaluación por competencias, criterios de evaluación",
"output: La evaluación por competencias implica valorar el desarrollo de habilidades y conocimientos específicos en los estudiantes."

"input: Rendimiento Académico, rendimiento académico, desempeño académico",
"output: El rendimiento académico se mide a través de las calificaciones obtenidas en las unidades de formación."

"input: Trabajo de Grado, trabajo de grado, proyecto de investigación",
"output: El trabajo de grado es un requisito para la titulación. Los estudiantes deben desarrollar un proyecto de investigación bajo la supervisión de un tutor."

"input: Otorgamiento de Títulos, otorgamiento de títulos, titulación",
"output: Para obtener un título, los estudiantes deben haber cumplido con todos los requisitos académicos y administrativos del programa."

"input: Constancias y Certificados de Estudio, constancias, certificados",
"output: Las constancias y certificados de estudio se solicitan a través de la dependencia de Admisiones Registro y Control Académico."

"input: Reconocimientos y Estímulos, reconocimientos, estímulos",
"output: El Instituto otorga reconocimientos y estímulos a los estudiantes que se destacan en su rendimiento académico, deportivo, cultural, o en servicios a la comunidad."

"input: Servicios de Bienestar, servicios de bienestar, bienestar estudiantil",
"output: El Instituto ofrece servicios de bienestar que incluyen asistencia médica, psicológica, odontológica, y programas culturales, artísticos, y deportivos."

"input: Régimen Disciplinario, régimen disciplinario, normas disciplinarias",
"output: Las normas disciplinarias establecen las conductas prohibidas y las sanciones aplicables en caso de incumplimiento."

"input: Sanciones, sanciones, medidas disciplinarias",
"output: Las sanciones pueden incluir amonestaciones, suspensiones, y expulsiones, dependiendo de la gravedad de la falta."

"input: Procedimiento Disciplinario, procedimiento disciplinario, proceso disciplinario",
"output: Los procedimientos disciplinarios incluyen la investigación de las faltas, la notificación al estudiante implicado, y la resolución del caso por parte de las autoridades competentes del Instituto."

"input: Vigencia del Estatuto, vigencia, estatuto estudiantil",
"output: El estatuto estudiantil entra en vigencia a partir de su aprobación y puede ser modificado por el Consejo Directivo del Instituto."

"input: Misión del Instituto, misión, objetivo del instituto",
"output: Ofrecer educación superior de calidad, orientada al desarrollo integral de sus estudiantes y a la proyección social."

"input: Objetivos Generales, objetivos generales, metas del instituto",
"output: Orientar la gestión de programas académicos, establecer políticas para la docencia e investigación, y diseñar una estructura presupuestal efectiva."

"input: Proceso de Inscripción, proceso de inscripción, manifestación de voluntad",
"output: Manifestación de la voluntad del aspirante de vincularse al Instituto, pago de derechos de inscripción, y presentación de la documentación requerida."

"input: Ciclo Tecnológico, ciclo tecnológico, ciclo académico",
"output: Requisito: Título de bachiller y haber completado satisfactoriamente el ciclo Técnico Profesional."

"input: Matrícula Inicial, matrícula inicial, inscripción",
"output: Acto personal que cumple el aspirante admitido dentro de las fechas establecidas, adquiriendo los derechos y deberes como estudiante regular."

"input: Derechos de los Estudiantes de Pregrado, derechos de pregrado, derechos académicos",
"output: Recibir una educación de calidad, participar en los órganos de gobierno del Instituto, y acceder a servicios de bienestar."

"input: Deberes Fundamentales de los Estudiantes, deberes fundamentales, responsabilidades académicas",
"output: Cumplir con las normas establecidas, asistir regularmente a clases, respetar la convivencia y los bienes del Instituto, y mantener un rendimiento académico adecuado."

"input: Programa Académico, programa académico, estructura de formación",
"output: Estructura en unidades de formación articuladas coherentemente, con objetivos y competencias definidos."

"input: Formación Técnica Profesional, formación técnica profesional, educación técnica",
"output: Incluye componentes teóricos y prácticos, diseñados para desarrollar competencias específicas en el área de estudio del estudiante."

"input: Prácticas Empresariales y Pasantías, prácticas empresariales, pasantías",
"output: Permiten a los estudiantes aplicar sus conocimientos en entornos reales y facilitan su integración al mundo laboral."

"input: Unidad de Formación, unidad de formación, módulo académico",
"output: Módulo o curso que compone un programa académico. Se clasifica en niveles y ciclos, y tiene especificaciones en términos de duración, créditos y competencias a desarrollar."

]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['message']
        prompt_parts.append(f"input: {user_input}")
        response = model.generate_content(prompt_parts)
        respuesta = response.text
        return jsonify({'respuesta': respuesta, 'follow_up': []})
    return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
    prompt_parts.clear()
    prompt_parts.extend([
        "input: modalidades de ingreso, ingreso, como ingresar",
        "output: Las modalidades de ingreso incluyen: estudiante nuevo, en continuidad de los ciclos propedéuticos, de reingreso, de transferencia interna o externa, y de articulación.",
        "input: Inscripción del Estudiante, inscripción, inscribirse",
        "output: Las modalidades de ingreso incluyen: estudiante nuevo, en continuidad de los ciclos propedéuticos, de reingreso, de transferencia interna o externa, y de articulación.",
        "input: Vision, visión, Visión",
        "output: El Instituto Tecnológico del Putumayo, se consolidará como una Institución de Educación superior, acreditada y líder en procesos tecnológicos, socioeconómicos, culturales y ambientales a través de la investigación, la docencia y la proyección social, en la región andino-amazónica y en el país.",
        "input: Principios, que principios",
        "output: Ética - Autonomía - democracia - Participativa - Idoneidad - Compromiso social - Integración - Universalidad - Racionalida -   Pertinencia -   Sostenibilidad -    Sustentabilidad",
        "input: Valores, que valores",
        "output: Participación - Solidaridad y Tolerancia - Respeto - Sentido de Pertenencia - Honestidad - Libertad - Liderazgo",
        "input: Proceso de Inscripción, inscripción, proceso de inscripcion",
        "output: La inscripción es el acto mediante el cual el aspirante manifiesta su voluntad de vincularse a uno de los programas ofrecidos por el Instituto. Puede hacerse personalmente, por terceros, por correo certificado, o por medios electrónicos que el Instituto disponga.",
        "input: Proceso de Selección y Admisión, selección, admisión",
        "output: El proceso de selección y admisión evalúa los conocimientos, aptitudes y actitudes del aspirante. El Consejo Académico define los mecanismos y pruebas de selección y admisión.",
        "input: Prueba de Admisión, prueba, examen de ingreso",
        "output: La prueba de admisión es aplicada a quienes aspiran ingresar a un programa académico y es definida y reglamentada por el Consejo Académico. Los resultados son válidos solo para el período y programa para el cual se presentan.",
        "input: Matrícula Inicial, matrícula, inscribirse",
        "output: La matrícula inicial es el acto personal que cumple todo aspirante admitido dentro de las fechas establecidas, adquiriendo los derechos y deberes como estudiante regular. La renovación de matrícula es similar y debe realizarse cada período académico.",
        "input: Requisitos de Matrícula, requisitos, inscripción",
        "output: Para matricularse por primera vez se requiere haber sido admitido, pagar los derechos correspondientes y presentar la documentación exigida. Existen dos tipos de matrícula: ordinaria y extraordinaria.",
        "input: Liquidación de Derechos de Matrícula, liquidación, derechos de matrícula",
        "output: La liquidación de derechos de matrícula y otros servicios académicos es realizada por la Vicerrectoría Administrativa. El registro de unidades de formación se realiza después de efectuar la matrícula financiera, dentro de las fechas establecidas.",
        "input: Categorías de Estudiantes, categorías, tipos de estudiantes",
        "output: Las categorías de estudiantes incluyen estudiantes de pregrado, de especialización, en articulación, de programas de educación para el trabajo y desarrollo humano, y de educación continuada.",
        "input: Calidad de Estudiante, calidad, ser estudiante",
        "output: La calidad de estudiante se adquiere mediante la matrícula y se puede ser estudiante regular, por convenio, de reingreso, de transferencia, y de articulación.",
        "input: POLÍTICA DE CALIDAD, politica de calidad",
        "output: El Instituto Tecnológico del Putumayo declara la calidad compromiso permanente, con el fin de satisfacer las necesidades de sus usuarios, fortaleciendo la docencia, la investigación y proyección social; garantizando el mejoramiento continuo de los procesos académicos y administrativos, con base en el compromiso de su talento humano y la gestión y optimización de sus recursos, dentro del marco legal que le aplica.",
        "input: Derechos de los Estudiantes, derechos, derechos del estudiante",
        "output: Todo estudiante tiene derecho a recibir una educación de calidad, a participar en los órganos de gobierno del Instituto, y a recibir servicios de bienestar, entre otros derechos.",
        "input: Deberes de los Estudiantes, deberes, responsabilidades del estudiante",
        "output: Los estudiantes deben cumplir con las normas establecidas, asistir regularmente a las clases y actividades programadas, respetar la convivencia y los bienes del Instituto, y mantener un rendimiento académico adecuado.",
        "input: ESLOGAN, eslogan",
        "output: El saber como arma de vida",
        "input: Programa Académico, programa, estructura académica",
        "output: Un programa académico es un conjunto de unidades de formación articuladas coherentemente, con objetivos y competencias definidos. La estructura curricular incluye formación técnica profesional, tecnológica, profesional, y de especialización.",
        "input: Componentes de la Formación, componentes, formación académica",
        "output: Esta formación incluye componentes teóricos y prácticos, diseñados para desarrollar competencias específicas en el área de estudio del estudiante.",
        "input: Prácticas Empresariales y Pasantías, prácticas, pasantías",
        "output: Las prácticas empresariales y pasantías son componentes importantes de la formación académica, permitiendo a los estudiantes aplicar sus conocimientos en entornos reales.",
        "input: Unidades de Formación, unidades, cursos académicos",
        "output: Las unidades de formación son módulos o cursos que componen un programa académico. Cada unidad de formación tiene objetivos específicos y contribuye al desarrollo de competencias del estudiante.",
        "input: Clasificación de los Programas Curriculares, clasificación, programas curriculares",
        "output: Los programas curriculares se clasifican en niveles y ciclos, y cada programa tiene especificaciones en términos de duración, créditos, y competencias a desarrollar.",
        "input: Crédito Académico, crédito, medida académica",
        "output: Un crédito académico es una unidad de medida del trabajo académico del estudiante, equivalendo a 48 horas de actividades académicas. Este tiempo incluye horas de clase y trabajo independiente del estudiante.",
        "input: Cancelación de Unidades de Formación, cancelación, unidades de formación",
        "output: La cancelación de unidades de formación debe tramitarse ante el docente de apoyo y la Vicerrectoría Académica. La adición de unidades de formación también requiere aprobación y debe realizarse dentro de las fechas establecidas.",
        "input: Cursos Intensivos, cursos intensivos, cursos cortos",
        "output: Los cursos intensivos son aquellos que se desarrollan en un período más corto que el regular. Estos cursos deben cumplir con los mismos requisitos y objetivos que los cursos regulares.",
        "input: Calendario Académico, calendario, período académico",
        "output: El período académico es el tiempo en el que se desarrollan las actividades académicas y se evalúa el rendimiento de los estudiantes. El año académico está compuesto por varios períodos.",
        "input: Asistencia a las Actividades Académicas, asistencia, actividades académicas",
        "output: Los estudiantes deben asistir regularmente a todas las actividades académicas programadas. La asistencia es registrada y puede influir en la evaluación final del estudiante.",
        "input: Evaluación de los Estudiantes, evaluación, calificaciones",
        "output: La evaluación de los estudiantes se realiza a través de diferentes métodos, incluyendo exámenes, trabajos prácticos, y proyectos. Las calificaciones deben ser registradas oficialmente y los estudiantes tienen derecho a conocer y revisar sus resultados.",
        "input: Evaluación por Competencias, evaluación por competencias, criterios de evaluación",
        "output: La evaluación por competencias implica valorar el desarrollo de habilidades y conocimientos específicos en los estudiantes. Este tipo de evaluación se basa en criterios definidos y objetivos medibles.",
        "input: Rendimiento Académico, rendimiento, desempeño académico",
        "output: El rendimiento académico se mide a través de las calificaciones obtenidas en las unidades de formación. Los estudiantes deben mantener un promedio mínimo para permanecer en el programa y evitar sanciones académicas.",
        "input: Trabajo de Grado, trabajo de grado, proyecto de investigación",
        "output: El trabajo de grado es un requisito para la titulación. Los estudiantes deben desarrollar un proyecto de investigación bajo la supervisión de un tutor y cumplir con los requisitos establecidos por el programa académico.",
        "input: Otorgamiento de Títulos, otorgamiento de títulos, titulación",
        "output: Para obtener un título, los estudiantes deben haber cumplido con todos los requisitos académicos y administrativos del programa, incluyendo la aprobación del trabajo de grado y la presentación de exámenes finales.",
        "input: Constancias y Certificados de Estudio, constancias, certificados",
        "output: Las constancias y certificados de estudio se solicitan a través de la dependencia de Admisiones Registro y Control Académico, y deben cumplir con los requisitos y procedimientos establecidos por el Instituto.",
        "input: Reconocimientos y Estímulos, reconocimientos, estímulos",
        "output: El Instituto otorga reconocimientos y estímulos a los estudiantes que se destacan en su rendimiento académico, deportivo, cultural, o en servicios a la comunidad. Estos estímulos incluyen matrículas de excelencia, menciones de honor, y premios a la innovación.",
        "input: Servicios de Bienestar, servicios, bienestar estudiantil",
        "output: El Instituto ofrece servicios de bienestar que incluyen asistencia médica, psicológica, odontológica, y programas culturales, artísticos, y deportivos. Estos servicios están orientados al desarrollo integral de los estudiantes.",
        "input: Régimen Disciplinario, régimen disciplinario, normas disciplinarias",
        "output: Las normas disciplinarias establecen las conductas prohibidas y las sanciones aplicables en caso de incumplimiento. El régimen disciplinario busca mantener el orden y el respeto en la comunidad educativa.",
        "input: Sanciones, sanciones, medidas disciplinarias",
        "output: Las sanciones pueden incluir amonestaciones, suspensiones, y expulsiones, dependiendo de la gravedad de la falta. Los procedimientos disciplinarios garantizan el derecho a la defensa y el debido proceso.",
        "input: Procedimiento Disciplinario, procedimiento disciplinario, proceso disciplinario",
        "output: Los procedimientos disciplinarios incluyen la investigación de las faltas, la notificación al estudiante implicado, y la resolución del caso por parte de las autoridades competentes del Instituto.",
        "input: Vigencia del Estatuto, vigencia, estatuto estudiantil",
        "output: El estatuto estudiantil entra en vigencia a partir de su aprobación y puede ser modificado por el Consejo Directivo del Instituto.",
        "input: Misión del Instituto, misión, objetivo del instituto",
        "output: Ofrecer educación superior de calidad, orientada al desarrollo integral de sus estudiantes y a la proyección social.",
        "input: Objetivos Generales, objetivos, metas del instituto",
        "output: Orientar la gestión de programas académicos, establecer políticas para la docencia e investigación, y diseñar una estructura presupuestal efectiva.",
        "input: Proceso de Inscripción, proceso de inscripción, manifestación de voluntad",
        "output: Manifestación de la voluntad del aspirante de vincularse al Instituto, pago de derechos de inscripción, y presentación de la documentación requerida.",
        "input: Ciclo Tecnológico, ciclo tecnológico, ciclo académico",
        "output: Requisito: Título de bachiller y haber completado satisfactoriamente el ciclo Técnico Profesional.",
        "input: Matrícula Inicial, matrícula inicial",
        "output: Acto personal que cumple el aspirante admitido dentro de las fechas establecidas, adquiriendo los derechos y deberes como estudiante regular.",
        "input: Derechos de los Estudiantes de Pregrado, derechos de pregrado, derechos académicos",
        "output: Recibir una educación de calidad, participar en los órganos de gobierno del Instituto, y acceder a servicios de bienestar.",
        "input: Deberes Fundamentales de los Estudiantes, deberes fundamentales, responsabilidades académicas",
        "output: Cumplir con las normas establecidas, asistir regularmente a clases, respetar la convivencia y los bienes del Instituto, y mantener un rendimiento académico adecuado.",
        "input: Programa Académico, programa académico, estructura de formación",
        "output: Estructura en unidades de formación articuladas coherentemente, con objetivos y competencias definidos.",
        "input: Formación Técnica Profesional, formación técnica profesional, educación técnica",
        "output: Incluye componentes teóricos y prácticos, diseñados para desarrollar competencias específicas en el área de estudio del estudiante.",
        "input: Prácticas Empresariales y Pasantías, prácticas empresariales, pasantías",
        "output: Permiten a los estudiantes aplicar sus conocimientos en entornos reales y facilitan su integración al mundo laboral.",
        "input: Unidad de Formación, unidad de formación, módulo académico",
        "output: Módulo o curso que compone un programa académico. Se clasifica en niveles y ciclos, y tiene especificaciones en términos de duración, créditos y competencias a desarrollar."
    ])
    return jsonify({'status': 'reset'})

if __name__ == '__main__':
    app.run(debug=True)
