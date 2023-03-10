# Requerimientos.

Para la instalacion de la API se necesita Docker.

La imagen

```sh
# Construimos nuestra imagen
docker build -t api-challenge-image .
```

y levantamos el contenedor

```sh
# Levantamos el contenedor
docker run -p 5000:5000 api-challenge-image
```

Por defecto la API se monta en el puerto 5000 (configurable como variable de entorno ``API_PORT``). Con el comando
de arriba hicimos el mapeo de puertos, y ahora podrás visualizar la aplicación en ``http://localhost:5000/``

Esta aplicación es un *hello world* que simula un escenario real de comunicación de modelos con API REST. El directorio
``model_environments``, en este ejemplo contiene una colección de modelos binarios (en formato pickle) y un simple
archivo de ``requirements.txt`` que nos entrega la información del ambiente en que se puede desplegar el modelo. En un escenario
profesional, los binarios vivirían en un Bucket (por ejemplo AWS S3) y los requerimientos serían un poco más complejos, por ejemplo,
el ambiente del modelo podría ser un instalable python desde un artefactory propio.


# Procedimiento.

Se propuso el modelo catboost el cual no obtuvo un gran mejor resultado y tambien se dejaron los modelos previamente realizados por el notebook. Los modelos que se pueden seleccionar para predecir son los siguientes:

-logistic_model
-xgboost_model
-catboost_model
-xgboost_fI_model
-catboost_fI_model

El como se guardo el modelo en un objeto pickle, esta agregado en el notebook del data scientist.

# Por hacer.

- Pruebas de integracion/unitarias.
- Manejos de excepciones.
- Levantamiento de estado http statuscode