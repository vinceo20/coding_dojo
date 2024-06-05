/* case insensitive string compare */

const strA1 = "ABC";
const strB1 = "abc";
const expected1 = true;

const strA2 = "ABC";
const strB2 = "abd";
const expected2 = false;

const strA3 = "ABC";
const strB3 = "bc";

// function caseInsensitiveStringCompare (strA, strB) {
//     if(strA.length === strB.length) {
//         if(strA.toUpperCase() === strB.toUpperCase()) {
//             return true;
//         } else{
//             return false;
//         } 
//     } else {
//         return false;
//     }
// }

function caseInsensitiveStringCompare (strA, strB) {
    return strA.toUpperCase() === strB.toUpperCase()
}

console.log(caseInsensitiveStringCompare(strA1,strB1))
console.log(caseInsensitiveStringCompare(strA2,strB2))
console.log(caseInsensitiveStringCompare(strA3,strB3))
console.log(caseInsensitiveStringCompare(strA4,strB4))