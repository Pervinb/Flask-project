create table User(
    id integer primary key,
    user_name varchar(50),
    user_mail varchar(50),
    user_type varchar(50)
)
 
--table silmek
drop table  User 

--yeni sutun elave etmek

alter table User
add column user_email varchar(50)

--column silmek

alter table User
drop column user_email

--lesson table

create table Lessons(
    id integer primary key,
    lesson_name varchar(70)
    
)

-- files table

create table files(
    id integer primary key,
    file_name varchar(100),
    file_type  varchar(50),
    file_url varchar(70)
)

create table Lessonsfiles(
    id integer primary key,
    file_id integer,
    lesson_id integer,
    constraint lesson
    foreign key (file_id)
    references files(id),
    foreign key (lesson_id)
    references Lessons(id)
)


insert into files(file_name,file_type,file_url)
values ('integer','jpg','files/integer.jpg'),
('manual','txt','files/manual.txt'),
('deyisenVideo','mp4','files/deyisenVideo.mp4')

select * from files


insert into Lessons(lesson_name)
values('Deyisenler')

select * from Lessons;
select * from files;
select * from Lessonsfiles;

drop table files;
drop table Lessons;

insert into Lessonsfiles(file_id,lesson_id)
values(1,1),
(1,2),
(2,1)

select file_id from Lessonsfiles where lesson_id=1;
select * from files;

select lesson_id from Lessonsfiles where file_id=1;
select * from Lessons;