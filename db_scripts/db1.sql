CREATE USER dbfirst IDENTIFIED BY "ATP_password";

GRANT CREATE SESSION TO dbfirst;
GRANT CREATE TABLE TO dbfirst;
GRANT CREATE SEQUENCE TO dbfirst;
GRANT UNLIMITED TABLESPACE TO dbfirst;

CREATE TABLE "DBFIRST"."DEPT" (
  given_name  VARCHAR2(100) NOT NULL
);

INSERT INTO "DBFIRST"."DEPT"
VALUES ('Hello world! This message is stored in Oracle database.');

commit;
exit;
