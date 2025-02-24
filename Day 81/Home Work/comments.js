//  ობიექტი (Object) არის კონკრეტული მონაცემთა ერთეული, რომელიც შეიცავს სხვადასხვა კუთვნილებებს და მეთოდებს
//  კუთვნილება (Property) არის ობიექტის კონკრეტული მონაცემი (მაგალითად: სახელი, ასაკი)
//  მეთოდი (Method) არის ფუნქცია, რომელიც ეკუთვნის ობიექტს და შეუძლია რაიმე ოპერაციის შესრულება

// ჩემი თავის ობიექტი
let myself = {
    name: "Zuka",
    surname: "udzlieresi",
    age: 16
};


let familyMember = {
    name: "gocha",
    surname: "sheucherebeli",
    age: 60
};


console.log("Myself:", myself);
console.log("Family Member:", familyMember);


console.log("My Name:", myself.name);
console.log("My Surname:", myself.surname);
console.log("My Age:", myself.age);

console.log("Family Member Name:", familyMember.name);
console.log("Family Member Surname:", familyMember.surname);
console.log("Family Member Age:", familyMember.age);


myself.age = 26;
familyMember.age = 51;

console.log("Updated Myself:", myself);
console.log("Updated Family Member:", familyMember);


myself.city = "Tbilisi";
familyMember.city = "Kutaisi";

console.log("Myself with new attribute:", myself);
console.log("Family Member with new attribute:", familyMember);


delete familyMember.surname;

console.log("Myself after deleting surname:", myself);
console.log("Family Member after deleting surname:", familyMember);


myself.sayHello = function () {
    console.log("Hello World!");
};

familyMember.sayHello = function () {
    console.log("Hello World!");
};


myself.sayHello();
familyMember.sayHello();

