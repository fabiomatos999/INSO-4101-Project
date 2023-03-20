sig Username {}{
	this in Seller.username
}
sig Pictures {}{
	this in ShoeEntry.pictures
}

sig Date {}{
	this in ShoeEntry.date
}

sig Password {}{
	this in Seller.password
}

sig Address {} {
	this in Seller.address
}

sig BusinessLicense {}{
	this in Seller.license
}

sig Email {} {
	this in Seller.email
}

sig Video {}{
	this in ShoeEntry.video
}

sig ShoeEntry {
	shoe: Shoe,
	pictures: set Pictures,
	video: Video,
	date : Date,
} {
	this in Seller.entries
}

sig Seller {
	username: Username,
	entries : set ShoeEntry,
	password: Password,
	address: Address,
	license: BusinessLicense,
	email: Email
}
sig Shoe {} {
	this in ShoeEntry.shoe
}
pred ShoeEntryAmmount {
	#ShoeEntry.pictures >= 4 &&
	#ShoeEntry.video = 1
}

fact {
	all s1,s2 : Seller | s1 != s2 =>
	s1.username != s2.username && 
	s1.entries not in s2.entries &&
	s2.entries not in s1.entries &&
	s1.address != s2.address &&
	s1.license != s2.license && 
	s1.email != s2.email
}

fact {
	all e1,e2: ShoeEntry | e1 != e2 => 
	e1.pictures not in e2.pictures &&
	e2.pictures not in e1.pictures &&
	e1.video != e2.video
}

assert UniqueSeller {
	all s1, s2: Seller| s1.username != s2.username &&
	s1.username != s2.username ||
	s1.entries not in s2.entries ||
	s2.entries not in s1.entries ||
	s1.address != s2.address ||
	s1.license != s2.license
}

assert UniqueEntry {
	all e1,e2: ShoeEntry | e1 != e2 => 
	e1.pictures not in e2.pictures ||
	e2.pictures not in e1.pictures ||
	e1.video != e2.video
}

//check UniqueSeller {} 
//check UniqueEntry {}

run {} for 3
