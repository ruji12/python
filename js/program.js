// console.log("hello world");
// let a = prompt("Hey whats your age?");
// a = Number . parseInt(a);
// if(a>0)
// {
//     console.log("This is a valid age");
// }
// else{

// }

// let a = prompt("Hey what's your age?");

// if(a>10 && a<20){
//     console.log("Your age lies between 10 and 20");
// }
// else{
//     console.log("Your age doesnot lies between 10 and 20");
// // }
// let age = prompt("Hey what's your age?");
// if(age%2==0 || age%3==0){
//    console.log("Your age is divisible by 2 and 3:");
// }
// else{
//     console.log("Your age is notdivisible by 2 and 3:");

// }
// let age = 20;
// let a = age > 18 ? "You can drive" :"You cannot drive";
// console.log(a);



//loops

// let n = prompt("Enter the value of n ");
// let i =0;
// do{
//     console.log(i);
//     i++;
// }while(i<n)

//for loop
// 
/*let sum = 0;
let n = prompt("Enter the value of n:");
for(let i=0;i<n;i++)
{
    sum +=i+1;
}
console.log("Sum of"+n+"are"+sum);*/


// for in loop
// let obj ={
//     "rujita":20,
//     "rohan":30,
//     "rus":70,
//     "nisha":90
// }
// for(a in obj){
//     console.log("the value of" +a+"are" +(obj[a]));

// }

//for of loop

// for(a of "rujita"){
//     console.log(a);
// }


// const sum =(a,b)=>{
//     let c = a+b;
//     return c;

// }
// let y = sum(2,4);
// console.log(y);

// practice set 3

// let obj={
//     rujita:90,
//     rohan:70,
//     aakash:30

// }
// for(a in obj){
//     console.log("The marks of"+a+"are"+obj[a]);
// }



// qn-2

// let num=23
// let i
// while (i!=num){
//     i=prompt("Enter a number:");
//     console.log("Try Again:");
// }
// console.log("You have entered correct number:");


// qn-3


// const mean =(a,d,c,d,e)=>{
//     return(a+b+c+d+e)/5;
// }
// console.log(mean(1,5,8,9,3));



//strings in javascript

// let name ="Rujitalage";
// console.log(name.length);

// let boy1 = "Nishan";
// let boy2 = "Arun";

// let a = `${boy1} is a friend of ${boy2}`;
// console.log(a);

//escape sequence characters

// let name = `D\' Adam`;
// console.log(name);

// let a = "hello\tworld";
// console.log(a);


//string properties


// let name = "rujita";
// console.log(name.toLowerCase());
// console.log(name.slice(2,4));
// console.log(name.slice(2));
// let newname = name . replace("rujita","rushali");
// console.log(newname);

// let a1 ="Rujita ";
// let a2 ="Lage";
// let a3 =a1.concat(a2);
// console.log(a3);


// let name ="Nishan";
// let friend ="Arun";

// console.log(name.concat("is a friend of",friend));



// let a2 ="             Rujita             ";
// console.log(a2.trim());
// console.log(a2);


//String set practise
// let str ="har\""
// console.log(str.length)


//prblm-2


// const sentence = 'The quick brown fox jumps over the lazy dog.';
// let word ="fox";
// console.log(sentence.includes(word));
// console.log(`The word"${word}" ${sentence.includes(word) ? 'is':'is not'} in the sentence`);
// console.log(typeof sentence);


//problem-3
// let name ="rujita";
// console.log(name.toUpperCase());

//Arrays

// let marks =[12,76,90,23];
// console.log(marks[0]);
// console.log(marks[1]);
// console.log(marks[2]);
// console.log(marks[3]);
// console.log(marks[4]);
// console.log(marks.length);
// marks[0]=70;
// marks[4]=90;
// console.log(marks);

//Printing array in loop

// let marks =[12,76,90,23];
// for(let i=0;i<marks.length;i++)
// {
//     console.log(marks[i]);
// }
// console.log(marks.length);


//Array Methods

// let n = [1,4,5,7];
// let r = n.toString();
// console.log(typeof r);

// let f = n.join("and");
// console.log(f);

//  let r = n.pop();
// console.log(n,r);

// let r = n.unshift(3);
// console.log(r,n);


// delete()
// let num = [1,6,7,8,9,2]
// console.log(num.length);
// delete num[0];
// console.log(num.length);

// Concat()
// let a1=[1,2,3,4];
// let a2=[1,2,3,4];
// let a3=[1,2,3,4];
// let a4=[1,2,3,4];

// let r = a1.concat(a2,a3,a4);
// console.log(r);

// Sort method
// let compare = (a,b)=>{
//     return a - b;
// }

// let  num = [124,7789,445,2,3,888];
// num.sort(compare);
// console.log(num); //will be sortted in an ascending order

// let  n= [124,7789,445,2,3,888];
// num.sort();
// console.log(n);
//will be sortted in an alphabetical order


//SPLICE()

// const num =[23,67,8,89,90];
// num.splice(2,3,234,567,890);
// console.log(num);


//for each loop


// let num =[1,3,4,5,6]

// for(let i=0;i<num.length;i++){
//     console.log(num[i*i]);
// }

// num.forEach((element)=>{
//     console.log(element*element)
// })

// let name ="RujitaLage"
// let arr = Array.from(name)
// console.log(arr)


// for...of

// for(let i of num){
//     console.log(i)
// }


// maps filter and reduce

// let arr = [1,4,5,6]

// let a = arr.map((value,index)=>{
//     // console.log(value,index)
//     return value + index;
// })
// console.log(a) 
// maps is used to create a new array.



// Array filter method

// let arr = [23,56,30,10,40]

//   let a=arr.filter((value)=>{
//     return value<50
// })
// console.log(a)




// Array reduce method
// let arr =[1,3,5,7,9]
// let a=arr.reduce((h1,h2)=>{
//     return h1+h2
// })
// console.log(a)


// chapter 5 practise set


// prblm-1
// let arr = [1, 2, 3, 5]
// let a

// prblm-2
// do {
//     a = prompt("Enter a number:")
//     a = Number.parseInt(a)
//     arr.push(a)
//     // console.log(arr)



// } while (a != 0)
// console.log(arr)


// prblm-3

// let arr=[1,2,34,5,6,10,20]
// let a = arr.filter((x)=>{
//     return x%10 == 0
// })
// console.log(a)

// prblm-4

// let arr=[1,2,34,5,6,10,20]
// let a = arr.map((x)=>{
//     return x*x
// })
// console.log(a)


// prblm-5

// let arr = [1,2,3,4,5]
// let a= arr.reduce((x1,x2)=>{
//     return x1*x2

// })
// console.log(a)



// console.time("forLoop")
// for (let i = 0; i < 5; i++) {
//     console.log(i)

// }

// console.timeEnd("forLoop")


// alert("Enter the value of a:")
// let a = prompt("Enter a here");
// document.write(a)

// alert("Enter the value of a!")
// let a = prompt("Enter a here")
// a = Number.parseInt(a)
// alert("You entered a of type" +(typeof a))
// let write = confirm("Do you want to write it to the page:");
// if(write){
//     document.write(a)
// }
// else{
//     document.write("Please allow me to write")
// }


// practise set-6
// let a = prompt("what's your age?")
// const canDrive = (a)=>{
// return a>=18?"you can drive":"you cannot drive"

// }
// runagain = true
// while(runagain)

// {
//     let a = prompt("what's your age?")
//     if(a<0){
//         console.error("please enter a valid age")
//         break;
//     }
//     if(canDrive(a)){
//     alert("You can drive")
// }
// else{
//     alert("You cannot drive")
// }
// runagain = confirm("You want to run again??")
// // if(a<0){
// //     console.error("you entered wrong")
// // }

// }



// let num = prompt("Enter a number")
// if (num<4){
//     location.href="https://google.com"
// }

// let color = prompt("Enter the page background color")
// document.body.style.background = color

// console.log(document.body.firstChild)
// console.log(document.body.lastChild)

// const changeBgRed = () =>{
//     document.body.firstElementChild.style.background = "blue"
// }

// let b = document.body
// console.log("First child of b is:",b.firstChild)
// console.log("First child of b is:",b.firstElementChild)
// let parent = document.getElementById('parent');
// let children = parent.children;
// console.log(children);



// 

// var name ="Rujita Lage"
// name.split()
// console.log(name)

// name.split(/\s+/)
// console.log(name)



// var fullnames = ["Rujita Lage","Nisha Lagge" ,"Rushali Lage"]
//  var firstandlastnames = []

// for(fullname of fullnames){
//     var name = fullname.split(/\s+/)
//     var firstandlastname ={
//         firstname : name[0],
//         lastname : name[1]


//     }
//     firstandlastnames.push(firstandlastname)
// }
// console.log(firstandlastnames)



