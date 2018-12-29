create schema bank;
use bank;
create table Person (
CNIC  varchar(12),
Name varchar(25) not null,
PhoneNo varchar(11) not null unique,
constraint person_pk primary key (CNIC),
constraint chk_person_CNIC check(length(CNIC)=12)
);

create table address(
CNIC  varchar(12) not null unique,
City varchar(10) not null,
streetNo varchar(5) not null,
streetName varchar(30) not null,
constraint chk_address_CNIC check(length(CNIC)=12),
constraint address_person_fk foreign key (CNIC) references Person(CNIC) on delete cascade
);

create table Employee (
EmpID int unsigned auto_increment,
CNIC  varchar(12) not null,
Passwords varchar(8) not null,
constraint employee_pk primary key (EmpID),
constraint chk_employee_CNIC check(length(CNIC)=12),
constraint employee_person_fk foreign key (CNIC) references Person(CNIC) on delete cascade
);

create table Customer (
CustomerID int unsigned auto_increment,
CNIC  varchar(12) not null,
Passwords varchar(8) not null,
constraint customer_pk primary key (CustomerID),
constraint chk_customer_CNIC check(length(CNIC)=12),
constraint customer_person_fk foreign key (CNIC) references Person(CNIC) on delete cascade
);

create table Sender (
SenderID int unsigned ,
constraint sender_customer_fk foreign key (SenderID) references Customer(CustomerID) on delete cascade
);

create table Receiver (
ReceiverID int unsigned ,
constraint reciever_customer_fk foreign key (ReceiverID) references Customer(CustomerID) on delete cascade
);

create table Transactions(
TransID int unsigned auto_increment,
Amount decimal (8,2) default 0.0 not null,
DateOfTransfer datetime default now(), 
TSenderID int unsigned ,
TReceiverID int unsigned ,
TEmpID int unsigned ,
constraint transactions_pk primary key (TransID),
constraint transactions_sender_fk foreign key (TSenderID) references Sender(SenderID) ,
constraint transactions_receiver_fk foreign key (TReceiverID) references Receiver(ReceiverID) ,
constraint transactions_employee_fk foreign key (TEmpID) references Employee(EmpID)
);

create table Accounts(
AccountNo int unsigned auto_increment,
Balance decimal  (8,2) unsigned default 0.0 not null,
Activation bool default true,
CNIC  varchar(12) not null,
constraint accounts_pk primary key (AccountNo),
constraint accounts_person_fk foreign key (CNIC) references Person(CNIC)
);


create table SavingsAccount(
SavingsAccountNo int unsigned ,
limits decimal unsigned default 0.0,
interestRate decimal(3,2) unsigned default 0.08,
constraint savings_accounts_fk foreign key (SavingsAccountNo) references Accounts(AccountNo) on delete cascade,
constraint chk_savings_interestRate check(interestRate = 0.08)
);

create table CurrentAccount(
CurrentAccountNo int unsigned auto_increment,
interestRate decimal(3,2) unsigned default 4.0,
constraint current_accounts_fk foreign key (CurrentAccountNo) references Accounts(AccountNo) on delete cascade,
constraint chk_current_interestRate check(interestRate = 4.0)
);

create table card(
cardNo int unsigned auto_increment,
expiryDate date default '2023-12-31',
pin int unsigned ,
AccountNo int unsigned ,
limits int unsigned default 5,
totalTransactions double unsigned default 0.0,
constraint card_pk primary key (cardNo),
constraint card_accounts_fk foreign key (AccountNo) references Accounts(AccountNo),
constraint chk_pin check(pin < 10000)
);
