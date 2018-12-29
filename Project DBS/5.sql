drop view if exists userData;

create view userData as  select acc.AccountNo,p.CNIC, p.Name, cus.passwords, p.PhoneNo,acc.Balance, ad.city, ad.streetNo, ad.streetName,c.cardNo
 from person as p join accounts as acc using (CNIC) join address as ad using (CNIC) join card as c using (accountno) join customer as cus using (CNIC);
 
drop view if exists userData2;

create view userData2 as  
select acc.AccountNo, acc.Balance, p.CNIC, p.Name, p.PhoneNo, ad.city, ad.streetName
from accounts as acc join person as p using(CNIC)
join address as ad using(CNIC);
 