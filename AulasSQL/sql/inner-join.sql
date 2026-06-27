select users.id as uid, profiles.id as pid,
profiles.bio, users.first_name 
from users, profiles
where users.id = profiles.user_id

select u.id as uid, p.id as pid,
p.bio, u.first_name
from users as u
inner join profiles as p
on u.id = p.user_id
where u.first_name like '%a'
limit 100