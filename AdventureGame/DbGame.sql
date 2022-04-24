--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: characters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.characters (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    hp integer NOT NULL,
    damage integer NOT NULL,
    agility integer NOT NULL,
    intelligence integer NOT NULL,
    speed integer NOT NULL
);


ALTER TABLE public.characters OWNER TO postgres;

--
-- Name: enemies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.enemies (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    hp integer NOT NULL,
    attack integer NOT NULL,
    dodge integer NOT NULL
);


ALTER TABLE public.enemies OWNER TO postgres;

--
-- Name: main; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.main (
    id integer NOT NULL,
    id_user integer NOT NULL,
    id_character integer NOT NULL,
    id_weapon integer NOT NULL,
    date date NOT NULL,
    gold integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.main OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    password character varying(100) NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: weapons; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.weapons (
    id integer NOT NULL,
    id_character integer NOT NULL,
    name character varying(100) NOT NULL,
    attack integer NOT NULL,
    speed_attack integer NOT NULL,
    weight real
);


ALTER TABLE public.weapons OWNER TO postgres;

--
-- Name: characters characters_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.characters
    ADD CONSTRAINT characters_pkey PRIMARY KEY (id);


--
-- Name: main main_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main
    ADD CONSTRAINT main_pkey PRIMARY KEY (id);


--
-- Name: enemies monsters_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enemies
    ADD CONSTRAINT monsters_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: weapons weapons_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.weapons
    ADD CONSTRAINT weapons_pkey PRIMARY KEY (id);


--
-- Name: main fk_character; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main
    ADD CONSTRAINT fk_character FOREIGN KEY (id_character) REFERENCES public.characters(id);


--
-- Name: weapons fk_id_character; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.weapons
    ADD CONSTRAINT fk_id_character FOREIGN KEY (id_character) REFERENCES public.characters(id);


--
-- Name: main fk_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main
    ADD CONSTRAINT fk_user FOREIGN KEY (id_user) REFERENCES public.users(id);


--
-- Name: main fk_weapon; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.main
    ADD CONSTRAINT fk_weapon FOREIGN KEY (id_weapon) REFERENCES public.weapons(id);


--
-- PostgreSQL database dump complete
--

-- Characters
INSERT INTO public.characters (id, name, hp, damage, agility, intelligence, speed) VALUES (1, 'Warrior', 120, 100, 60, 20, 30);
INSERT INTO public.characters (id, name, hp, damage, agility, intelligence, speed) VALUES (2, 'Wizard', 60, 140, 20, 100, 20);
INSERT INTO public.characters (id, name, hp, damage, agility, intelligence, speed) VALUES (3, 'Archer', 80, 120, 80, 60, 50);

-- Weapons
INSERT INTO public.weapons (id, id_character, name, attack, speed_attack, weight) VALUES (1, 1, 'sword', 100, 50, 1.35);
INSERT INTO public.weapons (id, id_character, name, attack, speed_attack, weight) VALUES (2, 1, 'axe', 80, 60, 0.95);
INSERT INTO public.weapons (id, id_character, name, attack, speed_attack, weight) VALUES (3, 1, 'spear', 110, 40, 1);
INSERT INTO public.weapons (id, id_character, name, attack, speed_attack, weight) VALUES (4, 2, 'fire_wand', 200, 10, 0.2);
INSERT INTO public.weapons (id, id_character, name, attack, speed_attack, weight) VALUES (5, 2, 'wind_wand', 50, 100, 0.1);
INSERT INTO public.weapons (id, id_character, name, attack, speed_attack, weight) VALUES (6, 2, 'lighting_wand', 100, 50, 0.2);
INSERT INTO public.weapons (id, id_character, name, attack, speed_attack, weight) VALUES (7, 3, 'short_bow', 100, 50, 0.5);
INSERT INTO public.weapons (id, id_character, name, attack, speed_attack, weight) VALUES (8, 3, 'long_bow', 150, 20, 0.85);
INSERT INTO public.weapons (id, id_character, name, attack, speed_attack, weight) VALUES (9, 3, 'crossbow', 200, 10, 1.2);

-- Enemies
INSERT INTO public.enemies (id, name, hp, attack, dodge) VALUES (1, 'Troll', 1000, 20, 0);
INSERT INTO public.enemies (id, name, hp, attack, dodge) VALUES (4, 'Zombie', 2000, 5, 0);
INSERT INTO public.enemies (id, name, hp, attack, dodge) VALUES (6, 'Blacksmith', 400, 15, 20);
INSERT INTO public.enemies (id, name, hp, attack, dodge) VALUES (3, 'Wraith', 200, 40, 70);
INSERT INTO public.enemies (id, name, hp, attack, dodge) VALUES (2, 'Wolf', 100, 10, 30);
INSERT INTO public.enemies (id, name, hp, attack, dodge) VALUES (5, 'Rat', 50, 5, 50);
INSERT INTO public.enemies (id, name, hp, attack, dodge) VALUES (7, 'Mercenary', 200, 10, 20);
INSERT INTO public.enemies (id, name, hp, attack, dodge) VALUES (8, 'Huntress', 250, 30, 55);
INSERT INTO public.enemies (id, name, hp, attack, dodge) VALUES (9, 'Bandits', 100, 10, 10);
INSERT INTO public.enemies (id, name, hp, attack, dodge) VALUES (10, 'Armed Villagers', 50, 5, 10);

-- Test user
INSERT INTO public.users (id, name, password) VALUES (1, 'test', '123');