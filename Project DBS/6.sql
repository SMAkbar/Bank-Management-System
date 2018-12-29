create or replace view card_details as
 select c.cardNo as cardNo, a.AccountNo as AccountNo, 
 p.Name as Name, c.expiryDate as expiryDate, c.limits as limits, c.pin as pin
 from card c join accounts a using (AccountNo) join person p using (CNIC);
 
 create or replace view emp_details as
 select e.EmpID as EmpID, e.CNIC as CNIC, p.Name as Name, p.PhoneNo as PhoneNo
 from employee e join person p using (CNIC);
 
 create or replace view acc_details as
 select a.AccountNo as AccountNo, p.Name as Name, 
 a.Balance as Balance, a.Activation as Activation
 from accounts a join person p using (CNIC);
 
 create or replace view atm as select * from
 card join accounts using (AccountNo)
 join person using (CNIC);