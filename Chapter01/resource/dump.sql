BEGIN TRANSACTION;
CREATE TABLE users (id INTEGER PRIMARY KEY, username text,     email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'Kim','Kim@naver.com','010-0000-0000','kim.com','2022-07-23 18:54:06');
INSERT INTO "users" VALUES(2,'Park','Park@daum.net','010-1111-1111','Park.com','2022-07-23 18:54:06');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.net','010-2222-2222','Lee.com','2022-07-23 18:54:06');
INSERT INTO "users" VALUES(4,'Cho','Cho@daum.net','010-3333-3333','Cho.com','2022-07-23 18:54:06');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@google.net','010-4444-4444','Yoo.com','2022-07-23 18:54:06');
COMMIT;
