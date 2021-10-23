-- Table: public.tweet_timeline

-- DROP TABLE public.tweet_timeline;

CREATE TABLE IF NOT EXISTS public.tweet_timeline
(
    auth_location text COLLATE pg_catalog."default",
    author text COLLATE pg_catalog."default",
    created_date bigint,
    tweet_id_str text COLLATE pg_catalog."default" NOT NULL,
    tweet_lang text COLLATE pg_catalog."default",
    tweet_text text COLLATE pg_catalog."default",
    system_time bigint DEFAULT date_part('epoch'::text, now())
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.tweet_timeline
    OWNER to postgres;