/*Display how many employees there are in each job in departments 1 and 6. 
Let the number of employees in the number_of_employees column. 
Add an additional column for city, (where the department is located), department name and job title. 
Record sort in ascending order by the number of employees.*/

SELECT D.department_name,E.job_id, count(*) as 'number_of_employees', CONCAT(L.city, ' ',D.department_name, ' ' ,E.job_id)
FROM employees as E
	left join departments as D on E.department_id=D.id
	left join locations as L on D.location_id=L.id
	left join jobs as J on J.id=E.job_id
WHERE E.department_id IN (1,6)
GROUP BY D.department_name,E.job_id, L.city
ORDER BY count(*);


/*Show all names beginning with the letter A, which are carried by at least two employees.
Additively write the number of employees in the number_of_employees column
Sort the records in descending order by the number of employees*/

SELECT first_name, count(first_name) as 'number_of_employees'
FROM employees
WHERE first_name like 'A%'
GROUP BY first_name
HAVING count(first_name)>1
ORDER BY count(first_name) desc;

/*Write out the names of departments located in Cracow with at least five employees. 
Additionally, record the number of employees in the number_of_employees column*/

SELECT D.department_name, count(*) as 'kolumnie number_of_employees'
FROM employees as E
	left join departments as D on E.department_id=D.id
	left join locations as L on D.location_id=L.id
WHERE L.city = 'Cracow'
GROUP BY D.department_name
HAVING count(*)>4;

--Write out the number of people working in departments 1-2 (describe as departments_1-2) 
--and in departments 3-6 (describe as departments_3-6)

SELECT sum(case when department_id in(1,2) then 1 else 0 end) as 'departments_1-2',
	   sum(case when department_id in(3, 4, 5, 6) then 1 else 0 end) as 'departments_3-6'
FROM employees;