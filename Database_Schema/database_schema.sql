create table access_token_tab
(
    id           bigint auto_increment
        primary key,
    access_token varchar(500) default '' not null,
    expiry_time  int          default 0  not null,
    user_id      int                     not null,
    created_time int                     not null,
    updated_time int                     not null,
    constraint idx_user_id
        unique (user_id)
);

create table group_tab
(
    id           bigint auto_increment
        primary key,
    group_name   varchar(200)      not null,
    is_deleted   tinyint default 0 not null,
    created_time int               not null,
    updated_time int               not null
);

create table group_team_tab
(
    id           bigint auto_increment
        primary key,
    group_id     int not null,
    team_id      int not null,
    created_time int not null,
    constraint idx_group_id_team_id
        unique (group_id, team_id)
);

create index idx_team_id
    on group_team_tab (team_id);

create table role_tab
(
    id           bigint auto_increment
        primary key,
    role_name    varchar(50) not null,
    alias        varchar(50) not null,
    created_time int         not null,
    updated_time int         not null
);

create index idx_alias
    on role_tab (alias);

create table team_tab
(
    id           bigint auto_increment
        primary key,
    team_name    varchar(200)      not null,
    is_deleted   tinyint default 0 not null,
    created_time int               not null,
    updated_time int               not null
);

create table user_group_tab
(
    id           bigint auto_increment
        primary key,
    user_id      int not null,
    group_id     int not null,
    created_time int not null,
    constraint idx_user_id_group_id
        unique (user_id, group_id)
);

create table user_role_tab
(
    id           bigint auto_increment
        primary key,
    user_id      int not null,
    role_id      int not null,
    created_time int not null,
    constraint idx_user_id_role_id
        unique (user_id, role_id)
);

create table user_tab
(
    id           bigint auto_increment
        primary key,
    username     varchar(50)       not null,
    password     varchar(200)      not null,
    email        varchar(50)       null,
    phone        varchar(15)       not null,
    is_deleted   tinyint default 0 null,
    created_by   int               not null,
    created_time int               not null,
    updated_time int               not null,
    constraint user_tab_username_uindex
        unique (username)
);

create index idx_is_deleted_username_email_phone
    on user_tab (is_deleted, username, email, phone);

create table user_team_tab
(
    id           bigint auto_increment
        primary key,
    user_id      int not null,
    team_id      int not null,
    created_time int not null,
    constraint idx_user_id_team_id
        unique (user_id, team_id)
);


INSERT INTO TechBaseVN.user_tab (username, password, email, phone, is_deleted, created_by, created_time, updated_time) VALUES ('user_1', '$2b$12$tsqQZDYUCdbSeJHwWzv3DOc8rRGqoSjcnnP/7PkogdD9kyipU7uW2', 'user_1@abc.com', '070432786', 0, -1, 1616475354, 1616475354);
INSERT INTO TechBaseVN.user_tab (username, password, email, phone, is_deleted, created_by, created_time, updated_time) VALUES ('user_2', '$2b$12$HT35hQLqhApGOmP5Sk/zZOjGrMLg.8wtod25H2UubvVPeLMm4oTMC', 'user_2@abc.com', '070432780', 0, -1, 1616482480, 1616482480);
INSERT INTO TechBaseVN.user_tab (username, password, email, phone, is_deleted, created_by, created_time, updated_time) VALUES ('user_3', '$2b$12$r49GmYQfoufWX9WUxtH8Re5GKUBdbQgavwbbUD0vJ65Mh8X/IFzEW', 'user_3@abc.com', '070432781', 0, -1, 1616482489, 1616482489);
INSERT INTO TechBaseVN.user_tab (username, password, email, phone, is_deleted, created_by, created_time, updated_time) VALUES ('user_4', '$2b$12$gRLTSlMC9PQ.IfZ8MZW4Zu1Woh45OMpWjxiv.rn/Jn/9VW27l9L0i', 'user_4@abc.com', '070432782', 0, -1, 1616482508, 1616482508);
INSERT INTO TechBaseVN.user_tab (username, password, email, phone, is_deleted, created_by, created_time, updated_time) VALUES ('user_5', '$2b$12$JoAAiVGStvZM.H64RD5d3.OVhnj5i5yrkMfv47JREssI1NqiH00/K', 'user_5@abc.com', '070432783', 0, -1, 1616482546, 1616482546);
INSERT INTO TechBaseVN.user_tab (username, password, email, phone, is_deleted, created_by, created_time, updated_time) VALUES ('user_6', '$2b$12$hn2qKxPuOkLjT81DwokkS.1Vfghb9UTPPjUPDoSkHrl3zrbGWX2Si', 'user_6@abc.com', '070432784', 0, -1, 1616482559, 1616482559);
INSERT INTO TechBaseVN.user_tab (username, password, email, phone, is_deleted, created_by, created_time, updated_time) VALUES ('user_7', '$2b$12$g058NhxZXx4vrfGpwWD7euRi4XxrM.qewpVDWzYo1o6DqTHfkUsY2', 'user_7@abc.com', '070432785', 0, -1, 1616482620, 1616482620);
INSERT INTO TechBaseVN.user_tab (username, password, email, phone, is_deleted, created_by, created_time, updated_time) VALUES ('user_8', '$2b$12$lRRzRvTNifHeVB5FbkwOXeG1fO9PK.wgLAQg/ctsehu8C731BuduO', 'user_8@abc.com', '070432787', 0, -1, 1616482630, 1616482630);
INSERT INTO TechBaseVN.user_tab (id, username, password, email, phone, is_deleted, created_by, created_time, updated_time) VALUES ('user_9', '$2b$12$ww6faMIAwRvTx/ifpsBFKuG06a0DMLdsCc1dICwgYzUD9c72cM9Zu', 'user_9@abc.com', '070432788', 0, -1, 1616482642, 1616482642);
INSERT INTO TechBaseVN.user_tab (username, password, email, phone, is_deleted, created_by, created_time, updated_time) VALUES ('user_10', '$2b$12$8QJxHxJjAcriOAhngiHhz.L.GPzZ/Nz6O.fFYQraFczq3iz80YZ.K', 'user_10@abc.com', '070432789', 0, -1, 1616482655, 1616482655);
INSERT INTO TechBaseVN.user_tab (username, password, email, phone, is_deleted, created_by, created_time, updated_time) VALUES ('user_11', '$2b$12$Z80bQtMZHCAwWt6N.kuyje9DYu0zeRXLhe2m8NF0VlOaWZQq2WlNy', 'user_11@abc.com', '070432790', 0, -1, 1616485096, 1616485096);

INSERT INTO TechBaseVN.group_tab (group_name, is_deleted, created_time, updated_time) VALUES ('Group_1', 0, 1616465848, 1616465848);
INSERT INTO TechBaseVN.group_tab (group_name, is_deleted, created_time, updated_time) VALUES ('Group_2', 0, 1616465848, 1616465848);
INSERT INTO TechBaseVN.group_tab (group_name, is_deleted, created_time, updated_time) VALUES ('Group_3', 0, 1616465848, 1616465848);

INSERT INTO TechBaseVN.team_tab (team_name, is_deleted, created_time, updated_time) VALUES ('Team_1', 0, 1616465848, 1616465848);
INSERT INTO TechBaseVN.team_tab (team_name, is_deleted, created_time, updated_time) VALUES ('Team_2', 0, 1616465848, 1616465848);
INSERT INTO TechBaseVN.team_tab (team_name, is_deleted, created_time, updated_time) VALUES ('Team_3', 0, 1616465848, 1616465848);
INSERT INTO TechBaseVN.team_tab (team_name, is_deleted, created_time, updated_time) VALUES ('Team_4', 0, 1616465848, 1616465848);

INSERT INTO TechBaseVN.role_tab (role_name, alias, created_time, updated_time) VALUES ('Manager', 'manager', 1616465848, 1616465848);
INSERT INTO TechBaseVN.role_tab (role_name, alias, created_time, updated_time) VALUES ('Group Manager', 'group_manager', 1616465848, 1616465848);
INSERT INTO TechBaseVN.role_tab (role_name, alias, created_time, updated_time) VALUES ('User', 'user', 1616465848, 1616465848);

INSERT INTO TechBaseVN.group_team_tab (group_id, team_id, created_time) VALUES (1, 1, 1616475354);
INSERT INTO TechBaseVN.group_team_tab (group_id, team_id, created_time) VALUES (2, 2, 1616475354);
INSERT INTO TechBaseVN.group_team_tab (group_id, team_id, created_time) VALUES (3, 3, 1616475354);
INSERT INTO TechBaseVN.group_team_tab (group_id, team_id, created_time) VALUES (1, 4, 1616475354);


INSERT INTO TechBaseVN.user_group_tab (user_id, group_id, created_time) VALUES (2, 1, 1616551984);
INSERT INTO TechBaseVN.user_group_tab (user_id, group_id, created_time) VALUES (3, 2, 1616551984);
INSERT INTO TechBaseVN.user_group_tab (user_id, group_id, created_time) VALUES (4, 3, 1616551984);


INSERT INTO TechBaseVN.user_role_tab (user_id, role_id, created_time) VALUES (1, 1, 1616475354);
INSERT INTO TechBaseVN.user_role_tab (user_id, role_id, created_time) VALUES (2, 2, 1616475354);
INSERT INTO TechBaseVN.user_role_tab (user_id, role_id, created_time) VALUES (3, 2, 1616475354);
INSERT INTO TechBaseVN.user_role_tab (user_id, role_id, created_time) VALUES (4, 2, 1616475354);
INSERT INTO TechBaseVN.user_role_tab (user_id, role_id, created_time) VALUES (5, 3, 1616475354);
INSERT INTO TechBaseVN.user_role_tab (user_id, role_id, created_time) VALUES (6, 3, 1616475354);
INSERT INTO TechBaseVN.user_role_tab (user_id, role_id, created_time) VALUES (7, 3, 1616475354);
INSERT INTO TechBaseVN.user_role_tab (user_id, role_id, created_time) VALUES (8, 3, 1616475354);
INSERT INTO TechBaseVN.user_role_tab (user_id, role_id, created_time) VALUES (9, 3, 1616475354);
INSERT INTO TechBaseVN.user_role_tab (user_id, role_id, created_time) VALUES (10, 3, 1616475354);
INSERT INTO TechBaseVN.user_role_tab (user_id, role_id, created_time) VALUES (11, 3, 1616475354);

INSERT INTO TechBaseVN.user_team_tab (user_id, team_id, created_time) VALUES (5, 1, 1616475354);
INSERT INTO TechBaseVN.user_team_tab (user_id, team_id, created_time) VALUES (6, 1, 1616475354);
INSERT INTO TechBaseVN.user_team_tab (user_id, team_id, created_time) VALUES (7, 2, 1616475354);
INSERT INTO TechBaseVN.user_team_tab (user_id, team_id, created_time) VALUES (8, 2, 1616475354);
INSERT INTO TechBaseVN.user_team_tab (user_id, team_id, created_time) VALUES (9, 3, 1616475354);
INSERT INTO TechBaseVN.user_team_tab (user_id, team_id, created_time) VALUES (10, 3, 1616475354);
INSERT INTO TechBaseVN.user_team_tab (user_id, team_id, created_time) VALUES (5, 3, 1616475354);
INSERT INTO TechBaseVN.user_team_tab (user_id, team_id, created_time) VALUES (8, 3, 1616475354);
INSERT INTO TechBaseVN.user_team_tab (user_id, team_id, created_time) VALUES (11, 4, 1616475354);
INSERT INTO TechBaseVN.user_team_tab (user_id, team_id, created_time) VALUES (2, 1, 1616475354);
INSERT INTO TechBaseVN.user_team_tab (user_id, team_id, created_time) VALUES (3, 2, 1616475354);
INSERT INTO TechBaseVN.user_team_tab (user_id, team_id, created_time) VALUES (4, 3, 1616475354);

