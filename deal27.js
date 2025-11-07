


function calculateAreaNormal(length, width) {
  return length * width;
}


const calculateAreaArrow = (length, width) => {
  return length * width;
};


console.log("Normal Function Area:", calculateAreaNormal(5, 10)); 
console.log("Arrow Function Area:", calculateAreaArrow(5, 10)); 



const name = "Alex";
const age = 28;
const hobby = "coding";


const sentence = `${name} is ${age} years old and loves ${hobby} in their free time.`;

console.log("\nTemplate Literal Output:");
console.log(sentence);


const delayedPromise = new Promise((resolve, reject) => {
  
  setTimeout(() => {
   
    resolve("The Promise has successfully resolved after 2 seconds!");
  }, 2000); 
});

console.log("\nStarting Promise...");


delayedPromise.then((message) => {
  console.log("Promise Resolved:");
  console.log(message);
});

console.log("This message appears immediately, before the promise resolves.");