# Cuestionario # 01: Requerimientos, Criterios, Casos
## Referencias
https://lorenzosolano.com/what-is-coding-dojo/
https://lorenzosolano.com/requirements-acceptance-criteria-and/

### 1. ¿Qué es un Coding Dojo?
Un _coding dojo_ es una reunión en donde un conjunto de desarrolladores se coordina para trabajar en un reto de  código. Las actividades a realizar suelen ser divertidas, colaborativas y no competetivas.

Se utilizan técnicas de práctica que requieran de mucho esfuerzo para mejorar; el objetivo principal es el mejoramiento personal con ayuda del grupo.

Es seguro probar nuevas ideas, y personas de todos los niveles de conocimiento pueden participar en el.

Las reuniones en un _coding dojo_ suelen ser de 2 horas y media hasta 3 horas, con una presencialidad de 5 a 20 personas, en una habitación en la que todas las personas tienen acceso a ver el progreso grupal (ya sea a través de un gran monitor o un proyector).

### 2. Diferencia entre Requerimientos, Criterios de Aceptación y Escenarios de Prueba. Dar ejemplos a partir de un problema distinto a la referencia.

**Requerimiento**: Se refiere a lo que el cliente quiere que el programa tenga o pueda hacer, una posible solución a un problema. Es más una descripción que una lista de cosas que hacer. Existen requerimientos funcionales y no funcionales:
* Los requerimientos funcionales determinan las cosas que debe poder hacer el programa (puede sumar, restar, comunicarse con la base de datos).
* Los requerimientos _no_ funcionales no determinan una funcionalidad, sino una cualidad (confiable) o restriccion (seguridad) del software.

**Criterio de Aceptacion**: Son las condiciones puntuales que un producto debe satisfacer para ser aceptado por un cliente. Es un item que marcar en una lista de requisitos.

**Escenario de Prueba**: Es un conjunto de pasos a efectuar bajo unas condiciones de un sistema, al cual se le tiene un resultado esperado. Es completamente diferente a los requerimientos y los criterios de aceptacion.

### 3. De dos ejemplos de requerimientos no-funcionales, y especifique cual es su categoría (seguridad, performance, portabilidad, etc.)
1. _Rápido_: se refiere a un programa que maneja correctamente los recursos, de forma que realiza sus procesos de forma rápida, optimizado a velocidad sobre memoria.
2. _Pequeño_: se refiere a un programa que puede ser ejecutado en aparatos con limitaciones de memoria (como sistemas incrustados), optimizado a memoria sobre velocidad.

### 4. ¿Qué es TDD?
_TDD_, por sus siglas en inglés _**T**est **D**riven **D**evelopment_ es un proceso de desarrollo de software que depende de que los requerimientos de software se conviertan en casos de prueba antes de que el programa esté completamente desarrollado, vigilando estas pruebas mientras se desarrolla el programa.

El ciclo TDD contiene 3 pasos:
1. Agrega una prueba de la nueva característica que se va a agregar.
2. Ejecute todas las pruebas; la prueba recien creada va a fallar por razones esperadas.
3. Escribe el codigo más simple que pase la prueba. No se debe crear mas codigo que el necesario.
4. Todas las pruebas deben pasar, si alguna falla, el codigo debe ser revisado hasta que la prueba funcione.
5. Reorganice el código para legibilidad y mantenibilidad. Despues de cada organizacion, todas las pruebas deben ser ejecutadas para confirmar que ninguna funcionalidad existente se haya roto.

### 5. ¿Que son pruebas unitarias automatizadas?
Una prueba unitaria es un método de prueba que prueba la validez de una parte minima de un programa, llamado unidad. Las unidades pueden ser aisladas lógicamente de un sistema. Las unidades, por lo tanto, son partes de un software como lo son funciones (o métodos) y subrutinas. Las pruebas unitarias automatizadas son las purebas unitarias que son ejecutadas por otro código: es hacer un programa para probar un programa.

Los programas que ayudan a realizar estas pruebas unitarias se llaman _unit testing frameworks_ o bien, marcos de pruebas unitarias.

### 6. ¿Cual fue el 1er framework de pruebas unitarias y para cual lenguaje fue creado?

SUnit para Smalltalk, creado por Kent Beck y publicado en 1989 en su publicación "Simple Smalltalk Testing: With Patterns" _(O diseñado en 1998, según otras fuentes)_. Varios _frameworks_ fueron basados en SUnit, su nombre colectivo es xUnit (porque sus nombres son tales como JUnit o RUnit).

### 7. ¿Describa los componentes de la arquitectura xUnit?
* **Test Runner**: Es un programa que ejecuta las pruebas implementadas y reporta los resultados de las pruebas.
* **Test Case**: Es una clase que representa un caso de prueba. Es la parte más pequeña de las pruebas.
* **Test Fixture**: (También conocido como contexto de prueba) son un conjunto de condiciones (o estado de programa) que se necesitan para lograr una prueba.
* **Test Suite**: Son un conjunto de pruebas que utilizan el mismo _Fixture_ (entorno). En este caso, el orden de las pruebas no debe importar.
* **Test Execution**: Es la ejecución de una prueba. Tiene 3 pasos generales:
  * Inicio: Se prepara el ámbito de prueba y se comprueba el Fixture; se prepara el mundo.
  * Body: Es el cuerpo de la prueba y todas las cosas a realizar. Se ensucia el mundo.
  * Teardown: Es el fin de la prueba, donde se deshacen los cambios que realizó la prueba. Se limpia el mundo.
* **Test Result Formatter**: Es la parte del programa que muestra los resultados de las pruebas, de una forma cómoda de entender para el programado.
* **Assertions**: Es una función que verifica el comportamiento o el estado de la unidad siendo probada. Representa una condición lógica que es verdadera si los resultados son los esperados (y falso si no, y suele lanzar una excepción).
### 8. Indique al menos tres desventajas de las pruebas unitarias automatizadas
* Hay más tiempo entre compilaciones y releases (porque hay que esperar las pruebas)
* Hay más tiempo en desarrollo (porque hay que escribir las pruebas)
* Es dificil probar interfaces gráficas.

### 9. Indique al menos tres ventajas de las pruebas unitarias automatizadas
* Los errores de código se encuentran más rápidamente (porque las pruebas se hacen en cada iteración).
* Se sabe si el código es correcto más rápidamente (te hace más eficiente).
* Ayuda a escribir mejor código (porque el código debe ser fácil de probar).

### 10. Tomando el algoritmo de conversión de números arábigos o "decimales" a números Romanos:

  * Cree un documento donde se listen los Requerimientos, Criterios de Aceptación y Casos de Prueba para una aplicación de consola

  * Los casos de prueba deben ser de dos categorías: End-To-End (desde el UI) y Unitarios (caja blanca, código, bajo nivel)

### 11. Utilizando el lenguaje de su preferencia cree cinco o mas casos de prueba unitarios automatizados utilizando un framework de automatización de pruebas para el algoritmo en cuestion