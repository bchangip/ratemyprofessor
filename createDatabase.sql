-- DROP DATABASE ratemyprofessor;

-- CREATE DATABASE ratemyprofessor;

CREATE TABLE student (
	id INT,
	username VARCHAR(10),
	firstname VARCHAR(10),
	lastname VARCHAR(10),
	email VARCHAR(20),
	career VARCHAR(30),
	interests VARCHAR(15)[],
	highschool VARCHAR(40),

	CONSTRAINT student_pk PRIMARY KEY (id)
);

CREATE TABLE course (
	id INT,
	name VARCHAR(20),

	CONSTRAINT course_pk PRIMARY KEY (id)
);

CREATE TABLE professor (
	id INT,
	firstname VARCHAR(10),
	lastname VARCHAR(10),

	CONSTRAINT professor_pk PRIMARY KEY (id)
);

CREATE TABLE review (
	id INT,
	id_user INT,
	id_course INT,
	id_professor INT,
	rating INT,
	comment VARCHAR(200),

	CONSTRAINT review_pk PRIMARY KEY (id),
	CONSTRAINT review_user_fk FOREIGN KEY (id_user) REFERENCES student(id),
	CONSTRAINT review_course_fk FOREIGN KEY (id_course) REFERENCES course(id),
	CONSTRAINT review_professor_fk FOREIGN KEY (id_professor) REFERENCES professor(id)
);