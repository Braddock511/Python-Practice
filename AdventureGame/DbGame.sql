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
-- Name: main; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.main (
    id integer NOT NULL,
    id_user integer NOT NULL,
    id_character integer NOT NULL,
    id_weapon integer NOT NULL,
    date date NOT NULL
);


ALTER TABLE public.main OWNER TO postgres;

--
-- Name: monsters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monsters (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    hp integer NOT NULL,
    attack integer NOT NULL,
    dodge integer NOT NULL
);


ALTER TABLE public.monsters OWNER TO postgres;

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
-- Name: monsters monsters_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters
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

