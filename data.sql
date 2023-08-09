--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

-- Started on 2023-08-09 14:01:15

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

DROP DATABASE promptly;
--
-- TOC entry 3336 (class 1262 OID 50181)
-- Name: promptly; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE promptly WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';


ALTER DATABASE promptly OWNER TO postgres;

\connect promptly

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 50183)
-- Name: genres; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genres (
    id integer NOT NULL,
    name character varying,
    description character varying
);


ALTER TABLE public.genres OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 50182)
-- Name: genres_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.genres_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.genres_id_seq OWNER TO postgres;

--
-- TOC entry 3337 (class 0 OID 0)
-- Dependencies: 214
-- Name: genres_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.genres_id_seq OWNED BY public.genres.id;


--
-- TOC entry 217 (class 1259 OID 50192)
-- Name: prompts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.prompts (
    id integer NOT NULL,
    title character varying,
    content character varying,
    genre_id integer NOT NULL
);


ALTER TABLE public.prompts OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 50191)
-- Name: prompts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.prompts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.prompts_id_seq OWNER TO postgres;

--
-- TOC entry 3338 (class 0 OID 0)
-- Dependencies: 216
-- Name: prompts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.prompts_id_seq OWNED BY public.prompts.id;


--
-- TOC entry 3178 (class 2604 OID 50186)
-- Name: genres id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres ALTER COLUMN id SET DEFAULT nextval('public.genres_id_seq'::regclass);


--
-- TOC entry 3179 (class 2604 OID 50195)
-- Name: prompts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prompts ALTER COLUMN id SET DEFAULT nextval('public.prompts_id_seq'::regclass);


--
-- TOC entry 3328 (class 0 OID 50183)
-- Dependencies: 215
-- Data for Name: genres; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.genres (id, name, description) VALUES (1, 'Fantasy', 'A genre of fiction that features magical or supernatural elements');
INSERT INTO public.genres (id, name, description) VALUES (2, 'Horror', 'A genre of fiction that evokes fear, suspense, or dread');
INSERT INTO public.genres (id, name, description) VALUES (3, 'Romance', 'A genre of fiction that focuses on the relationship and romantic love between two or more characters');
INSERT INTO public.genres (id, name, description) VALUES (4, 'Sci-Fi', 'A genre of fiction that deals with imaginative and futuristic concepts such as advanced science, technology, or space exploration');
INSERT INTO public.genres (id, name, description) VALUES (5, 'Mystery', 'A genre of fiction that involves a crime, puzzle, or secret that needs to be solved');


--
-- TOC entry 3330 (class 0 OID 50192)
-- Dependencies: 217
-- Data for Name: prompts; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.prompts (id, title, content, genre_id) VALUES (1, 'The Dragons Egg', 'You find a dragon''s egg in the forest. What do you do with it?', 1);
INSERT INTO public.prompts (id, title, content, genre_id) VALUES (2, 'The Haunted House', 'You and your friends decide to spend a night in a haunted house. What happens?', 2);
INSERT INTO public.prompts (id, title, content, genre_id) VALUES (3, 'The Fake Wedding', 'You have to pretend to be married to someone you hate for a week. How do you cope?', 3);
INSERT INTO public.prompts (id, title, content, genre_id) VALUES (4, 'The Alien Invasion', 'Aliens have invaded Earth and are abducting humans. How do you survive?', 4);
INSERT INTO public.prompts (id, title, content, genre_id) VALUES (5, 'The Missing Painting', 'You are a detective hired to find a missing painting worth millions. Who stole it and why?', 4);
INSERT INTO public.prompts (id, title, content, genre_id) VALUES (6, 'The Magic School', 'You receive a letter inviting you to attend a school for magic. What do you learn there?', 1);
INSERT INTO public.prompts (id, title, content, genre_id) VALUES (7, 'The Zombie Apocalypse', 'The dead have risen and are attacking the living. How do you escape?', 2);
INSERT INTO public.prompts (id, title, content, genre_id) VALUES (8, 'The Blind Date', 'You agree to go on a blind date with someone you met online. What do they look like and how do they act?', 3);
INSERT INTO public.prompts (id, title, content, genre_id) VALUES (9, 'The Time Machine', 'You invent a time machine and decide to travel to the past or the future. Where do you go and what do you see?', 4);
INSERT INTO public.prompts (id, title, content, genre_id) VALUES (10, 'The Murder Mystery', 'You are invited to a dinner party where a murder takes place. Who is the killer and how do you catch them?', 5);
INSERT INTO public.prompts (id, title, content, genre_id) VALUES (11, 'The Fairy Tale', 'You are the main character of a fairy tale. What is your story and how does it end?', 1);
INSERT INTO public.prompts (id, title, content, genre_id) VALUES (12, 'The Nightmare', 'You have a recurring nightmare that seems to be trying to tell you something. What is it and what does it mean?', 2);
INSERT INTO public.prompts (id, title, content, genre_id) VALUES (13, 'The Love Triangle', 'You are in love with two people who are also in love with you. How do you choose between them?', 3);
INSERT INTO public.prompts (id, title, content, genre_id) VALUES (14, 'The Space Adventure', 'You are part of a crew on a spaceship exploring the galaxy. What do you encounter on your journey?', 4);
INSERT INTO public.prompts (id, title, content, genre_id) VALUES (15, 'The Secret Society', 'You discover that you belong to a secret society that has been hidden for centuries. What is their purpose and what do they want from you?', 5);


--
-- TOC entry 3339 (class 0 OID 0)
-- Dependencies: 214
-- Name: genres_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.genres_id_seq', 5, true);


--
-- TOC entry 3340 (class 0 OID 0)
-- Dependencies: 216
-- Name: prompts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.prompts_id_seq', 15, true);


--
-- TOC entry 3181 (class 2606 OID 50190)
-- Name: genres genres_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres
    ADD CONSTRAINT genres_pkey PRIMARY KEY (id);


--
-- TOC entry 3183 (class 2606 OID 50199)
-- Name: prompts prompts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prompts
    ADD CONSTRAINT prompts_pkey PRIMARY KEY (id);


--
-- TOC entry 3184 (class 2606 OID 50200)
-- Name: prompts prompts_genre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prompts
    ADD CONSTRAINT prompts_genre_id_fkey FOREIGN KEY (genre_id) REFERENCES public.genres(id);


-- Completed on 2023-08-09 14:01:15

--
-- PostgreSQL database dump complete
--

