--
-- PostgreSQL database dump
--

-- Dumped from database version 12.19 (Ubuntu 12.19-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.19 (Ubuntu 12.19-0ubuntu0.20.04.1)

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
-- Name: posts; Type: TABLE; Schema: public; Owner: mike
--

CREATE TABLE public.posts (
    id integer NOT NULL,
    title character varying(50) NOT NULL,
    content character varying NOT NULL,
    created_at timestamp without time zone NOT NULL,
    user_id integer
);


ALTER TABLE public.posts OWNER TO mike;

--
-- Name: posts_id_seq; Type: SEQUENCE; Schema: public; Owner: mike
--

CREATE SEQUENCE public.posts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.posts_id_seq OWNER TO mike;

--
-- Name: posts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mike
--

ALTER SEQUENCE public.posts_id_seq OWNED BY public.posts.id;


--
-- Name: posts_tags; Type: TABLE; Schema: public; Owner: mike
--

CREATE TABLE public.posts_tags (
    post_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.posts_tags OWNER TO mike;

--
-- Name: tags; Type: TABLE; Schema: public; Owner: mike
--

CREATE TABLE public.tags (
    id integer NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.tags OWNER TO mike;

--
-- Name: tags_id_seq; Type: SEQUENCE; Schema: public; Owner: mike
--

CREATE SEQUENCE public.tags_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tags_id_seq OWNER TO mike;

--
-- Name: tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mike
--

ALTER SEQUENCE public.tags_id_seq OWNED BY public.tags.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: mike
--

CREATE TABLE public.users (
    id integer NOT NULL,
    first_name character varying(25) NOT NULL,
    last_name character varying(25) NOT NULL,
    image_url character varying NOT NULL
);


ALTER TABLE public.users OWNER TO mike;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: mike
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO mike;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mike
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: posts id; Type: DEFAULT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.posts ALTER COLUMN id SET DEFAULT nextval('public.posts_id_seq'::regclass);


--
-- Name: tags id; Type: DEFAULT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.tags ALTER COLUMN id SET DEFAULT nextval('public.tags_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: mike
--

COPY public.posts (id, title, content, created_at, user_id) FROM stdin;
6	I have a secret	im spider-man	2024-07-15 22:31:56.863239	4
7			2024-07-15 23:05:11.590327	4
9	d		2024-07-15 23:05:32.446248	4
8	Im spider	Look im a spider	2024-07-15 23:05:20.377593	4
3	I'm Not a Ghost	Im danny	2024-07-15 22:19:26.290674	\N
4	Fought a ghost	it was really scary	2024-07-15 22:21:59.465291	\N
5			2024-07-15 22:31:09.633985	\N
1	My First Post	Hi guys this is my first post	2024-07-15 22:09:58.145347	\N
\.


--
-- Data for Name: posts_tags; Type: TABLE DATA; Schema: public; Owner: mike
--

COPY public.posts_tags (post_id, tag_id) FROM stdin;
\.


--
-- Data for Name: tags; Type: TABLE DATA; Schema: public; Owner: mike
--

COPY public.tags (id, name) FROM stdin;
1	spider
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: mike
--

COPY public.users (id, first_name, last_name, image_url) FROM stdin;
4	Peter	Parker	
6	Paul	Blart	
7	Kim	Possible	
10	Bill	Cipher	https://www.freeiconspng.com/uploads/name-people-person-user-icon--icon-search-engine-1.png
11	asda	asdas	https://www.freeiconspng.com/uploads/name-people-person-user-icon--icon-search-engine-1.png
\.


--
-- Name: posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mike
--

SELECT pg_catalog.setval('public.posts_id_seq', 10, true);


--
-- Name: tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mike
--

SELECT pg_catalog.setval('public.tags_id_seq', 1, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mike
--

SELECT pg_catalog.setval('public.users_id_seq', 12, true);


--
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (id);


--
-- Name: posts_tags posts_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.posts_tags
    ADD CONSTRAINT posts_tags_pkey PRIMARY KEY (post_id, tag_id);


--
-- Name: tags tags_name_key; Type: CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_name_key UNIQUE (name);


--
-- Name: tags tags_pkey; Type: CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: posts_tags posts_tags_post_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.posts_tags
    ADD CONSTRAINT posts_tags_post_id_fkey FOREIGN KEY (post_id) REFERENCES public.posts(id);


--
-- Name: posts_tags posts_tags_tag_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.posts_tags
    ADD CONSTRAINT posts_tags_tag_id_fkey FOREIGN KEY (tag_id) REFERENCES public.tags(id);


--
-- Name: posts posts_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: mike
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

