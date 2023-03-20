sig Username {} {
	this in User.username
}

sig Password {} {
	this in User.password
}

sig Email {} {
	this in User.email
}

sig User {
	username: Username,
	password: Password,
	email: Email
}

fact {
	all u1, u2: User | u1 != u2 => 
	u1.username != u2.username &&
	u1.email != u2.email
}

assert UniqueUser {
	all u1, u2: User | u1 != u2 => 
	u1.username != u2.username ||
	u1.email != u2.email
}

check UniqueUser {}
run {} for 3
