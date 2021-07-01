# SageMaker

---

## Motivación

Los Científicos de datos en su día a día deben construir modelos predictivos con el objetivo de responder una pregunta de negocio. En muchas ocasiones se necesita iterar de manera rápida para tener resultados más rápidos y adicional confiables.

SageMaker es un servicio administrado por Amazon Web Services (AWS) que no permite iterar rápidamente para entrenar, evaluar y desplegar modelos predictivos.

---

### Pasos a seguir

Lo primero que necesitamos es tener instalado en nuestra máquina local **AWS CLI**, para interactuar desde nuestro PC con los servicios de AWS. Si tienes un pc con sistema operativo Windows este link te puede servir: [AWS CLI](https://docs.aws.amazon.com/es_es/cli/latest/userguide/install-cliv2-windows.html)

**Nota**: Cabe aclarar que ya necesitamos tener una cuenta creada de AWS

Después de tener instalado el AWS CLI, y tener a la mano las credenciales de seguridad, procedemos a configurar el CLI, para eso en nuestra terminal ejecutamos lo siguiente:

```
aws configure
```

Con lo anterior puedes colocar tu **AWS ACCESS KEY ID** y **AWS SECRET ACCESS KEY** y la región por defecto en la que vamos a trabajar.

Después de tenerlo configurado, desde nuestra máquina podemos ejecutar el siguiente comando en la terminal del proyecto:

```
python split_data.py
```

El código anterior ejecuta la siguiente lógica:

* Descarga el set de datos de un bucket de S3.
* Carga el set de datos y parte en entrenamiento, validación y datos "nuevos". Estos últimos con el objetivo de emular predicciones sobre datos nuevos.
* Une nuevamente los set de datos de entrenamiento y validación con su respetiva variable objetivo. Acá la variable objetivo debe ir en la primera posición, daod que SageMaker lo requiere de esta manera, aunque es flexible por si no se le proporciona de esa manera.
* Finalmente carga los set de datos al bucket ya listos para que Amazon SageMaker los use para hacer los respectivos entrenamientos.

Después de esto, podemos ir a verificar que los datos queden en S3 donde definimos que van a quedar. Y podemos iniciar una instancia de SageMaker para desarrollar el notebook `pre-built.ipynb`.