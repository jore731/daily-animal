# Setup Inicial

## 1. Crear una Cuenta en GitHub

1. Accede a la página principal de [Github](https://github.com).
2. En la página principal, haz clic en el botón **Sign up** (Registrarse) ubicado en la esquina superior derecha.
3. Ingresa tu **dirección de correo electrónico**, **nombre de usuario** y **contraseña**.
4. Haz clic en el botón **Continue** (Continuar).
5. Completa el desafío de verificación de seguridad (captcha) para demostrar que no eres un robot.
6. Revisa el correo electrónico de verificación enviado por GitHub a la cuenta proporcionada.
7. Haz clic en el enlace de verificación dentro del correo electrónico o introduce el código en el campo correspondiente en el navegador.
8. Una vez verificado el email, vuelve a iniciar sesión con tus datos para confirmar que el registro se ha completado con éxito.

## 2. Crea una cuenta en Streamlit Cloud

1. Accede a la página de inicio de [Streamlit](https://authkit.streamlit.io)
2. Pulsa el botón `Continue with Github`
3. Si fuera necesario, inicia sesión con la cuenta creada anteriormente
4. Si fuera necesario, verifica nuevamente el correo electrónico intoduciendo el código recibido.
5. En caso de que pida permisos de Github, hacer click en `Authorize`
6. Completar el formulario con los datos correspondientes para cada caso.

## 3. Crear repositorio en Github

> [!NOTE]
> Utilizaremos de forma muy básica _Git_ y _Github_ dado el alcance de la sesión. Para obtener más información sobre repositorios _Git_ recomendamos el siguiente [vídeo](https://www.youtube.com/watch?v=2nYUyP7l7zg)

A continuación, utilizaremos **Github** para almacenar nuestro trabajo. Para ello, crearemos un **repositorio**.

Un **repositorio** nos permitirá guardar el código de forma que podamos colaborar con los demás y mantener organizado nuestro código, así como tener un registro de las distintas versiones y cambios que hacemos.

Para crear un repositorio nuevo tenemos dos opciones, iniciar un repositorio vacío, o partir de un repositorio existente y hacer una copia del mismo.
En nuestro caso, partiremos de una plantilla de modo que:

1. Accedemos a la [plantilla](https://github.com/jore731/daily-animal)
2. Hacemos click en el botón verde de la parte superior que dice `Use this template` y seleccionamos la opción `create a new repository`.
3. Introducimos un nombre para el repositorio que queremos crear (podemos utilizar el nombre sugerido por Github más abajo).
4. Esperamos a que el repositorio esté creado.

## 4. Registrar el repositorio de la nueva aplicación en Streamlit Cloud

Una vez que tenemos las cuentas y el repositorio creados, solo nos faltaría registrar el nuevo repositorio en la cuenta de Streamlit.

1. Abrir de nuevo Streamlit Cloud.
2. Pulsar el botón de la esquina superior derecha `Create app`
3. Seleccionar la opción `Deploy a public app from Github`
4. En el campo repository, seleccionaremos el repositorio creado (al hacer click en el campo de texto nos debería aparecer un desplegable)
5. Elegir, si queremos, un `App URL` para poder acceeder a la aplicación desde otros dispositivos.
6. Hacemos click en `Deploy`...

Y LISTO! Ya tendremos nuestra primera web app creada con Streamlit!

</details>
