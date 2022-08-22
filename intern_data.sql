LOCK TABLES `user` WRITE;

insert into user (id, user_name, email_adress, password, is_manager, is_deleted, note) 
values 
(1, 'a', 'a@gmail.com', a, True, False, 'A会社の社長です'),
(1, 'b', 'b@gmail.com', b, True, False, 'B会社の社長です'),
(1, 'c', 'c@gmail.com', c, True, False, 'C会社の社長です'),
(1, 'd', 'd@gmail.com', d, True, False, 'D会社の社長です'),
(1, 'e', 'e@gmail.com', e, True, False, 'E会社の社長です');

/* insert into device (id, device_name, is_deleted, note) 
values 
(1, 'd_a', False, 'A会社のデバイスです'),
(1, 'd_b', False, 'B会社のデバイスです'),
(1, 'd_c', False, 'C会社のデバイスです'),
(1, 'd_d', False, 'D会社のデバイスです'),
(1, 'd_e', False, 'E会社のデバイスです'); */

