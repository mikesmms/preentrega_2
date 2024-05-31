# Padel Rank

Comision: 54140

Alumno: Michael Simmons

## Objetivos del Proyecto:
Web para llevar el seguimiento de partidos de padel jugados con amigos.

## Explicacion Tecnica:
1. App Core
Continee un template Base y un template index. Los Blocks de Base se heredan en todo el resto. 
2. App Partidos
Contine create y list para cada uno de Torneos, Partidos, Jugadores.

## Mejoras Futuras:
Tablas para cada template, en lugar de lista para mejor visualizacion de los datos
Promedios y ranking.
Detail page por cada jugador.

## Problemas Conocidos:
Nombre de App Partidos no tiene sentido, ya que incluye no solo Partidos sino que tambien Jugadores, y Torneos.
Date field de fecha de nacimiento no se visualiza bien en el HTML a la hora de crear jugadores.
No parece tener sentido el template index de la App Partidos. El Index de core podria directamente redirigir a cada una de Partidos_list, Jugadores_list, Torneos_list





-----------------------------

🕵️ Cumplimiento de consigna:

💫 Entrega hecha por GitHub

💫 Readme con la explicación del proyecto

💫 Video de no más de 10 minutos

🕵️ Estructura interna:

💫 una o más aplicaciones creadas

💫 dos modelos con campos de texto, número, fecha

💫 vista de listado de registros de un modelo

💫 vista del detalle de un registro de un modelo

💫 vista para crear un registro de un modelo

💫 vista para eliminar un registro de un modelo

💫 about/ que hable sobre el creador del proyecto

🕵️ Lógica de usuarios:

💫 login de usuario

💫 registro de usuario

💫 administrador: puede realizar CRUD sobre los modelos

💫 administrador: subir una imagen de perfil para un usuario

🕵️ Flujo del proyecto

💫 Ingresar a la web app desde la ruta base ‘/’ y direccionar a “home”

💫 navegar entre las diferentes URL sin tener que usar la “barra del navegador”