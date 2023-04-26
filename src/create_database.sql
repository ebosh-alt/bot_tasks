create table referral_statuses(
    id integer primary key,
    name nvarchar(25),
    reward_lvl_1 integer default 0,
    reward_lvl_2 integer default 0
);

create table documents(
    id integer primary key,
    name nvarchar(25)
);

create table country(
    id integer primary key,
    name nvarchar(25)
);

create table payment_methods(
    id integer primary key,
    name nvarchar(25)
);

create table users(
    id integer primary key,
    status bool default TRUE,
    referral_link text,
    referral_boss_id integer default null,
    referral_status_id integer,
    firstname nvarchar(25),
    lastname nvarchar(25),
    patronymic nvarchar(25),
    document_id integer,
    country_id integer,
    registration_date integer,
    full_registered bool default FALSE,
    username nvarchar(25),
    payment_method_id integer, --change
    withdrawal_account text,
    balance integer default 0,
    earnings integer default 0,
    count_no_verified integer default 0,
    count_verified_paid integer default 0,
    count_verified_rejected integer default 0,
    flag integer,
    bot_message_id integer,
    delete_message_id integer default null,
    foreign key(referral_boss_id) references users(id),
    foreign key(referral_status_id) references referral_statuses(id),
    foreign key(document_id) references documents(id),
    foreign key(country_id) references country(id),
    foreign key(payment_method_id) references payment_methods(id)
);

create table faq(
    id integer primary key,
    name nvarchar(20),
    link text
);

create table admins(
    id integer primary key,
    text_for_mailing text,
    name_button_for_mailing nvarchar(20),
    link_button_for_mailing text,
    flag integer,
    bot_message_id integer,
    delete_message_id integer default null
);

create table managers(
    id integer primary key,
    current_task_id integer default null, -- ref
    user_id integer default null,
    foreign key(current_task_id) references tasks(id),
    foreign key(user_id) references users(id)
);

create table tasks(
    id integer primary key,
    name nvarchar(20),
    description text,
    number_of_executions integer,
    number_of_completed integer,
    price integer,
    deadline integer,
    status bool default TRUE
);

create table tasks_users(
    id integer primary key,
    user_id integer,
    task_id integer,
    completion_date integer,
    foreign key(task_id) references tasks(id),
    foreign key(user_id) references users(id)
);



