CREATE TABLE bilet( 
idbiletu INT(11) PRIMARY KEY, 
rzad VARCHAR(5), 
miejsce INT(10), 
idsali INT(11), 
cena DECIMAL(5,2), 
idfilmu INT(11), 
idklienta INT(11), 
godzinarozpoczecia DATETIME, 
typ VARCHAR(30), 
FOREIGN KEY (idfilmu) REFERENCES film(idfilmu) ON DELETE RESTRICT, 
FOREIGN KEY (idklienta) REFERENCES klient(idklienta) ON DELETE SET NULL ); 

CREATE TABLE kopiafilm SELECT * FROM tomzmi.film;

SELECT * FROM pracownik
WHERE (nazwisko LIKE "%e%" OR nazwisko LIKE "%o%") 
AND YEAR(dataZatrudnienia)<=2006
ORDER BY dataur DESC LIMIT 4;

SELECT klient.imie, klient.nazwisko, film.tytul FROM klient
NATURAL JOIN bilet NATURAL JOIN film
WHERE film.katwiekowa>YEAR(CURRENT_DATE()-dataur);

SELECT film.tytul, COUNT(bilet.idbiletu) FROM film
INNER JOIN bilet ON bilet.idfilmu=film.idfilmu
GROUP BY film.tytul
ORDER BY COUNT(bilet.idbiletu) DESC LIMIT 3;

INSERT INTO `klient` SELECT * FROM wikingowie.kreatura;
INSERT INTO `klient`(imie, nazwisko, cena) SELECT kreatura.nazwa, "wszedzie", kreatura.waga FROM wikingowie.kreatura;

SELECT GROUP_CONCAT(film.tytul," ",bilet.godzinarozpoczecia) 
FROM film NATURAL JOIN bilet
GROUP BY DATE(bilet.godzinarozpoczecia)
ORDER BY bilet.godzinarozpoczecia DESC;

SELECT imie, nazwisko FROM klient
WHERE idklienta NOT IN (SELECT DISTINCT idklienta FROM bilet);

SELECT film.tytul, AVG(bilet.cena) FROM film NATURAL JOIN bilet
GROUP BY film.tytul HAVING COUNT(bilet.idbiletu)>8;

SELECT pracownik.nazwisko, COUNT(sala.liczbamiejsc), COUNT(bilet.idbiletu) 
FROM pracownik NATURAL JOIN sala_pilnowanie NATURAL JOIN sala
NATURAL JOIN bilet
GROUP BY DATE(bilet.godzinarozpoczecia) 
HAVING YEAR(bilet.godzinarozpoczecia) = 2018 AND MONTH(bilet.godzinarozpoczecia) = 10;

