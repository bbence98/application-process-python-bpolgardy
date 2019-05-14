DROP TABLE IF EXISTS applicants;
DROP TABLE IF EXISTS mentors;

CREATE TABLE applicants (
    id SERIAL PRIMARY KEY,
    first_name character varying(255) NOT NULL,
    last_name character varying(255) NOT NULL,
    phone_number character varying(100) NOT NULL,
    email character varying(255) NOT NULL,
    application_code integer UNIQUE NOT NULL
);

CREATE TABLE mentors (
    id SERIAL PRIMARY KEY,
    first_name character varying(255) NOT NULL,
    last_name character varying(255) NOT NULL,
    nick_name character varying(255),
    phone_number character varying(100) NOT NULL,
    email character varying(255) NOT NULL,
    city character varying(255) NOT NULL,
    favourite_number integer
);

INSERT INTO applicants VALUES (1, 'Dominique', 'Williams', '003630/734-4926', 'dolor@laoreet.co.uk', 61823);
INSERT INTO applicants VALUES (2, 'Jemima', 'Foreman', '003620/834-6898', 'magna@etultrices.net', 58324);
INSERT INTO applicants VALUES (3, 'Zeph', 'Massey', '003630/216-5351', 'a.feugiat.tellus@montesnasceturridiculus.co.uk', 61349);
INSERT INTO applicants VALUES (4, 'Joseph', 'Crawford', '003670/923-2669', 'lacinia.mattis@arcu.co.uk', 12916);
INSERT INTO applicants VALUES (5, 'Ifeoma', 'Bird', '003630/465-8994', 'diam.duis.mi@orcitinciduntadipiscing.com', 65603);
INSERT INTO applicants VALUES (6, 'Arsenio', 'Matthews', '003620/804-1652', 'semper.pretium.neque@mauriseu.net', 39220);
INSERT INTO applicants VALUES (7, 'Jemima', 'Cantu', '003620/423-4261', 'et.risus.quisque@mollis.co.uk', 10384);
INSERT INTO applicants VALUES (8, 'Carol', 'Arnold', '003630/179-1827', 'dapibus.rutrum@litoratorquent.com', 70730);
INSERT INTO applicants VALUES (9, 'Jane', 'Forbes', '003670/653-5392', 'janiebaby@adipiscingenimmi.edu', 56882);
INSERT INTO applicants VALUES (10, 'Ursa', 'William', '003620/496-7064', 'malesuada@mauriseu.net', 91220);
SELECT pg_catalog.setval('applicants_id_seq', 10, true);


INSERT INTO mentors VALUES
  (2, 'Pál', 'Monoczki', 'Pali', '003630/327-2663', 'pal.monoczki@codecool.com', 'Miskolc', NULL),
  (3, 'Sándor', 'Szodoray', 'Szodi', '003620/519-9152', 'sandor.szodoray@codecool.com', 'Miskolc', 7),
  (4, 'Dániel', 'Salamon', 'Dani', '003620/508-0706', 'daniel.salamon@codecool.com', 'Budapest', 4),
  (5, 'Miklós', 'Beöthy', 'Miki', '003630/256-8118', 'miklos.beothy@codecool.com', 'Budapest', 42),
  (6, 'Tamás', 'Tompa', 'Tomi', '003630/370-0748', 'tamas.tompa@codecool.com', 'Budapest', 42),
  (7, 'Mateusz', 'Ostafil', 'Mateusz', '003648/518-664-923', 'mateusz.ostafil@codecool.com', 'Krakow', 13),
  (8, 'Anikó', 'Fenyvesi', 'Anikó', '003670/111-2222', 'aniko.fenyvesi@codecool.com', 'Budapest', 11),
  (9, 'Immánuel', 'Fodor', 'Immi', '003620/123-6234', 'immanuel.fodor@codecool.com', 'Budapest', 3),
  (10, 'László', 'Molnár', 'Laci', '003620/222-5566', 'laszlo.molnar@codecool.com', 'Budapest', 5),
  (11, 'Mátyás', 'Forián Szabó', 'Matyi', '003630/111-5532', 'matyas.forian.szabo@codecool.com', 'Budapest', 90),
  (12, 'Zoltán', 'Sallay', 'Zozi', '003670/898-3122', 'zoltan.sallay@codecool.com', 'Budapest', 5),
  (13, 'Szilveszter', 'Erdős', 'Sly', '003620/444-5555', 'szilveszter.erdos@codecool.com', 'Budapest', 13),
  (14, 'László', 'Terray', 'Laci', '003670/402-2435', 'laszlo.terray@codecool.com', 'Budapest', 8),
  (15, 'Árpád', 'Törzsök', 'Árpád', '003630/222-1221', 'arpad.torzsok@codecool.com', 'Budapest', 9),
  (16, 'Imre', 'Lindi', 'Imi', '003670/222-1233', 'imre.lindi@codecool.com', 'Miskolc', 3),
  (17, 'Róbert', 'Kohányi', 'Robi', '003630/123-5553', 'robert.kohanyi@codecool.com', 'Miskolc', NULL),
  (18, 'Przemysław', 'Ciąćka', 'Przemek', '003670/222-4554', 'przemyslaw.ciacka@codecool.com', 'Krakow', 55),
  (19, 'Marcin', 'Izworski', 'Marcin', '003670/999-2323', 'marcin.izworski@codecool.com', 'Krakow', 55),
  (20, 'Rafał', 'Stępień', 'Rafal', '003630/323-5343', 'rafal.stepien@codecool.com', 'Krakow', 3),
  (21, 'Agnieszka', 'Koszany', 'Agi', '003630/111-5343', 'agnieszka.koszany@codecool.com', 'Krakow', 77),
  (22, 'Mateusz', 'Steliga', 'Mateusz', '003630/123-5343', 'mateusz.steliga@codecool.com', 'Krakow', 5),
  (23, 'Bence', 'Fábián', 'Benec', '003620/123-7654', 'bence.fabian@codecool.com', 'Budapest', NULL),
  (1, 'Attila', 'Molnár', 'Atesz', '003670/630-0539', 'attila.molnar@codecool.com', 'Budapest', 23);

SELECT pg_catalog.setval('mentors_id_seq', 22, true);
