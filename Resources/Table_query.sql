drop table if exists business;
create table business (latitude VARCHAR,
longitude VARCHAR,
business_id VARCHAR primary key,
address VARCHAR,
business_name VARCHAR,
business_type VARCHAR,
community_id FLOAT
)

SELECT *
FROM business


drop table if exists community;
create table community (community_id FLOAT,
community_name VARCHAR,
community_no VARCHAR,
global_id VARCHAR
)

SELECT *
FROM community


ALTER TABLE community ADD PRIMARY KEY (community_id);

ALTER TABLE ONLY business
    ADD CONSTRAINT community_id_fkey FOREIGN KEY(community_id)
REFERENCES community(community_id) ON UPDATE CASCADE;