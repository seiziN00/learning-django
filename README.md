# Practice

This is the first practice of my Django learning process.

#### English

You are a Backend Developer assigned to a management software project for a multinational company.

You're in charge of implementing a new Django application to manage our global workforce data.

Your task is to design the backend logic to track employee records, including their national ID, full name, email, address, job title, and assigned location (factory).

Keep in mind the following requirements for the data architecture:

- Job Roles: Each role must include a job description and title.
- Compensation: Salaries are linked to one or more roles. You need to store the gross annual salary and a boolean flag to indicate if they are eligible for extra pay cycles (Summer and Christmas bonuses in June/December).
- Work Sites: Factories require a name, street address, zip code, and city.
- Geography: Cities must be grouped and mapped by Country.

Please ensure the relationships between models are properly defined.

---

#### Español

Eres el encargado de implementar el backend de una aplicación de gestión de empleados para una multinacional.

Esta aplicación debe llevar el control de cada empleado:

- DNI
- Nombre
- Email
- Dirección
- Puesto de trabajo
- Ubicación (fábrica en la que trabaja)

El puesto de trabajo siempre tiene una descripción de cargo y el cargo, además de los salarios, los salarios pueden pertenecer a uno o diferentes puesto de trabajo y siempre incluyen el bruto anual a cobrar y si tienen o no tienen asociada una paga extra en junio y en diciembre (paga de verano y navidad respectivamente).

Las ubicaciones donde los empleados trabajan serán ubicaciones donde:
- Se registran nombre de fábrica
- Dirección
- Código postal
- Población a la que pertenece

Esta "población" estarán agrupadas por país.