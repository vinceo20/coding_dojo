/*
    Given an arr and a separator string, output a string of every item in the array separated by the saparator.

    No trailing separator at the end
    Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3]
const separator2 = "-"
const expected2 = "1-2-3"

const arr3 = [1, 2, 3]
const separator3 = " - "
const expected3 = "1 - 2 - 3"

const arr4 = [1]
const separator4 = ", "
const expected4 = "1"

const arr5 = []
const separator5 = ", "
const expected5 = "";

function concatArrWithSep (arr, separator) {
    let result = arr.join(separator);
    // for (let i = 0; i < arr.length; i++){
    //     result += (arr[i])
    //     result +=(separator)
    // }
    return result
}
console.log(concatArrWithSep(arr1, separator1))
console.log(concatArrWithSep(arr2, separator2))
console.log(concatArrWithSep(arr3, separator3))
console.log(concatArrWithSep(arr4, separator4))
console.log(concatArrWithSep(arr5, separator5))

// =======================================================================================

/**
Turns the given str into an acronym

 */

const str1 = "object oriented programming"
const exp1 = "OOP";

const str2 = "abstraction polymorphism inheritance encapsulation"
const exp2 = "APIE"

const str3 = "software development life cycle"
const exp3 = "SDLC"

const str4 = "       global        information tracker          "
const exp4 = "GIT"

// function acronymize (str) {
//     let result = "";
//     let tempArr = str.split(" ")
//     for (let i = 0; i < tempArr.length; i++){
//         if (tempArr[i][0] == " "){
//             continue
//         }
//         result += tempArr[i][0].toUpperCase()
//     }
//     console.log(result)
// }

function acronymize (str) {
    let result = "";
    for (let word of str.split(" ")){
        if (word === "") continue
        result += word[0].toUpperCase()
    }
    return result
}

console.log(acronymize(str1))
console.log(acronymize(str2))
console.log(acronymize(str3))
console.log(acronymize(str4))